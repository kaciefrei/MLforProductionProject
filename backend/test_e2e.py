import unittest
import json
import requests

class TestAppE2E(unittest.TestCase):

    BASE_URL = "http://localhost:5000"

    def test_e2e_predict(self):
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
        response = requests.post(f"{self.BASE_URL}/predict", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("prediction", response.json())

    def test_e2e_invalid_data(self):
        data = {"Temperature": "invalid_data"}  # Données incorrectes
        response = requests.post(f"{self.BASE_URL}/predict", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("error", response.json())

    def test_e2e_home(self):
        response = requests.get(f"{self.BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Algerian Forest Fires Prediction API is running!", response.text)

if __name__ == "__main__":
    unittest.main()
