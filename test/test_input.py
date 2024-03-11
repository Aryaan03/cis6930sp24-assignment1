import unittest
import pytest
import re
import os
import sys
import spacy
from google.cloud import language_v1  
from unittest.mock import Mock
from censoror import *

# Defining a test class named TestAnalyzeEntities inheriting from unittest.TestCase
class TestAnalyzeEntities(unittest.TestCase):

    # Defining a test method named test_empty_input
    def test_read(self):
        result, count = analyze_entities('Philip')  # Calling analyze_entities with two strings
        self.assertEqual(result, [])  # Asserting that the result is an empty list

    # Defining a test method named test_no_entities
    def test_input(self):
        info = "orchestrating file processing and censorship operations"
        result, count = analyze_entities(info)  # Calling analyze_entities with text_content
        self.assertEqual(result, [])  # Asserting that the result is an empty list

# If the script is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()