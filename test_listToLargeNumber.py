'''
Tests for listToLargeNumber.py
'''
import pytest, listToLargeNumber

@pytest.mark.skip()
@pytest.mark.parametrize('input, exOutput',[([1,2],21), ([49,7,3,6],76493)])
def test_(input, exOutput):
	result = 0
	assert result == exOutput

@pytest.mark.parametrize('input, exOutput',[([1,2],[2,1]), ([5,49,7,3,6],[7,6,5,49,3])])
def test_sortBySignificance(input, exOutput):
	result = listToLargeNumber.sortBySignificance(input)
	assert result == exOutput
	
@pytest.mark.parametrize('input',[[1,-2], [49,7,-3,6]])
def test_sortBySignificance_ValueError(input):
	with pytest.raises(ValueError):
		listToLargeNumber.sortBySignificance(input)