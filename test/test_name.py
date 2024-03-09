import unittest
from unittest.mock import patch, mock_open
from censoror import *

class TestCensor(unittest.TestCase):

    @patch('censoror.spacy.load')
    def test_CenName(self, mock_spacy_load):
        mock_spacy_load.return_value = mock_spacy_load
        mock_spacy_load.ents = [{'label_': 'PERSON', 'text': 'John Doe'}]
        data = "John Doe is a person."
        self.assertEqual(CenName(data), "████████ is a person.")

    @patch('censoror.spacy.load')
    def test_CenDate(self, mock_spacy_load):
        mock_spacy_load.return_value = mock_spacy_load
        mock_spacy_load.ents = [{'label_': 'DATE', 'text': '2022-01-01'}]
        data = "The event happened on 2022-01-01."
        self.assertEqual(CenDate(data), "The event happened on ██████████.")

    # def test_CenNum(self):
    #     data = "Phone number: +1234567890"
    #     self.assertEqual(CenNum(data), "Phone number: ██████████")

    @patch('censoror.spacy.load')
    def test_CenLoc(self, mock_spacy_load):
        mock_spacy_load.return_value = mock_spacy_load
        mock_spacy_load.ents = [{'label_': 'GPE', 'text': 'New York'}]
        data = "He lives in New York."
        self.assertEqual(CenLoc(data), "He lives in ████████.")

    # def test_CenInf(self):
    #     data = "John Doe was born on 2022-01-01. Phone: +1234567890. He lives in New York."
    #     temp = {'names': True, 'dates': True, 'phones': True, 'addresses': True}
    #     censored_data, statistics = CenInf(data, temp)
    #     self.assertEqual(censored_data, "████████ was born on ██████████. Phone: ███████████. He lives in ███ ████.")
    #     self.assertEqual(statistics, {'names': 1, 'dates': 1, 'phones': 1, 'addresses': 1})

    # @patch('builtins.open', new_callable=mock_open, read_data="John Doe is a person.")
    # def test_Input(self, mock_open):
    #     data, stats = Input('test_file.txt', {'names': True, 'dates': False, 'phones': False, 'addresses': False})
    #     self.assertEqual(data, "████████ is a person.")
    #     self.assertEqual(stats, {'names': 1, 'dates': 0, 'phones': 0, 'addresses': 0})

    @patch('builtins.open', new_callable=mock_open)
    @patch('censoror.os.path.basename')
    @patch('censoror.os.path.join')
    def test_Output(self, mock_join, mock_basename, mock_open):
        mock_basename.return_value = "test_file.txt"
        Output("test_file.txt", "John Doe is a person.", "output_dir")
        mock_join.assert_called_once_with("output_dir", "test_file.txt.censored")
        handle = mock_open()
        handle.write.assert_called_once_with("John Doe is a person.")

    @patch('censoror.argparse.ArgumentParser.parse_args')
    def test_parg(self, mock_parse_args):
        mock_parse_args.return_value = argparse.Namespace(input=['test_file.txt'], names=True, dates=True, phones=True, addresses=True, output='output_dir', stats='stderr')
        args = parg()
        self.assertEqual(args.input, ['test_file.txt'])
        self.assertTrue(args.names)
        self.assertTrue(args.dates)
        self.assertTrue(args.phones)
        self.assertTrue(args.addresses)
        self.assertEqual(args.output, 'output_dir')
        self.assertEqual(args.stats, 'stderr')

if __name__ == '__main__':
    unittest.main()
