import unittest
from score_calculator import calculate_average_score

class TestScoreCalculator(unittest.TestCase):
    def test_average_score(self):
        feedback = [
            {"score": 3},
            {"score": 5},
            {"score": 4}
        ]
        avg = calculate_average_score(feedback)
        self.assertEqual(avg, 4)

if __name__ == "__main__":
    unittest.main()

