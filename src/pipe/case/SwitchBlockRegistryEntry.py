# AKA switch block entry
from src.pipe.registry.PipelineRegistryEntry import PipelineRegistryEntry

class CallableValue:
    """House a value, or expression used to determine a value."""

    def __init__(self, value_expression):

        self.__value_expression_fcn = value_expression

        # Transform a non-callable value into a callable function
        if not callable(value_expression):
            self.__value_expression_fcn = lambda item: value_expression

    def get_value(self, item):
        return self.__value_expression_fcn(item)



class AbstractSwitchBlockRegistryEntry(PipelineRegistryEntry):
    """Represents a switch block."""

    def __init__(self, match_expression_function=None, pipe_from=None, pipe_to=None):
        """

        # Build a switch block with no expression transformation function.
        switch()
        case(...)
        default(...)

        # Build a pure mapping operation option 1
        switch(lambda x: <transform>)
        default(lambda x: x)

        # Build a pure mapping operation option 2
        switch()
        default(lambda x: <transform>)

        :param match_expression_function: Monolithic transformation function which could be used to form a mapping
                operation.
        :param pipe_from:
        :param pipe_to:
        """
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)

        if callable(match_expression_function):
            # Match expression provided
            self.match_expression_function = match_expression_function
        else:
            # Build match expression function to map onto itself
            self.match_expression_function = lambda x: x

        self.case_block_value_registry = {}
        self.case_block_expression_registry = {}

        # Assign None to return as the default value
        self.default_block_value = CallableValue(None)

    def _apply_item(self, item):
        """
        Apply case block to a single item.

        item -> match_expression -> value lookup -> expression lookup

        :param item:
        :return:
        """

        # Determine the match expression
        match_expression = self.match_expression_function(item)

        # Attempt to find the relevant case block by value lookup
        value_match_value = self.case_block_value_registry.get(match_expression)
        if value_match_value is not None:
            return value_match_value.get_value(item)

        # Attempt to find the relevant case block by evaluating item in an expression
        for case_block_expression, case_block_value in self.case_block_expression_registry:
            if match_expression == case_block_expression(item):
                return case_block_value.get_value(item)

        # Return default value
        return self.default_block_value.get_value(item)




class SwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, match_expression_function=None, pipe_from=None, pipe_to=None):
        super().__init__(match_expression_function=match_expression_function, pipe_from=pipe_from, pipe_to=pipe_to)

    def add_case(self, match_expression, value_expression):
        if not callable(match_expression):
            self.case_block_value_registry[match_expression] = CallableValue(value_expression)
        else:
            self.case_block_expression_registry[match_expression] = CallableValue(value_expression)

        return self

    def add_default(self, value_expression):
        self.default_block_value = CallableValue(value_expression)
        return self

    def add_cases_from_dict(self, case_lookup):
        """

        :param case_lookup: Values or expressions mapped to output values or expressions. None key denotes default case. Example:

                {
                    1: "One",                   # Maps a value to a value
                    lambda x: x == 2: "Two",    # Evaluates the match expression (computed from the item), and if the function returns true the value "Two" is returned.
                    3: lambda x: "Three",       # Maps a value to a function which is executed on the item.
                    None: "Unknown"             # Provides a default value. If not provided, None is used as the default.
                 }

        :return:
        """
        for match_expression, value_expression in case_lookup:
            if match_expression is None:
                self.add_default(value_expression)
            else:
                self.add_case(match_expression, value_expression)

        return self




class BinarySwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, match_expression_function=None, pipe_from=None, pipe_to=None):
        super().__init__(match_expression_function=match_expression_function, pipe_from=pipe_from, pipe_to=pipe_to)

    def add_true(self, value_expression):
        self.case_block_value_registry[True] = CallableValue(value_expression)
        return self

    def add_false(self, value_expression):
        self.case_block_value_registry[False] = CallableValue(value_expression)
        self.default_block_value = CallableValue(value_expression)
        return self



# TODO
# class EnumSwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):





