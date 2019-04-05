"""
Tests for molssi_math module
"""
import pytest
import molssi_devops_uf as md_uf

@pytest.mark.parametrize("num_list, expected_mean", [
    ([1, 2, 3, 4, 5], 3),
    ([0, 2, 4, 6], 3),
    ([1, 2, 3, 4], 2.5)
])

def test_many(num_list, expected_mean):
    assert md_uf.mean(num_list) == expected_mean

def test_mean():
    num_list = [1, 2, 3, 4, 5]
    observed = md_uf.mean(num_list)
    expected = 3
    assert observed == expected

def test_mean_wrong_type():
    test_input = 'This is not a list'

    with pytest.raises(TypeError):
        md_uf.mean(test_input)
