import unittest
from Histogram import Histogram
from unittest.mock import patch
import io


class TestHistogram(unittest.TestCase):
    def setUp(self):
        self.histogram = Histogram()

    def test_add(self):
        # Test adding values to the histogram
        self.histogram.add(3)
        self.histogram.add(3)
        self.histogram.add(2)
        self.assertEqual(
            self.histogram.data,
            {3: 2, 2: 1},
            "Histogram data should correctly count occurrences",
        )

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_display(self, mock_stdout):
        # Test the display method of the histogram, ensuring it outputs correctly formatted results
        self.histogram.add(3)
        self.histogram.add(3)
        self.histogram.add(2)
        self.histogram.display()
        self.assertEqual(
            mock_stdout.getvalue(),
            "2: *\n3: **\n",
            "Display output should correctly represent histogram data",
        )


if __name__ == "__main__":
    unittest.main()
