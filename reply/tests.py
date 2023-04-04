import pytest

from .models import Reply

@pytest.fixture()
def newReply():
    newReply = Reply
    newReply.reply = "Replying to your comment."
    # Still need comment_id and user_id
    yield newReply

class TestReply:
    def test_cID(self, newReply):
        # Will need to create a comment object then add a reply to it to test this
        assert True
        
    def test_uID(self, newReply):
        # Will need to create a user object then add a reply from them to test this
        assert True
        
    def test_reply(self, newReply):
        assert newReply.reply == "Replying to your comment."
        
        # Test size constraints
        
        # Test no other variables were changed

