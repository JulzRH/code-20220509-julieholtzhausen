import unittest
from bmi_calculator import bmi, bmiCategory

class TestBmiCalculator(unittest.TestCase):
    #Tests for bmi method
    def test_bmi(self):
        self.assertEqual(bmi(67.5, 150), 30)
    
    def test_bmi_fails_for_invalid_weight(self):
        self.assertEqual(bmi('INVALID_WEIGHT', 165), 'Undefined')
        
    def test_bmi_fails_for_invalid_height(self):
        self.assertEqual(bmi(67.5, 'INVALID_WEIGHT'), 'Undefined')
    
    #Tests for bmiCategory method
    def test_bmiCategory(self):
        self.assertEqual(bmiCategory(30), ('Moderately obese', 'Medium risk'))
        # Could add a data provider to check all possible outputs of bmiCategory method, but seems out of scope
        
    def test_bmiCategory_fails_for_invalid_bmi(self):
        self.assertEqual(bmiCategory('INVALID_BMI'), ('Undefined', 'Undefined'))
        