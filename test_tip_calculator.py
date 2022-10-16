import io
from unittest import mock, TestCase

from tip_calculator import tip_calculator

class TestTipCalculator(TestCase):
    # Test Case #01 - "A meal for 1"
    @mock.patch('builtins.input', side_effect=['15', '1', '20'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator_case_1(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual(
            "\nTotal bill: $19.50\n",
            mock_stdout.getvalue()
        )
    # Test Case #02 - "A feast to remember"
    @mock.patch('builtins.input', side_effect=['25000000', '3', '31'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator_case_2(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual(
            "\nTotal bill: $35,250,000.00\nEach person should pay $11,750,000.00\n",
            mock_stdout.getvalue()
        )
    # Test Case # 03 - "No tip"
    @mock.patch('builtins.input', side_effect=['78.99', '6', '0'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator_case_3(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual(
            "\nTotal bill: $86.89\nEach person should pay $14.48\n",
            mock_stdout.getvalue()
        )
    # Test Case # 04 - "Sharing the bill among many"
    @mock.patch('builtins.input', side_effect=['5000', '876', '12'])
    @mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_tip_calculator_case_4(self, mock_stdout, mock_input):
        tip_calculator()

        self.assertEqual(
            "\nTotal bill: $6,100.00\nEach person should pay $6.96\n",
            mock_stdout.getvalue()
        )
