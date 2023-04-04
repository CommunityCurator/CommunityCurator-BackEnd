import pytest

from .models import Post

@pytest.fixture()
def newPost():
    newPost = Post
    newPost.post = "My first post!"
    # Still need group_id and user_id
    yield newPost

class TestPost:
    def test_gID(self, newPost):
        # Will need to create a group object then add a comment to it to test this
        assert True
        
    def test_uID(self, newPost):
        # Will need to create a user object then add a post from them to test this
        assert True
        
    def test_post(self, newPost):
        assert newPost.post == "My first post!"
        
        # Test size constraints
        
        # Test no other variables were changed

