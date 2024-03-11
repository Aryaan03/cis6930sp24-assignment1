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

    def test_censor(self):
        data = "We are travelling to India on 05-15-2025 for holidays"
        result, count = analyze_entities(data)  # Calling analyze_entities with text_content
        verify = ['05-15-2025']  # Expected entities list
        self.assertEqual(result, verify)  # Asserting that the result matches the expected entities

# If the script is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()