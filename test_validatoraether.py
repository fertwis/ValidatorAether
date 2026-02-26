# test_validatoraether.py
"""
Tests for ValidatorAether module.
"""

import unittest
from validatoraether import ValidatorAether

class TestValidatorAether(unittest.TestCase):
    """Test cases for ValidatorAether class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ValidatorAether()
        self.assertIsInstance(instance, ValidatorAether)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ValidatorAether()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
