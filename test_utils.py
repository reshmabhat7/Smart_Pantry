# test_utils.py
import unittest
from utils import clean_ingredient_string  # adjust 'utils' to your actual filename if different

class TestUtils(unittest.TestCase):
    def test_clean_ingredient_string(self):
        raw = "Salt, Pepper , Garlic!!"
        cleaned = clean_ingredient_string(raw)
        self.assertEqual(cleaned, ['salt', 'pepper', 'garlic'])

if __name__ == '__main__':
    unittest.main()
