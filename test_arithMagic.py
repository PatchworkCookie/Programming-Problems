'''
Tests for arithMagic.py
'''
import pytest, arithMagic

@pytest.mark.skip(reason="Not ready")
@pytest.mark.parametrize('input1, input2, exOutput',[([1,2,3],6, ['1+2+3']), ([1,2,3,4,5,6,7,8,9], 100, ['1+2+34–5+67–8+9'])])
def test_magicSum(input1, input2, exOutput):
	result = arithMagic.magicSum(input1, input2)
	assert exOutput in result
	
@pytest.mark.parametrize('input1, input2, exOutput',[([1,2,3],('_','+'), '12+3'), ([1,2,3,4,5,6,7,8,9], ('+','+','_','-','+','_','-','+'),'1+2+34-5+67-8+9')])
def test_implementOperators(input1, input2, exOutput):
	result = arithMagic.implementOperators(input1, input2)
	assert exOutput == result