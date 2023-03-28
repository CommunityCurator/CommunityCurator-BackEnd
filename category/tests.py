import pytest

from .models import Category

@pytest.fixture()
def category():
    newCategory = Category
    newCategory.name = "Computer Science Majors"
    # Still need to add groups
    yield newCategory

class TestCategory:
    def test_name(self, category):
        # Initial Test
        assert category.name == "Computer Science Majors"
        
        # Test character limit
        
        # Test if already availble
        
    def test_createdAt(self):
        # Could use seed data for test as DateField is only used when .save() is called

        assert True
        
    def test_groups(self):
        # Could use seed data for this one as well
        assert True