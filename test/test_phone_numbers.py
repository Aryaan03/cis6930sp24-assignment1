import unittest
import pytest
import os
import sys
from unittest.mock import patch
import spacy
from google.cloud import language_v1
from censoror import *  
# Importing all functions from the censoror module

class TestCensoringFunctions(unittest.TestCase):  
    # Defining a test class that inherits from unittest.TestCase

    @patch("censoror.language_v1.LanguageServiceClient.from_service_account_json")   
    # Patching the LanguageServiceClient for mocking in the test
    def test_CenNum(self, mock_GoogleMod):   
        # Defining a test method to test the function for censoring phone numbers 
        mock_GoogleMod.return_value.analyze_entities.return_value = MockResponse(entity_type='PHONE_NUMBER', entity_text=["352-999-9999", "5555566666"])   
        # Mocking response from Google Cloud NLP API
        tempdata = "I have two numbers, one is 352-999-9999 and second is 5555566666"   
        # Setting up test data
        out = ["352-999-9999", "5555566666"]   
        # Expected output after detecting phone numbers
        self.assertEqual(CenNum(tempdata), out)

class MockResponse:   
    # Defining a mock class to simulate responses from Google Cloud NLP API or similar services 
    def __init__(self, entity_type, entity_text):
        self.entities = [MockGoogleEntity(name=text, type_=entity_type) for text in entity_text]   
        # Creating entities based on provided text and type

class MockGoogleEntity:   
    # Defining a mock class to simulate entities returned by Google Cloud NLP API or similar services 
    def __init__(self, name, type_):
        self.name = name   
        # Storing name of entity 
        self.type_ = {   
            # Mapping entity types to corresponding values from language_v1.Entity.Type enum 
            'PHONE_NUMBER': language_v1.Entity.Type.PHONE_NUMBER,
        }.get(type_, language_v1.Entity.Type.PHONE_NUMBER)

if __name__ == '__main__':
    unittest.main()   
