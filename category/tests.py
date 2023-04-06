import pytest
from django.test import Client

from django.forms.models import model_to_dict
from datetime import datetime
import json

from .models import Category

@pytest.fixture()
def category():
    newCategory = Category
    newCategory.name = "Fishing"
    newCategory.created_at = datetime.today().strftime('%Y-%m-%d')
    yield newCategory
    
@pytest.fixture()
def client():
    client = Client()
    yield client

@pytest.mark.django_db
class TestCategory:
    def test_name(self, category, client):
        # Initial Test
        assert category.name == "Fishing"
        assert category.created_at == datetime.today().strftime('%Y-%m-%d')
                
        # Test views
        jsonObj = model_to_dict(category)
        response = client.post('/api/categories/', jsonObj)
        assert response.status_code == 201
        
        response = client.get('/api/categories/')
        assert response.status_code == 200
        data = response.json()
        
        for cat in data['categories']:
            if(cat['name'] == "Fishing"):
                assert True
                return
        assert False
        
    def test_createdAt(self):
        # Could use seed data for test as DateField is only used when .save() is called

        assert True
