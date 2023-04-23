import pytest

from .models import Feedback

@pytest.fixture()
def newFeedback():
    newFeedback = Feedback
    newFeedback.feedback = "My first disliked group!"
    # Still need group_id and user_id
    yield newFeedback

class TestFeedback:
    def test_gID(self, newFeedback):
        # Will need to create a group object then add a Feedback to it to test this
        assert True
        
    def test_uID(self, newFeedback):
        # Will need to create a user object then add a Feedback from them to test this
        assert True
        
    def test_Feedback(self, newFeedback):
        assert newFeedback.feedback == "My first disliked group!"
        
        # Test size constraints
        
        # Test no other variables were changed

