"""Test the five required emotion classifications."""
import unittest

from EmotionDetection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    """Check the dominant emotion for each required statement."""

    def test_joy(self):
        """Identify joy."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

    def test_anger(self):
        """Identify anger."""
        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

    def test_disgust(self):
        """Identify disgust."""
        result = emotion_detector(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(result["dominant_emotion"], "disgust")

    def test_sadness(self):
        """Identify sadness."""
        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

    def test_fear(self):
        """Identify fear."""
        result = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result["dominant_emotion"], "fear")
if __name__ == "__main__":
    unittest.main(verbosity=2)