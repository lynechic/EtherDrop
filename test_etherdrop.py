# test_etherdrop.py
"""
Tests for EtherDrop module.
"""

import unittest
from etherdrop import EtherDrop

class TestEtherDrop(unittest.TestCase):
    """Test cases for EtherDrop class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = EtherDrop()
        self.assertIsInstance(instance, EtherDrop)
        
    def test_run_method(self):
        """Test the run method."""
        instance = EtherDrop()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
