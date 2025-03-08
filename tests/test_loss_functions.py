import pytest
import sys
import os
import numpy as np

# Add the root project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from machine_learning.loss_functions import kullback_leibler_divergence

def test_kl_divergence_with_zero():
    """This test ensures that KL divergence avoids log(0)."""
    p = np.array([0.2, 0.3, 0.5])
    q = np.array([0.3, 0.3, 0.0])  # `0` in q will cause log(0) error

    with pytest.raises(ValueError):  # Expect an error due to log(0)
        kullback_leibler_divergence(p, q)