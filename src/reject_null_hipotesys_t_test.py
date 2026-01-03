"""
This module provides hipotesys testing analysis for a paremeter.

This module does uses third-party modules.
"""

from scipy.stats import t


def reject_null_hipotesys_t_test(
        parameter,
        alpha,
        degrees_of_freedom,
        standard_error
) -> dict:
    
    # Calculates the p-value.
    t_stats = (parameter - 0) / (standard_error)
    p_value = 2 * (1 - t.cdf(abs(t_stats), degrees_of_freedom))
    
    # Compares the value of p-value with alpha.
    if p_value <= alpha:
        test_result = {
            "reject_null_hypotesis": True
            }
    else:
        test_result = {
            "reject_null_hypotesis": False
            }
    return test_result