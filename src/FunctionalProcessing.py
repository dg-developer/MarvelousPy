






# ------------------------------------------------------------------------------
# Pipeline registry management
# ------------------------------------------------------------------------------

class PipelineRegistryEntry:
    def __init__(self):

        # Need to store:
        # resettable_iterator
        #   collection_reference
        #   get_iterator()
        # registered switch nodes
        # registered pipelines
        #   these are callable and don't require construction,
        #   however could be registered to enable fluent API

class CaseBlockRegistryEntry(PipelineRegistryEntry):

    def __init__(self):
        self.case_blocks = []

    def add_case(self, switch_expression_fcn_or_value, case_result_fcn_or_value):
        self.case_blocks.append(CaseBlockRegistryEntry(switch_expression_fcn_or_value, case_result_fcn_or_value))





class CaseBlockRegistryEntry:

    def __init__(self, switch_expression_fcn_or_value, case_result_fcn_or_value):

        # Callable function passed in
        self.switch_expression_fcn = switch_expression_fcn_or_value
        self.case_result_fcn = case_result_fcn_or_value

        # If value passed in, change to callable function
        if not callable(switch_expression_fcn_or_value):
            self.switch_expression_fcn = lambda: switch_expression_fcn_or_value
        if not callable(case_result_fcn_or_value):
            self.case_result_fcn = lambda: case_result_fcn_or_value




class PipelineRegistry:
    def __init__(self):
        self.__iterables_registry = {}
        self.__case_block_registry = {}

    # Cleanup & resetting

    def delete_pipe_from_registry(self, pipe):
        if pipe in self.__iterables_registry:
            del self.__iterables_registry[pipe]
        if pipe in self.__case_block_registry:
            del self.__case_block_registry[pipe]

    def generate_new_pipe(self, pipe):
    # TODO Throw if something already registered with this pipe





    # Define new switch block

    def define_new_switch_block(self, pipe, fcn):
        self.__iterables_registry[pipe] = fcn
        self.__case_block_registry[pipe] = {}

    def register_case(self, pipe, value, fcn_or_value):
        self.__case_block_registry[pipe][value] = fcn_or_value

    def register_default_case(self, pipe, fcn_or_value):
        self.__case_block_registry[pipe][None] = fcn_or_value

    # Checks

    def is_switch_expression_fcn_defined(self, pipe):
        return pipe in self.__iterables_registry

    def is_default_case_defined(self, pipe):
        return None in self.__case_block_registry[pipe]

    # Access the switch logic

    def get_switch_expression_fcn(self, pipe):
        return self.__iterables_registry[pipe]

    def get_case_values(self, pipe):
        return pipeline_registry.__case_block_registry[pipe]


# Define the registry singleton
pipeline_registry = PipelineRegistry()


# ------------------------------------------------------------------------------
# Case block definition
# ------------------------------------------------------------------------------


def switch(iterable, fcn=None):
    pipe = iter(iterable)

    # Switch case expression may be determined by a function, or simply be the collection item
    fcn = fcn or (lambda x: x)

    pipeline_registry.delete_pipe_from_registry(pipe)
    pipeline_registry.define_new_switch_block(pipe, fcn)
    return pipe


def case(pipe, value, fcn_or_value):
    if not pipeline_registry.is_switch_expression_fcn_defined(pipe):
        raise AttributeError("No switch block is defined for this pipe.")
    pipeline_registry.register_case(pipe, value, fcn_or_value)


def case_default(pipe, fcn_or_value):
    if not pipeline_registry.is_switch_expression_fcn_defined(pipe):
        raise AttributeError("No switch block is defined for this pipe.")
    pipeline_registry.register_default_case(pipe, fcn_or_value)


def apply_switch(pipe):
    if not pipeline_registry.is_switch_expression_fcn_defined(pipe):
        raise AttributeError("No switch block is defined for this pipe.")

    if not pipeline_registry.is_default_case_defined(pipe):
        raise AttributeError("Default case not defined for switch.")

    switch_expression_fcn = pipeline_registry.get_switch_expression_fcn(pipe)

    # Need to reset the iterator in each applicaiton of the pipe, but Python provides no way
    new_pipe = pipeline_registry.generate_new_pipe(pipe)

    for item in pipe:

        switch_expression = switch_expression_fcn(item)

        case_values = pipeline_registry.get_case_values(pipe)

        if switch_expression in case_values:
            fcn_or_value = case_values[item]
        else:
            fcn_or_value = case_values.get(None)

        if callable(fcn_or_value):
            yield fcn_or_value(item)
        else:
            yield fcn_or_value
