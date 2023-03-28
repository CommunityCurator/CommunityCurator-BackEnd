import pytest

from .models import Event

@pytest.fixture()
def event():
    newEvent = Event
    newEvent.event_name = "Community Curator Developers"
    newEvent.event_description = "Developers who work on the Community Curator prototype"
    newEvent.event_city = "Norfolk"
    newEvent.event_state = "Virginia"
    # Still need date, time, categories, image, event_creator
    yield newEvent

class TestEvent:
    def test_name(self, event):
        assert event.event_name == "Community Curator Developers"
        
        event.event_name = "Back End Developers"
        assert event.event_name != "Community Curator Developers"
        assert event.event_name == "Back End Developers"
        
        assert event.event_description == "Developers who work on the Community Curator prototype"
        assert event.event_city == "Norfolk"
        assert event.event_state == "Virginia"
        
        # Test size constraints

    def test_description(self, event):
        assert event.event_description == "Developers who work on the Community Curator prototype"
        
        event.event_description = "Developers who work on the Community Curator RWP"
        assert event.event_description == "Developers who work on the Community Curator RWP"
        
        assert event.event_name == "Community Curator Developers"
        assert event.event_city == "Norfolk"
        assert event.event_state == "Virginia"
        
        # Test size constraints

    def test_city(self, event):
        assert event.event_city == "Norfolk"
        
        event.event_city = "Chesapeake"
        assert event.event_city == "Chesapeake"
        assert event.event_name == "Community Curator Developers"
        assert event.event_description == "Developers who work on the Community Curator prototype"
        assert event.event_state == "Virginia"
        
        # Test size constraints

    def test_state(self, event):
        assert event.event_state == "Virginia"
        
        event.event_state = "Hawaii"
        assert event.event_state == "Hawaii"
        assert event.event_city == "Norfolk"
        assert event.event_name == "Community Curator Developers"
        assert event.event_description == "Developers who work on the Community Curator prototype"
