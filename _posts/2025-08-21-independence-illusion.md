---
layout: post
title: "When Math Breaks Common Sense: The Independence Illusion"
subtitle: "Why X and X+Y aren't independent (except when they are?)"
date: 2025-08-21
gh-repo: yayme/normalsite
gh-badge: [follow]
tags: [probability, mathematics, bayesian-statistics]
comments: true
mathjax: true
author: Adnan Sadik
---

An easy exercise in probability is to ask: if two random variables $X$ and $Y$ are independent, is $X$ also independent of $X+Y$? The short answer is **no**—in general, they are not independent.

---

#### Quick Counter Argument

Take $X, Y \sim \text{Bernoulli}(1/2)$, independent. Then the pair $(X, X+Y)$ takes values like:

* $(0,0), (0,1), (1,1), (1,2)$

If we check independence formally, the joint distribution of $(X, X+Y)$ does not factorize into a product of marginals. For example,

$$
\mathbb{P}(X=0, X+Y=0) = 1/4, \quad \mathbb{P}(X=0) \cdot \mathbb{P}(X+Y=0) = 1/8.
$$

These are not equal. Hence, $X$ and $X+Y$ are dependent.

**Intuitively**: $X+Y$ contains information about $X$, so they cannot be independent.

---

#### A Thought Experiment with Translation Invariance

Now imagine a random number generator that outputs any integer (positive or negative) with equal chance, and each number it generates does not depend on any that came before. If such a thing existed:

* Generate $X$ and $Y$ independently from this "uniform over $\mathbb{Z}$."
* Consider the pair $(X, X+Y)$.

If you fix $X=x$, the distribution of $X+Y$ is just a shifted version of the "uniform over $\mathbb{Z}$." Because of translation invariance, every value of $X+Y$ is still equally likely. Likewise, conditioning on $X+Y=z$ gives no bias about $X$. In this setup, $X$ and $X+Y$ *behave as if they are independent*.

---

#### Connection to Improper Priors

Of course, we cannot define such a probability measure in the classical sense. However, this idea underpins **improper priors** in Bayesian statistics. For example, a "uniform prior over $\mathbb{R}$" is not a proper probability distribution, but it is translation-invariant. Using such priors allows Bayesian models to exploit symmetry properties and often leads to proper posterior distributions.

For a deeper dive, check out this [blogpost by Craig Gidney](https://algassert.com/post/1630).

---

