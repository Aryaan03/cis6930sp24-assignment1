import unittest
from unittest.mock import patch, MagicMock
import sys
import os
from censoror import parg, case, censor, analyze_entities, CenP, Read, main

# class TestCensoringFunctions(unittest.TestCase):

#     def test_case_function(self):
#         # Test the case function with a sample input
#         input_list = ['1234', '5678', 'abcd']
#         expected_output = ['abcd']
#         self.assertEqual(case(input_list), expected_output)

#     def test_censor_function(self):
#         # Test the censor function with a sample input and type
#         input_info = "My phone number is 1234567890"
#         input_type = ['1234567890']
#         expected_output = "My phone number is ██████████"
#         self.assertEqual(censor(input_info, input_type), expected_output)

#     @patch('your_script_name.Model')
#     @patch('your_script_name.language_v1.LanguageServiceClient')
#     def test_analyze_entities_function(self, mock_Model, mock_language_client):
#         # Mocking external dependencies for analyze_entities function
#         mock_Model.return_value.ents = [MagicMock(text="John Doe", label_="PERSON")]
        
#         mock_response = MagicMock()
#         mock_response.entities = [
#             MagicMock(name="1234567890", type_=3),  # PHONE_NUMBER type
#             MagicMock(name="123 Main St", type_=5),  # ADDRESS type
#             MagicMock(name="2023-12-31", type_=6)  # DATE type
#         ]
        
#         mock_language_client.from_service_account_json.return_value.analyze_entities.return_value = mock_response

#         MailData = "John Doe's phone number is 1234567890 and he lives at 123 Main St."
#         entities, stats = analyze_entities(MailData)
        
#         self.assertEqual(entities, ['John Doe'])
#         self.assertEqual(stats, [1, 1, 1, 1])

#     def test_CenP_function(self):
#         # Test the CenP function with a sample data
#         data = "John Doe's phone number is 1234567890 and he lives at 123 Main St."
#         censored_data = CenP(data)
        
#         # Add your assertions here based on the expected output after censoring

#     @patch('builtins.open', unittest.mock.mock_open(read_data='Sample file content'))
#     @patch('os.makedirs')
#     def test_Read_function(self, mock_makedirs):
#         # Test the Read function with mocked file reading and writing
#         Xtemp = ['sample_file.txt']
#         CCd = 'output_directory'
        
#         Read(Xtemp, CCd)
        
#         # Add your assertions here to check if the file reading and writing operations were successful

# if __name__ == '__main__':
#     unittest.main()

class TestCensoring(unittest.TestCase):

    @patch('censoror.language_v1.LanguageServiceClient')
    def test_analyze_entities(self, mock_language_client):
        # Mock the language service client
        mock_client = MagicMock()
        mock_language_client.from_service_account_json.return_value = mock_client

        # Mock the analyze_entities response
        response_mock = MagicMock()
        response_mock.entities = [
            MagicMock(type_="DATE"),
            MagicMock(type_="PHONE_NUMBER"),
            MagicMock(type_="ADDRESS")
        ]
        mock_client.analyze_entities.return_value = response_mock

        # Define some sample MailData
        mail_data = "John Doe's phone number is 1234567890 and his address is 123 Main St."

        # Call the analyze_entities function
        entities, stats = analyze_entities(mail_data)

        # Check if the function returns the correct entities and stats
        self.assertEqual(entities, ['1234567890', '123 Main St.', 'John Doe'])
        self.assertEqual(stats, [1, 1, 1, 1])  # Dates, Phone Numbers, Locations, Persons

    def test_censor(self):
        # Define some sample data and entities
        data = "John Doe's phone number is 1234567890 and his address is 123 Main St."
        entities = ['1234567890', '123 Main St.', 'John Doe']

        # Call the censor function
        censored_data = censor(data, entities)

        # Check if the function censors the data correctly
        self.assertEqual(censored_data, "████████'s phone number is ██████████ and his address is ███████████.")

    @patch('censoror.os.makedirs')
    @patch('censoror.open')
    def test_read(self, mock_open, mock_makedirs):
        # Define some sample arguments
        file_list = ['text1.txt', 'test2.txt']
        output_dir = 'output/'

        # Mock the behavior of open and os.makedirs
        mock_open.side_effect = [
            MagicMock(spec=open, **{'__ne__.return_value.read.return_value': 'Some text'}),
            MagicMock(spec=open, **{'__ne__.return_value.read.return_value': 'Some more text'})
        ]

        # Call the Read function
        Read(file_list, output_dir)

        # Check if the necessary mocks were called with the correct arguments
        mock_makedirs.assert_called_once_with(output_dir, exist_ok=True)
        mock_open.assert_any_call('file1.txt', 'r', encoding='utf-8')
        mock_open.assert_any_call('file2.txt', 'r', encoding='utf-8')

if __name__ == '__main__':
    unittest.main()
