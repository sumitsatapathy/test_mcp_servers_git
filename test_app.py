import unittest
import json
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_home_endpoint(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'ok')
        self.assertIn('flaskapptest', data['message'])

    def test_read_endpoint_default(self):
        response = self.app.get('/read')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello World')
        self.assertEqual(data['branch'], 'flaskapptest')

    def test_read_endpoint_with_name(self):
        response = self.app.get('/read?name=TestUser')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello TestUser')
        self.assertEqual(data['branch'], 'flaskapptest')

if __name__ == '__main__':
    unittest.main()
