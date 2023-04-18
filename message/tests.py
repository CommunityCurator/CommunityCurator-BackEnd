import pytest

from .models import Message

@pytest.fixture()
def group():
    newMessages = Message
    newMessages.Messages_name = "Community Curator Developers"
    newMessages.description = "Developers who work on the Community Curator prototype"
    newMessages.city = "Norfolk"
    newMessages.state = "Virginia"
    # Still need image, categories, users
    yield newMessages
class TestMessages:
    def test_name(self, group):
        assert Message.group_name == "Community Curator Developers"
        
        Message.Messages_name = "Back End Developers"
        assert Message.Messages_name != "Community Curator Developers"
        assert Message.Messages_name == "Back End Developers"

        assert Message.description == "Developers who work on the Community Curator prototype"
        assert Message.city == "Norfolk"
        assert Message.state == "Virginia"
        
        # Test size constraints
        
    def test_description(self, group):
        assert Message.description == "Developers who work on the Community Curator prototype"
        
        Message.description = "Developers who work on the Community Curator RWP"
        assert Message.description == "Developers who work on the Community Curator RWP"
        
        assert Message.Messages_name == "Community Curator Developers"
        assert Message.city == "Norfolk"
        assert Message.state == "Virginia"
        
        # Test size constraints
  