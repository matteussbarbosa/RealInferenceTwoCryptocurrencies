"""
Determines whether the null hypothesis should be rejected using a t-test.
"""

import numpy as np
from scipy.stats import t


def reject_null_hipotesys_t_test(
        parameter,
        alpha,
        degrees_of_freedom,
        standard_error
):
    
    # Calculates the p-value.
    t_stats = (parameter - 0) / (standard_error)
    p_value = 2 * (1 - t.cdf(abs(t_stats), degrees_of_freedom))
    
def reject_null_hypothesis_t_test(
        parameter: float,
        null_hypothesis_value: float,
        degrees_of_freedom: int,
        standard_error: float,
        alpha: float = 0.05
) -> bool:
    """
    Determine whether the null hypothesis should be rejected.

    Parameters
    ----------
    parameter : float
        Estimated parameter value to be evaluated.
    null_hypothesis_value : float
        Number of the null hypothesis.
    degrees_of_freedom : int
        Number of degrees of freedom.
    standard_error: float
        The value of the standard error.
    alpha : float
        The significance level of the test. Default is 0.05.

    Returns
    -------
    bool
       True, if the null hypothesis should be rejected; false otherwise.
    """
    # Validate the parameters: 
    if degrees_of_freedom <= 0:
        raise ValueError('degrees_of_freedom must be positive')
    if standard_error <= 0:
        raise ValueError('standard_error must be positive')
    if not 0 < alpha < 1:
        raise ValueError('alpha must be between 0 and 1.')

    # Calculates the p-value for two-tail t-test.
    t_statistic = (parameter - null_hyt_statspothesis_value) / (standard_error)
    p_value = 2 * (1 - t.cdf(abs(t_statistic), degrees_of_freedom))
        
    return p_value <= alpha

