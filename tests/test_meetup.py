import unittest
from calendar_aggregator.meetup.meetup import readPage
import os

def read_example_html():
    # Get the directory of the current file
    current_dir = os.path.dirname(__file__)
    
    # Define the path to the example HTML file
    example_html_path = os.path.join(current_dir, 'test_data', 'example.html')
    
    # Read the content of the example HTML file
    with open(example_html_path, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    return html_content

class TestMainModule(unittest.TestCase):
    def test_main(self):
        html_content = read_example_html()
        # Perform your test using the html_content
        assert "<html" in html_content
        results = readPage(html_content)
        # print(results)
        self.assertEqual(len(results), 15)
        self.assertEqual(results[0]['date'], '2024-05-20 17:30:00')
        self.assertEqual(results[0]['title'], 'Orlandopreneur Monthly Happy Hour')
        self.assertEqual(results[0]['location'], 'Citrus Club, Orlando, FL')

        # You could redirect stdout to capture print output, or test other logic
        pass

if __name__ == "__main__":
    unittest.main()