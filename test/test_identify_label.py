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

    # Defining a test method named test_analyze_entities_name
    def test_group(self):
        mock_model = Mock()  # Creating a mock object using the Mock class

        # Creating mock objects representing entities with text and label
        mock_d1 = Mock(text="Philip Paul", label_="PERSON")
        mock_d2 = Mock(text="Lee Odonnel", label_="PERSON")
        mock_d3 = Mock(text="Logan Paul", label_="PERSON")
        mock_d4 = Mock(text="Jake Paul", label_="PERSON")
        mock_d = [mock_d1, mock_d2, mock_d3, mock_d4]  # Creating a list of mock entities

        mock_model.return_value.ents = mock_d  # Setting the entities attribute of mock_model

        data = "I am Philip Paul and here are my friends Lee Odonnel, Logan Paul and Jake Paul."
        outcome = ['Philip Paul', 'Lee Odonnel', 'Logan Paul', 'Jake Paul']  # Expected outcome list
        
        # Calling the analyze_entities function with the data
        result, count = analyze_entities(data)

        # Asserting that the result matches the expected outcome
        self.assertListEqual(result, outcome)

# If the script is executed directly, run the tests
if __name__ == '__main__':
    unittest.main()  
