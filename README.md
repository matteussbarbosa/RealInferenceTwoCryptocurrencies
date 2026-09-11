# Statistical Inference for Two Cryptocurrencies

## Overview

This project implements statistical inference methods for analyzing cryptocurrency data using **Student's t-distribution and hypothesis testing**.

The implementation focuses on the statistical workflow required to evaluate whether an observed parameter differs significantly from a reference value.

## Objectives

* Implement the Student's t-distribution based hypothesis testing workflow.
* Calculate the t-statistic.
* Calculate p-values.
* Apply statistical decision rules.
* Structure the results for integration into quantitative analysis workflows.

## Technologies

* Python
* Statistical Analysis
* Inferential Statistics
* Hypothesis Testing
* Student's t-Distribution
* p-values

## Methodology

The hypothesis testing workflow consists of:

1. Defining the null and alternative hypotheses.
2. Providing the parameter estimate, standard error, degrees of freedom, and significance level.
3. Computing the t-statistic.
4. Calculating the p-value using the Student's t-distribution.
5. Comparing the p-value with the selected significance level.
6. Returning the statistical decision.

## Statistical Decision

For a two-sided hypothesis test:

* Reject the null hypothesis when `p ≤ α`.
* Fail to reject the null hypothesis when `p > α`.

## Output

The implementation returns a structured result containing:

* t-statistic
* p-value
* significance level
* hypothesis test decision

## Assumptions

The analysis assumes independent observations and appropriate conditions for the use of the t-distribution.

Statistical significance should be interpreted alongside practical or economic significance.

## Purpose

This project demonstrates the implementation of **inferential statistics and hypothesis testing in Python**, with an emphasis on clear separation between statistical computation and decision logic.
