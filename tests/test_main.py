import unittest
from calendar_aggregator.main import main

class TestMainModule(unittest.TestCase):
    def test_main(self):
        main()
        # You could redirect stdout to capture print output, or test other logic
        pass

if __name__ == "__main__":
    unittest.main()