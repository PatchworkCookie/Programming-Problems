'''
Tests for listSums.py
'''
import pytest, listSums

class Test_summing():
	
	@pytest.mark.parametrize('input, exOutput', [([1,2,3,4],10),([-2, 3],1),([35,-20,],15)])
	def test_sumViaFor(self, input, exOutput):
		result = listSums.sumViaFor(input)
		assert result == exOutput
	
	@pytest.mark.parametrize('input, exOutput', [([1,2,3,4],10),([-2, 3],1),([35,-20,],15)])
	def test_sumViaWhile(self, input, exOutput):
		result = listSums.sumViaWhile(input)
		assert result == exOutput
		pass
		
	@pytest.mark.parametrize('input, exOutput', [([1,2,3,4],10),([-2, 3],1),([35,-20,],15)])
	def test_sumViaRecursion(self, input, exOutput):
		result = listSums.sumViaRecursion(input)
		assert result == exOutput
		pass
	
	pass