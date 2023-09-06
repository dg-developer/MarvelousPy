from src.pipe.case.SwitchBlockRegistryEntry import SwitchBlockRegistryEntry, BinarySwitchBlockRegistryEntry


# ------------------------------------------------------------------------------
# Switch block builder interface
# ------------------------------------------------------------------------------

def switch(match_expression_function=None):
    return SwitchBlockRegistryEntry(match_expression_function)

def case(data_pipe, match_expression, value_expression):
    return data_pipe.add_case(match_expression, value_expression)

def cases_from_dict(data_pipe, case_lookup):
    data_pipe.add_cases_from_dict(case_lookup)

def case_default(data_pipe, value_expression):
    return data_pipe.add_default(value_expression)

# ------------------------------------------------------------------------------
# Binary switch block builder interface
# ------------------------------------------------------------------------------

def binary_switch(match_expression_function=None):
    return BinarySwitchBlockRegistryEntry(match_expression_function)

def case_true(data_pipe, value_expression):
    data_pipe.add_true(value_expression)

def case_false(data_pipe, value_expression):
    data_pipe.add_false(value_expression)



# ------------------------------------------------------------------------------
# Switch executor interface
# ------------------------------------------------------------------------------


def apply(data_pipe, data):
    return data_pipe.apply(data)

def apply_keys(data_pipe, data):
    return data_pipe.apply_keys(data)

def apply_values(data_pipe, data):
    return data_pipe.apply_values(data)



# ------------------------------------------------------------------------------
# Map-reduce interface
# ------------------------------------------------------------------------------

def fmap(mapping_function):
    return SwitchBlockRegistryEntry().add_default(mapping_function)

def reduce(reduce_function):
    data_pipe = SwitchBlockRegistryEntry()




