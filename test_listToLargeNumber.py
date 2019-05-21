'''
Tests for listToLargeNumber.py
'''
import pytest, listToLargeNumber

@pytest.mark.skip()
@pytest.mark.parametrize('input, exOutput',[([1,2],21), ([49,7,3,6],76493)])
def test_(input, exOutput):
	result = 0
	assert result == exOutput

@pytest.mark.parametrize('input, exOutput',[([1,2],[2,1]), ([5,49,7,3,6],[7,6,5,49,3]),
([234,342,123,534,6455,123], [6455,534,342,234,123,123])])
def test_sortBySignificance(input, exOutput):
	result = listToLargeNumber.sortBySignificance(input)
	assert result == exOutput
	
@pytest.mark.parametrize('input',[[1,-2], [49,7,-3,6]])
def test_sortBySignificance_ValueError(input):
	with pytest.raises(ValueError):
		listToLargeNumber.sortBySignificance(input)
		
@pytest.mark.parametrize('input1, input2, exOutput',
[(21121,21111,1), 
(3,9,-1),
(124,124,0)])
def test_testBiggerSum(input1, input2, exOutput):
	result = listToLargeNumber.testBiggerSum(input1, input2)
	assert result == exOutput