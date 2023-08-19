# AKA switch block entry
from src.pipe.registry.PipelineRegistryEntry import PipelineRegistryEntry

class SwitchBlockRegistryEntry(PipelineRegistryEntry):
    def __init__(self, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)
        self.case_block_registry = {}

class BinarySwitchBlockRegistryEntry(SwitchBlockRegistryEntry):
    def __init__(self, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)

class EnumSwitchBlockRegistryEntry(SwitchBlockRegistryEntry):
    def __init__(self, pipe_from=None, pipe_to=None):
        super().__init__(pipe_from=pipe_from, pipe_to=pipe_to)
