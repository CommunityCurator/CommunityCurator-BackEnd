import pytest

from .models import Comment

class TestComment:
    def test_gID(self):
        # Will need to create a group object then add a comment to it to test this
        assert True
        
    def test_uID(self):
        # Will need to create a user object then add a comment from them to test this
        assert True
        
    def test_comment(self):
        newComment = Comment(comment="Great idea! I will attend!")
        assert newComment.comment == "Great idea! I will attend!"
        
        # Test size constraints
        
        # Test no other variables were changed

