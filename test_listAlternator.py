'''
Tests for listAlternator.py
'''
import pytest, listAlternator

@pytest.mark.parametrize('input1, input2, exOutput', 
[([1,2,3,4],['a','b','c','d'],[1,'a',2,'b',3,'c',4,'d']),
(['s','m','t','i','g','s','o','k'],['o','e','h','n',' ','p','o','y'],['s','o','m','e','t','h','i','n','g',' ','s','p','o','o','k','y']),
(['t','e','s','t','i','n','g'],['1','2','3'],['t','1','e','2','s','3','t','i','n','g']),
(['4','5','6'],['t','h','i','n','g','s'],['4','t','5','h','6','i','n','g','s'])])
def test_alternateLists(input1, input2, exOutput):
	result = listAlternator.alternateLists(input1, input2)
	assert result == exOutput
	






