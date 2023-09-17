import unittest

from src.pipe.switch.SwitchBlockRegistryEntry import CallableValue


class CallableValueTests(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic(self):
        v1 = CallableValue("Some string")
        v2 = CallableValue(lambda x: "Some string")
        assert v1.get_value(3) == "Some string"
        assert v2.get_value(3) == "Some string"


if __name__ == "__main__":
    unittest.main()
