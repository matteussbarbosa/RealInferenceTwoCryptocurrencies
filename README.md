## Overview

This module implements the statistical logic required to perform **hypothesis tests based on Student’s t-distribution** (*t-test*). It is intended for inferential analysis when the population standard deviation is unknown and/or the sample size is limited.

The design emphasizes conceptual clarity and separation between:

* the t distribution;
* the t statistic;
* the hypothesis testing decision rule.

---

## Statistical Background

### Student’s t Distribution

The **Student’s t distribution** arises when a population mean is estimated using a finite sample and the population standard deviation is unknown. Its shape depends on the **degrees of freedom**, typically:

[
\nu = n - 1
]

As the degrees of freedom increase, the t distribution converges to the standard normal distribution.

---

### t Statistic

The **t statistic** measures how far an estimated parameter deviates from its null-hypothesis value, scaled by its standard error:

[
t = \frac{\hat{\theta} - \theta_0}{SE(\hat{\theta})}
]

where:

* ( \hat{\theta} ) is the parameter estimate;
* ( \theta_0 ) is the null-hypothesis value;
* ( SE(\hat{\theta}) ) is the standard error.

---

### t-test

The **t-test** is the full inferential procedure that combines:

1. the t statistic;
2. the appropriate t distribution;
3. a significance level (( \alpha ));
4. the *p-value*;
5. a decision rule.

This module implements **two-sided hypothesis tests**, with a structure that can be easily extended to one-sided tests.

---

## Hypotheses

The standard hypothesis formulation is adopted:

* **Null hypothesis (H₀):** the population parameter equals a reference value.
* **Alternative hypothesis (H₁):** the population parameter differs from the reference value.

Example:

* H₀: ( \theta = \theta_0 )
* H₁: ( \theta \neq \theta_0 )

---

## Module Workflow

Conceptually, the module performs the following steps:

1. Receives as input:

   * parameter estimate;
   * standard error;
   * degrees of freedom;
   * significance level (( \alpha )).
2. Computes the t statistic.
3. Computes the *p-value* using the Student’s t distribution.
4. Compares the *p-value* with ( \alpha ).
5. Returns the statistical decision:

   * **Reject H₀** if ( p \leq \alpha );
   * **Fail to reject H₀** otherwise.

---

## Output

The module returns a structured result containing:

* t statistic;
* *p-value*;
* significance level;
* hypothesis test decision.

This structure supports integration with quantitative pipelines and automated reporting.

---

## Assumptions and Limitations

* Observations are assumed to be independent.
* The estimator is assumed to be approximately normally distributed (or the data are approximately normal in small samples).
* Statistical significance should always be interpreted alongside **practical or economic significance**.

---

## Conclusion

This module provides a concise and statistically sound implementation of the **Student’s t hypothesis test**, serving as a foundational component for inferential analysis in scientific and quantitative projects.
