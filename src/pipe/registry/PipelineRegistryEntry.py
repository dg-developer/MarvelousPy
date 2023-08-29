from collections.abc import Iterable

class PipelineRegistryEntry:
    """Represents a node in a processing pipeline."""

    def __init__(self, pipe_from=None, pipe_to=None):
        self.pipe_from = pipe_from
        self.pipe_to = pipe_to

    def apply(self, item):
        """
        Apply the block to an item or iterable. In the case of a dictionary, key-value tuples are iterated.

        :param item
        :return:
        """

        # Dispatch
        if isinstance(item, Iterable):
            return self._apply_iterable(item)
        else:
            return self._apply_item(item)

    def apply_keys(self, dictionary_data):
        """Apply to the keys of a dictionary."""
        for key, value in dictionary_data:
            yield self._apply_item(key), value

    def apply_values(self, dictionary_data):
        """Apply to the values of a dictionary."""
        for key, value in dictionary_data:
            yield key, self._apply_item(value)

    def _apply_iterable(self, iterable_data):
        # Apply case block to items in an iterable.
        for item in iterable_data:
            yield self._apply_item(item)

    def _apply_item(self, item):
        """Apply to a single item."""
        pass
