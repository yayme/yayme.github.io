import tkinter as tk
from tkinter import ttk, messagebox
import re

# Constants
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
start_hour = 8
end_hour = 20
slot_minutes = 30

# Helper functions
def time_to_str(hour, minute):
    return f"{hour:02}:{minute:02}"

def slot_label(start_h, start_m, slot_m=slot_minutes):
    end_h = start_h + (start_m + slot_m) // 60
    end_m = (start_m + slot_m) % 60
    # Add line break for compactness
    return f"{time_to_str(start_h, start_m)}\n–\n{time_to_str(end_h, end_m)}"

def parse_time(s):
    m = re.match(r"(\d{1,2}):(\d{2})", s)
    if m:
        return int(m.group(1)), int(m.group(2))
    return None

def merge_slots(slots):
    # slots: list of (start_h, start_m)
    slots = sorted(slots)
    merged = []
    for sh, sm in slots:
        if not merged:
            end_h, end_m = sh, sm + slot_minutes
            if end_m >= 60:
                end_h += end_m // 60
                end_m %= 60
            merged.append([[sh, sm], [end_h, end_m]])
        else:
            last = merged[-1]
            # If current slot starts at the end of last slot, merge
            if (sh, sm) == (last[1][0], last[1][1]):
                # Extend last's end
                end_h, end_m = sh, sm + slot_minutes
                if end_m >= 60:
                    end_h += end_m // 60
                    end_m %= 60
                last[1][0], last[1][1] = end_h, end_m
            else:
                end_h, end_m = sh, sm + slot_minutes
                if end_m >= 60:
                    end_h += end_m // 60
                    end_m %= 60
                merged.append([[sh, sm], [end_h, end_m]])
    return [((s[0][0], s[0][1]), (s[1][0], s[1][1])) for s in merged]

def slots_to_text(day_slots):
    lines = []
    for i, slots in enumerate(day_slots):
        if not slots:
            continue
        merged = merge_slots(slots)
        slot_strs = [f"{time_to_str(s[0][0], s[0][1])}–{time_to_str(s[1][0], s[1][1])}" for s in merged]
        lines.append(f"{days[i]}: {', '.join(slot_strs)}")
    return "\n".join(lines)

def text_to_slots(text):
    day_slots = [[] for _ in days]
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        for i, day in enumerate(days):
            if line.startswith(day):
                times = re.findall(r"(\d{1,2}:\d{2})–(\d{1,2}:\d{2})", line)
                for t1, t2 in times:
                    sh, sm = parse_time(t1)
                    eh, em = parse_time(t2)
                    # Add all slots in this range
                    cur_h, cur_m = sh, sm
                    while (cur_h, cur_m) < (eh, em):
                        day_slots[i].append((cur_h, cur_m))
                        cur_m += slot_minutes
                        if cur_m >= 60:
                            cur_h += 1
                            cur_m = 0
                break
    return day_slots

class TimeslotApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Timeslot Selector")
        self.resizable(False, False)
        self.day_slot_vars = [[tk.BooleanVar() for _ in range(self.num_slots())] for _ in days]
        self.build_ui()
        self.update_textboxes_from_slots()

    def num_slots(self):
        return ((end_hour - start_hour) * 60) // slot_minutes

    def build_ui(self):
        main = ttk.Frame(self)
        main.pack(padx=10, pady=10)
        # Timeslot view (narrower)
        slot_frame = ttk.LabelFrame(main, text="Timeslot View")
        slot_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 10))
        for d, day in enumerate(days):
            ttk.Label(slot_frame, text=day, width=8, anchor="w").grid(row=d+1, column=0, sticky="w")
        for s in range(self.num_slots()):
            h = start_hour + (s * slot_minutes) // 60
            m = (s * slot_minutes) % 60
            lbl = slot_label(h, m)
            # Make slot label narrower
            ttk.Label(slot_frame, text=lbl, width=7).grid(row=0, column=s+1)
            for d in range(len(days)):
                cb = ttk.Checkbutton(slot_frame, variable=self.day_slot_vars[d][s], command=self.on_slot_change, width=2)
                cb.grid(row=d+1, column=s+1)

        # Plain text view: one textbox per day
        text_frame = ttk.LabelFrame(main, text="Plain Text View (per day)")
        text_frame.grid(row=0, column=1, sticky="nsew")
        self.day_texts = []
        for i, day in enumerate(days):
            row = ttk.Frame(text_frame)
            row.pack(fill="x", pady=1)
            ttk.Label(row, text=day+":", width=9, anchor="w").pack(side="left")
            txt = tk.Text(row, width=22, height=1, font=("Consolas", 11))
            txt.pack(side="left", fill="x", expand=True)
            self.day_texts.append(txt)
        # Sync button
        sync_btn = ttk.Button(main, text="Update from Textboxes", command=self.on_text_change)
        sync_btn.grid(row=1, column=1, sticky="e", pady=(5,0))

        # Overall summary box at the bottom
        summary_frame = ttk.LabelFrame(main, text="Overall Timeslots (for copy)")
        summary_frame.grid(row=2, column=0, columnspan=2, sticky="ew", pady=(10,0))
        self.summary_text = tk.Text(summary_frame, width=50, height=7, font=("Consolas", 11))
        self.summary_text.pack(fill="both", expand=True)
        self.summary_text.config(state="disabled")

    def on_slot_change(self):
        self.update_textboxes_from_slots()

    def on_text_change(self, event=None):
        # Read all day textboxes and update slot grid
        day_slots = []
        for i, txt in enumerate(self.day_texts):
            line = txt.get("1.0", tk.END).strip()
            if not line:
                day_slots.append([])
                continue
            # Parse all time ranges in the line
            slots = []
            times = re.findall(r"(\d{1,2}:\d{2})–(\d{1,2}:\d{2})", line)
            for t1, t2 in times:
                sh, sm = parse_time(t1)
                eh, em = parse_time(t2)
                if sh is None or sm is None or eh is None or em is None:
                    continue
                cur_h, cur_m = sh, sm
                while (cur_h, cur_m) < (eh, em):
                    slots.append((cur_h, cur_m))
                    cur_m += slot_minutes
                    if cur_m >= 60:
                        cur_h += 1
                        cur_m = 0
            day_slots.append(slots)
        # Update slot grid
        for d in range(len(days)):
            for s in range(self.num_slots()):
                h = start_hour + (s * slot_minutes) // 60
                m = (s * slot_minutes) % 60
                self.day_slot_vars[d][s].set((h, m) in day_slots[d])
        self.update_textboxes_from_slots(update_summary=True)

    def update_textboxes_from_slots(self, update_summary=True):
        # Update all day textboxes from slot grid
        all_day_slots = []
        for d in range(len(days)):
            slots = []
            for s in range(self.num_slots()):
                if self.day_slot_vars[d][s].get():
                    h = start_hour + (s * slot_minutes) // 60
                    m = (s * slot_minutes) % 60
                    slots.append((h, m))
            merged = merge_slots(slots)
            slot_strs = [f"{time_to_str(s[0][0], s[0][1])}–{time_to_str(s[1][0], s[1][1])}" for s in merged]
            text = ', '.join(slot_strs)
            self.day_texts[d].delete("1.0", tk.END)
            self.day_texts[d].insert("1.0", text)
            all_day_slots.append(merged)
        # Update summary box if requested
        if update_summary:
            summary_lines = []
            for i, merged in enumerate(all_day_slots):
                if not merged:
                    continue
                slot_strs = [f"{time_to_str(s[0][0], s[0][1])}–{time_to_str(s[1][0], s[1][1])}" for s in merged]
                summary_lines.append(f"{days[i]}:{' ' if slot_strs else ''}{', '.join(slot_strs)}")
            self.summary_text.config(state="normal")
            self.summary_text.delete("1.0", tk.END)
            self.summary_text.insert("1.0", "\n".join(summary_lines))
            self.summary_text.config(state="disabled")

if __name__ == "__main__":
    TimeslotApp().mainloop()
