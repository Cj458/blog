from rest_framework.test import APIClient
from rest_framework import status

import pytest

class TestCreatePost:

    def test_if_user_is_anonymous_returns_401(self):


        'http://127.0.0.1:8000/api/myusers/'
        # client = APIClient()
        # response = client.post('/api/myusers/', {})   
        pass


@pytest.mark.django_db
class TestRetrieveUsers:
    def retrieve_users(self):
        'http://127.0.0.1:8000/api/myusers/'

        client = APIClient()
        response = client.get('/api/myusers/')

        assert response.status_code == status.HTTP_200_OK

    def retrieve_a_user_posts(self, user_id):
        'http://127.0.0.1:8000/api/myusers/'

        client = APIClient()
        response = client.get(f'/api/myusers/{user_id}/posts/')

        assert response.status_code == status.HTTP_200_OK
      