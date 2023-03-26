import pytest

from .models import Category

# Create your tests here.
class TestCategory:
    def test_name(self):
        # Initial Test
        newCategory = Category
        newCategory.name = "Computer Science Majors"
        assert newCategory.name == "Computer Science Majors"
        
        # Test character limit
        
        # Test already availble