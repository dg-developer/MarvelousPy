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
    def __init__(self, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)


class SwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, match_expression_function, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)
        self.match_expression_function = match_expression_function
        self.case_block_value_registry = {}
        self.case_block_expression_registry = {}

    def add_case(self, match_expression, value_expression):
        if callable(match_expression):
            self.__add_expression_case(match_expression, value_expression)
        else:
            self.__add_value_case(match_expression, value_expression)

    def __add_value_case(self, match_value, value_expression):
        self.case_block_value_registry[match_value] = CallableValue(value_expression)

    def __add_expression_case(self, match_fcn, value_expression):
        self.case_block_expression_registry[match_fcn] = CallableValue(value_expression)



class BinarySwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)

    def add_case(self):
        if not binary value, throw
        super.add_case()

class EnumSwitchBlockRegistryEntry(AbstractSwitchBlockRegistryEntry):
    def __init__(self, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)

    def add_case(self):
        if not enum value, throw
        super.add_case()
