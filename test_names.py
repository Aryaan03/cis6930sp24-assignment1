import unittest
import pytest
import os
import sys
from unittest.mock import patch
import spacy
from google.cloud import language_v1
from censoror import *  # Importing all functions from the censoror module

class TestCensoringFunctions(unittest.TestCase):  # Defining a test class that inherits from unittest.TestCase

    @patch("censoror.spacy.load")  
    # Patching spacy for mocking in the test
    def test_CenName(self, mock_Model):  
        # Defining a test method to test the function for censoring names
        mock_Mod = mock_Model.return_value  
        mock_Input = mock_Mod.return_value  
        # Creating a mock input object
        mock_Input.ents = [MockEntity(text=["Philip Paul", "Lee Odonnel", "Logan Paul", "Jake Paul"], label_="PERSON")]  
        # Mocking entities detected by Spacy
        tempdata = "I am Philip Paul and here are my friends Lee Odonnel, Logan Paul and Jake Paul."  
        # Setting up test data
        out = ["Philip Paul", "Lee Odonnel", "Logan Paul", "Jake Paul"]  
        # Expected output after detecting names
        self.assertEqual(CenName(tempdata), out)  

class MockEntity:   
    # Defining a mock class to simulate entities detected by Spacy 
    def __init__(self, text, label_):
        self.text = text   
        # Storing text of detected entity
        self.label_ = label_   
        # Storing label of detected entity

if __name__ == '__main__':
    unittest.main()   
