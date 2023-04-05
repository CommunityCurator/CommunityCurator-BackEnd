import pytest

from .models import Comment

@pytest.fixture()
def newComment():
    newComment = Comment
    newComment.comment = "Commenting on a post."
    # Still need post_id and user_id
    yield newComment

class TestComment:
    def test_pID(self, newComment):
        # Will need to create a post object then add a comment to it to test this
        assert True
        
    def test_uID(self, newComment):
        # Will need to create a user object then add a comment from them to test this
        assert True
        
    def test_comment(self, newComment):
        assert newComment.comment == "Commenting on a post."
        
        # Test size constraints
        
        # Test no other variables were changed

