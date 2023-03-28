import pytest

from .models import Group

@pytest.fixture()
def group():
    newGroup = Group
    newGroup.group_name = "Community Curator Developers"
    newGroup.description = "Developers who work on the Community Curator prototype"
    newGroup.city = "Norfolk"
    newGroup.state = "Virginia"
    # Still need image, categories, users
    yield newGroup
class TestGroup:
    def test_name(self, group):
        assert group.group_name == "Community Curator Developers"
        
        group.group_name = "Back End Developers"
        assert group.group_name != "Community Curator Developers"
        assert group.group_name == "Back End Developers"

        assert group.description == "Developers who work on the Community Curator prototype"
        assert group.city == "Norfolk"
        assert group.state == "Virginia"
        
        # Test size constraints
        
    def test_description(self, group):
        assert group.description == "Developers who work on the Community Curator prototype"
        
        group.description = "Developers who work on the Community Curator RWP"
        assert group.description == "Developers who work on the Community Curator RWP"
        
        assert group.group_name == "Community Curator Developers"
        assert group.city == "Norfolk"
        assert group.state == "Virginia"
        
        # Test size constraints
        
    def test_city(self, group):
        assert group.city == "Norfolk"
        
        group.city = "Chesapeake"
        assert group.city == "Chesapeake"
        assert group.group_name == "Community Curator Developers"
        assert group.description == "Developers who work on the Community Curator prototype"
        assert group.state == "Virginia"

        # Test size constraints
        
    def test_state(self, group):
        assert group.state == "Virginia"
        
        group.state = "Hawaii"
        assert group.state == "Hawaii"
        assert group.city == "Norfolk"
        assert group.group_name == "Community Curator Developers"
        assert group.description == "Developers who work on the Community Curator prototype"
