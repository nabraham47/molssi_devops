"""
Unit and regression test for the title_case module.
"""

# Import package, test suite, and other packages as needed
import molssi_devops
import pytest
import sys

def test_title_case():
    """Test the title_case calculates what we expect."""
    test_string =  "THiS iS a STRing tO be ConVERTED"
    expected = "This Is A String To Be Converted "
    calculated = molssi_devops.title_case(test_string)
    assert expected == calculated

def test_mean_type_error():
    test_variable = ['this', 'is', 'not', 'a', 'string']

    with pytest.raises(TypeError):
        molssi_devops.title_case(test_variable)


