"""
Unit and regression test for the molssi_math module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys
import numpy as np

def test_mean():
    """Test that mean function calculates what we expect."""
    test_list = [1, 2, 3, 4, 5]
    expected = 3
    calculated =  molssi_devops.mean(test_list)
    assert expected == calculated

import pytest
import numpy as np

@pytest.mark.parametrize("num_list, expected_mean" , [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5),
    (list(range(1, 1000000)), 1000000/2.0)
])

def test_many(num_list, expected_mean):
    # assert mean(num_list) == expected_mean
    assert np.isclose(molssi_devops.mean(num_list), expected_mean, 1e-6)



