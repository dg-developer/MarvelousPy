
class PipelineRegistryEntry:
    """Represents a node in a processing pipeline."""

    def __init__(self, pipe_from=None, pipe_to=None):
        self.pipe_from = pipe_from
        self.pipe_to = pipe_to

    def execute(self, *args, **kwargs):
        pass
