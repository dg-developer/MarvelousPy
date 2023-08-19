# AKA switch block entry
from src.pipe.registry.PipelineRegistryEntry import PipelineRegistryEntry

class CallableValue:
    """House a value, or expression used to determine a value."""

    def __init__(self, value_expression):

        self.value_expression_fcn = value_expression

        # Transform a non-callable value into a callable function
        if not callable(value_expression):
            self.value_expression = lambda item: value_expression

    def get_value(self, item):
        return self.value_expression_fcn(item)



class AbstractSwitchBlockRegistryEntry(PipelineRegistryEntry):
    def __init__(self, match_expression_function, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)
        self.match_expression_function = match_expression_function
        self.case_block_value_registry = {}
        self.case_block_expression_registry = {}
        self.default_block_value = None

    def apply(self, item):

        # Determine match expression
        match_expression = item
        if self.match_expression_function is not None:
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
        if callable(self.default_block_value):
            return self.default_block_value(item)
        else:
            return self.default_block_value


class SwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, match_expression_function, pipe_from=None, pipe_to=None):
        super().__init__(match_expression_function=match_expression_function, pipe_from=pipe_from, pipe_to=pipe_to)

    def add_case(self, match_expression, value_expression):
        if callable(match_expression):
            self.case_block_expression_registry[match_expression] = CallableValue(value_expression)
        else:
            self.case_block_value_registry[match_expression] = CallableValue(value_expression)

    def add_default(self, value_expression):
        self.default_block_value = value_expression



class BinarySwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, match_expression_function=None, pipe_from=None, pipe_to=None):
        super().__init__(match_expression_function=match_expression_function, pipe_from=pipe_from, pipe_to=pipe_to)

    def add_true(self, value_expression):
        self.case_block_value_registry[True] = CallableValue(value_expression)

    def add_false(self, value_expression):
        self.case_block_value_registry[False] = CallableValue(value_expression)
        self.default_block_value = value_expression




# TODO
# class EnumSwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
