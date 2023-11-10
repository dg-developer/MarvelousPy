# Design

TODO Document in progress

# Type of switching pipeline nodes:
# - Value-based
#   - Binary
#   - Case
# - Single-expression, single-outcome
#   - Binary
#   - Case block
# - Multi-expression
#   - Case block
#   - Generalized if-else

# - Binary
#   - Value-based, single-expression
# - Case
#   - Value-based, single-expression, multi-expression
# - Generalized if-else
#   - Multi-expression


General switch and general if-else can be considered the same, and "cases" added which either provide a mix of value-based and expression-based match expressions.

Mapping function can be overlayed on any solution.

Binary switch must disallow any additional cases to be added. 

Enum must disallow any additional cases to be added.


pipe registry PipelineRegistry
    pipe node (case block.pipe_reference) CaseBlockRegistryEntry(PipelineRegistryEntry)
        [from]
        [to]
        case block lookup table
            mapping function
            match value table
                apply function to produce value - CaseBlock
            match expression table
                apply function to produce value - CaseBlock

# TODO Reference the https://iteration-utilities.readthedocs.io/en/latest library
