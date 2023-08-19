import unittest

from src.FunctionalProcessing import *


class FunctionalProcessingTests(unittest.TestCase):

    def setUp(self):

        self.data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
        self.expected_data_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Unknown"]


    # ------------------------------------------------------------------------------
    # Case block
    # ------------------------------------------------------------------------------


    def test_case_management_conventional_approach(self):
        def map_fcn(item):
            if item == 0:
                return "Zero"
            elif item == 1:
                return "One"
            elif item == 2:
                return "Two"
            elif item == 3:
                return "Three"
            elif item == 4:
                return "Four"
            elif item == 5:
                return "Five"
            elif item == 6:
                return "Six"
            elif item == 7:
                return "Seven"
            elif item == 8:
                return "Eight"
            elif item == 9:
                return "Nine"
            elif item == 10:
                return "Ten"
            else:
                return "Unknown"
        out = list(map(map_fcn, self.data_list))
        self.assertListEqual(out, self.expected_data_list)

    def test_case_nominal_usage_list(self):

        # Set up the switch
        data_pipe = switch()

        # Assign a value through a function
        case(data_pipe, 1, lambda x: "One")

        # Assign values directly
        case(data_pipe, 2, "Two")
        case(data_pipe, 3, "Three")
        case(data_pipe, 4, "Four")
        case(data_pipe, 5, "Five")
        case(data_pipe, 6, "Six")
        case(data_pipe, 7, "Seven")
        case(data_pipe, 8, "Eight")
        case(data_pipe, 9, "Nine")
        case(data_pipe, 10, "Ten")

        # Assign a default value
        case_default(data_pipe, "Unknown")

        # Apply the switch to capture data
        out_pipe = apply_switch(data_pipe, self.data_list)
        out = list(out_pipe)
        self.assertListEqual(out, self.expected_data_list)

    def test_case_nominal_usage_dict(self):



    def test_case_repeatedly_callable(self):
        # Verify that the pipeline can be called again

        # Verify pipe is not callable repeatedly with the same collection
        out_pipe = apply_switch(data_pipe)
        out = list(out_pipe)
        self.assertListEqual(out, expected_data_list)

        # Verify is configurable with different collection
        out_pipe = apply_switch(data_pipe)
        out = list(out_pipe)
        self.assertListEqual(out, expected_data_list)


    # ------------------------------------------------------------------------------
    # Binary case block
    # ------------------------------------------------------------------------------


    def test_binary_case(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
        expected_data_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Unknown"]

        # Set up the switch
        data_pipe = binary_switch()

        # Assign values (default implicitly assigned through the False case)
        case_true(data_pipe, "Found Four")
        case_false(data_pipe, "Not Four")

        # Apply the switch
        out_pipe = apply_switch(data_pipe, data_list)
        out = list(out_pipe)
        self.assertListEqual(out, expected_data_list)



    # ------------------------------------------------------------------------------
    # If-else block
    # ------------------------------------------------------------------------------


    def test_ifelse(self):

        # Value-based equivalency
        # Expression-based equivalency



    # ------------------------------------------------------------------------------
    # Binary if-else block
    # ------------------------------------------------------------------------------



    def test_binary_ifelse(self):



