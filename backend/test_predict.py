import unittest
import numpy as np
from app import predict

class TestPredictionFunction(unittest.TestCase):
    
    def test_predict_valid_input(self):
        features = [30, 60, 5, 0, 85, 200, 150, 10, 100, 250]  # Exemple de valeurs de caractéristiques
        prediction = predict(features)
        self.assertIsInstance(prediction, np.ndarray)
        self.assertEqual(prediction.shape, (1, 1))
    
    def test_predict_invalid_input(self):
        features = "invalid_input"  # Entrée incorrecte
        with self.assertRaises(ValueError):
            predict(features)
    
    def test_predict_empty_input(self):
        features = []  # Entrée vide
        with self.assertRaises(ValueError):
            predict(features)

if __name__ == "__main__":
    unittest.main()
