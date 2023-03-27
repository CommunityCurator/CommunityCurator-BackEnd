import pytest

from .models import Comment

@pytest.fixture()
def newComment():
    newComment = Comment
    newComment.comment = "Great idea! I will attend!"
    # Still need group_id and user_id
    yield newComment

class TestComment:
    def test_gID(self, newComment):
        # Will need to create a group object then add a comment to it to test this
        assert True
        
    def test_uID(self, newComment):
        # Will need to create a user object then add a comment from them to test this
        assert True
        
    def test_comment(self, newComment):
        assert newComment.comment == "Great idea! I will attend!"
        
        # Test size constraints
        
        # Test no other variables were changed

