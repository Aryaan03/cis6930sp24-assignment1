import unittest
import pytest
import os
import sys
from unittest.mock import patch
import spacy
from google.cloud import language_v1
from censoror import *  # Importing all functions from the censoror module

class TestCensoringFunctions(unittest.TestCase):  # Defining a test class that inherits from unittest.TestCase

    def test_censor(self):  
        # Defining a test method to test the censor function
        tempdata = "I am Philip Paul, today is 05-15-2025 and my phone number is 352-999-9999."  
        # Setting up test data
        Detected = ["Philip", "Paul", "05-15-2025", "352-999-9999"]  
        # Defining detected entities
        out = "I am ██████ ████, today is ██████████ and my phone number is ████████████."  
        # Expected output after censoring
        self.assertEqual(censor(tempdata, Detected), out)  

if __name__ == '__main__':
    unittest.main()   
