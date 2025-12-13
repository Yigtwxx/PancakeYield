# test_pancakeyield.py
"""
Tests for PancakeYield module.
"""

import unittest
from pancakeyield import PancakeYield

class TestPancakeYield(unittest.TestCase):
    """Test cases for PancakeYield class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PancakeYield()
        self.assertIsInstance(instance, PancakeYield)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PancakeYield()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
