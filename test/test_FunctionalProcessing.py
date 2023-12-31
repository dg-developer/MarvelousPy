import itertools
import unittest

from src.marvelous import switch
from src.pipe.switch.SwitchBlock import *


class FunctionalProcessingTests(unittest.TestCase):

    def setUp(self):

        self.data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
        self.expected_data_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                                   "Unknown"]

    # ------------------------------------------------------------------------------
    # Case block
    # ------------------------------------------------------------------------------

    def test_switch_management_conventional_approach(self):
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

    def test_switch_nominal_usage_list(self):

        # Set up the switch
        data_pipe = switch()

        # Assign values directly
        case(data_pipe, 1, "One")
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
        out_iterator = apply(data_pipe, self.data_list)
        self.assertListEqual(list(out_iterator), self.expected_data_list)

    def test_switch_function_usage_list(self):

        # Set up the switch
        data_pipe = switch()

        # Assign a value through a function
        case(data_pipe, 1, lambda x: "One")

        # Ignore the match expression and evaluate the value expression only
        case(data_pipe, lambda x: x + 1 == 3, "Two")

        # Use a function to generate a function
        case(data_pipe, lambda x: x + 1 == 4, lambda x: 2 * x)

        # Assign a default value
        case_default(data_pipe, "Unknown")

        # Apply the switch to capture data
        out_iterator = apply(data_pipe, [1, 2, 3, 4])
        self.assertListEqual(list(out_iterator), ["One", "Two", 6, "Unknown"])

    def test_switch_dictionary_registered_lookup(self):
        case_lookup = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                       9: "Nine", 10: "Ten", None: "Unknown"}

        # Build switch from dictionary lookup structure
        data_pipe = switch()
        cases_from_dict(data_pipe, case_lookup)
        out_iterator = apply(data_pipe, self.data_list)
        self.assertListEqual(list(out_iterator), self.expected_data_list)

        # Able to mix usage of dictionary lookup and conventional case registration
        case(data_pipe, 3, lambda x: "The Three Number")
        case_default(data_pipe, "New Default")
        out_iterator = apply(data_pipe, self.data_list)
        self.assertListEqual(list(out_iterator),
                             ["One", "Two", "The Three Number", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                              "New Default"])

    def test_switch_dict_keys(self):
        data_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                     10: "Ten", 999: "Nine-Hundred Ninety-Nine"}
        expected_data_dict = {"ONE": "One", "TWO": "Two", "THREE": "Three", "FOUR": "Four", "FIVE": "Five",
                              "SIX": "Six", "SEVEN": "Seven", "EIGHT": "Eight", "NINE": "Nine", "TEN": "Ten",
                              "UNKNOWN": "Nine-Hundred Ninety-Nine"}
        data_pipe = switch()
        case(data_pipe, 1, "ONE")
        case(data_pipe, 2, "TWO")
        case(data_pipe, 3, "THREE")
        case(data_pipe, 4, "FOUR")
        case(data_pipe, 5, "FIVE")
        case(data_pipe, 6, "SIX")
        case(data_pipe, 7, "SEVEN")
        case(data_pipe, 8, "EIGHT")
        case(data_pipe, 9, "NINE")
        case(data_pipe, 10, "TEN")
        case_default(data_pipe, "UNKNOWN")
        out_iterator = apply_keys(data_pipe, data_dict)
        self.assertDictEqual(dict(list(out_iterator)), expected_data_dict)

    def test_switch_dict_values(self):
        data_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                     10: "Ten", 999: "Nine-Hundred Ninety-Nine"}
        expected_data_dict = {1: "ONE", 2: "TWO", 3: "THREE", 4: "FOUR", 5: "FIVE", 6: "SIX", 7: "SEVEN", 8: "EIGHT",
                              9: "NINE", 10: "TEN", 999: "UNKNOWN"}
        data_pipe = switch()
        case(data_pipe, "One", "ONE")
        case(data_pipe, "Two", "TWO")
        case(data_pipe, "Three", "THREE")
        case(data_pipe, "Four", "FOUR")
        case(data_pipe, "Five", "FIVE")
        case(data_pipe, "Six", "SIX")
        case(data_pipe, "Seven", "SEVEN")
        case(data_pipe, "Eight", "EIGHT")
        case(data_pipe, "Nine", "NINE")
        case(data_pipe, "Ten", "TEN")
        case_default(data_pipe, "UNKNOWN")
        out_iterator = apply_values(data_pipe, data_dict)
        self.assertDictEqual(dict(list(out_iterator)), expected_data_dict)

    def test_switch_repeatedly_callable(self):
        # Verify that the pipeline can be called again

        case_lookup = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 7: "Seven", 8: "Eight",
                       9: "Nine", 10: "Ten", None: "Unknown"}

        # Verify pipe is not callable repeatedly with the same collection
        data_pipe = switch()
        cases_from_dict(data_pipe, case_lookup)
        out_iterator = apply(data_pipe, self.data_list)
        self.assertListEqual(list(out_iterator), self.expected_data_list)
        out_iterator = apply(data_pipe, self.data_list)
        self.assertListEqual(list(out_iterator), self.expected_data_list)

        # Verify is configurable with different collection
        data_list = ["A", "B", "Z", "C", "D"]
        expected_data_list = [10, 11, -1, 12, 13]
        case(data_pipe, "A", 10)
        case(data_pipe, "B", 11)
        case(data_pipe, "C", 12)
        case(data_pipe, "D", 13)
        case_default(data_pipe, -1)
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_switch_redefinition(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
        expected_data_list = ["OneOne", "TwoTwoTwo", "Unknown2", "Unknown2", "Unknown2", "Unknown2", "Unknown2",
                              "Unknown2", "Unknown2", "Unknown2", "Unknown2"]

        # Set up the switch
        data_pipe = switch()

        # Assign values directly
        case(data_pipe, 1, "One")
        case(data_pipe, 1, "OneOne")
        case(data_pipe, 2, "Two")
        case(data_pipe, 2, "TwoTwo")
        case(data_pipe, 2, "TwoTwoTwo")

        # Assign a default value
        case_default(data_pipe, "Unknown1")
        case_default(data_pipe, "Unknown2")

        # Apply the switch to capture data
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_switch_usage_as_map(self):

        # Pure mapping function
        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        data_pipe = switch()
        case_default(data_pipe, lambda item: item * item)
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

        # Mapping function with selector logic (maps all values except those matching a criterion)
        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [1, 4, 9, 16, 25, 36, "Seven", 64, 81, 100]
        data_pipe = switch()
        case(data_pipe, 7, "Seven")
        case_default(data_pipe, lambda item: item * item)
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    # ------------------------------------------------------------------------------
    # Binary case block
    # ------------------------------------------------------------------------------

    def test_binary_case_1(self):

        data_list = [True, False, True, True, False, False, "String"]
        expected_data_list = [1, 0, 1, 1, 0, 0, 0]

        # Set up the switch
        data_pipe = binary_switch()

        # Assign values (default implicitly assigned through the False case)
        case_true(data_pipe, 1)
        case_false(data_pipe, 0)

        # Apply the switch
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_binary_case_2(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
        expected_data_list = ["Not Four", "Not Four", "Not Four", "FOUND FOUR", "Not Four", "Not Four", "Not Four",
                              "Not Four", "Not Four", "Not Four", "Not Four"]

        # Set up the switch
        data_pipe = binary_switch(lambda x: x == 4)

        # Assign values (default implicitly assigned through the False case)
        case_true(data_pipe, "FOUND FOUR")
        case_false(data_pipe, "Not Four")

        # Apply the switch
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    # ------------------------------------------------------------------------------
    # If-else block
    # ------------------------------------------------------------------------------

    def test_ifelse(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [0, 1, 1, 1, 2, 2, 2, 3, 3, 3]

        data_pipe = switch()

        # Value-based equivalency
        case(data_pipe, 1, 0)

        # Expression-based equivalency
        case(data_pipe, lambda x: x < 5, 1)
        case(data_pipe, lambda x: 5 <= x <= 7, 2)
        case_default(data_pipe, 3)

        # Apply the switch
        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    # ------------------------------------------------------------------------------
    # Nested case blocks
    # ------------------------------------------------------------------------------

    def test_chained_functions(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [1, 4, 9, 16, 25, 216, 343, 512, 729, 1000]

        data_pipe = switch()
        c0 = lambda x: -x
        v0 = lambda x: x ** 2
        case(data_pipe, lambda x: c0(x) >= -5, lambda x: v0(x))
        c1 = lambda x: x - 0.1
        v1 = lambda x: x ** 3
        case(data_pipe, lambda x: c1(x) > 4.89, lambda x: v1(x))

        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_nested_case_blocks(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [1, 4, 9, "Four", "Five", "data_pipe_1 default", 343, 512, 729, "data_pipe_0 default"]

        data_pipe_1 = switch()
        case(data_pipe_1, 4, lambda x: "Four")
        case(data_pipe_1, lambda x: x == 5, "Five")
        case_default(data_pipe_1, "data_pipe_1 default")

        data_pipe_0 = switch()
        case(data_pipe_0, lambda x: x < 4, lambda x: x ** 2)
        case(data_pipe_0, lambda x: 4 <= x <= 6, lambda x: apply(data_pipe_1, x))
        case(data_pipe_0, lambda x: 6 < x < 10, lambda x: x ** 3)
        case_default(data_pipe_0, "data_pipe_0 default")

        out_iterator = apply(data_pipe_0, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_chained_statement_chaining(self):
        out_iterator = switch() \
            .add_case(1, "One") \
            .add_case(2, "Two") \
            .add_case(3, "Three") \
            .add_case(4, "Four") \
            .add_case(5, "Five") \
            .add_case(6, "Six") \
            .add_case(7, "Seven") \
            .add_case(8, "Eight") \
            .add_case(9, "Nine") \
            .add_case(10, "Ten") \
            .add_default("Unknown") \
            .apply(self.data_list)
        out = list(out_iterator)
        self.assertListEqual(out, self.expected_data_list)

    def test_chained_pipeline(self):
        # TODO
        pass










    # ------------------------------------------------------------------------------
    # Map-reduce
    # ------------------------------------------------------------------------------

    def test_fmap(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

        data_pipe = fmap(lambda x: x ** 2)

        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_fmap_with_special_cases(self):

        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected_data_list = [1, 4, 9, 3, 3, 3, 3, 64, 81, 100]

        data_pipe = fmap(lambda x: x ** 2)

        case(data_pipe, lambda x: 4 <= x < 8, 3)

        out_iterator = apply(data_pipe, data_list)
        self.assertListEqual(list(out_iterator), expected_data_list)

    def test_deque(self):
        # TODO Testing iterable slicing for application in accumulator function
        data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        iterable_data = iter(data_list)

        # qlen = 3
        # q = deque(iterable_data, 2)

        it = iter(data_list)
        l = itertools.islice(it, 3)
        ll = list(l)
        while len(ll) > 0:
            # print("l")
            # print(ll)
            l = itertools.islice(it, 3)
            ll = list(l)


if __name__ == "__main__":
    unittest.main()
