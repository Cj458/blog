from rest_framework.test import APIClient

class TestCreatePost:

    def test_if_user_is_anonymous_returns_401(self):


        
        client = APIClient()
        response = client.post('/api/posts/', {})   