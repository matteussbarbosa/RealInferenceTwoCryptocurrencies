"""
This module provides hipotesys testing analysis for a paremeter.

This module does uses third-party modules.
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
    