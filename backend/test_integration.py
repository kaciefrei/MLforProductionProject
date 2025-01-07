import unittest
import json
from app import app

class TestAppIntegration(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()

    def test_predict_route_valid(self):
        data = {
            "Temperature": 30,
            "RH": 60,
            "Ws": 5,
            "Rain": 0,
            "FFMC": 85,
            "DMC": 200,
            "DC": 150,
            "ISI": 10,
            "BUI": 100,
            "FWI": 250
        }
        response = self.client.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('prediction', json.loads(response.data))
    
    def test_predict_route_invalid_data(self):
        data = {"Temperature": "invalid_data"}  # Données invalides
        response = self.client.post('/predict', json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('error', json.loads(response.data))

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn("Algerian Forest Fires Prediction API is running!", response.data.decode())

if __name__ == "__main__":
    unittest.main()
