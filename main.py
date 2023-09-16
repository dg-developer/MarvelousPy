from marvelous.marvelous import switch
from marvelous.pipe.switch.SwitchBlock import case, case_default, apply


def main():

    # Set up the switch
    data_pipe = switch()

    # Assign values directly
    case(data_pipe, 1, "One")
    case(data_pipe, 2, "Two")
    case(data_pipe, 3, "Three")
    case(data_pipe, 4, "Four")
    case(data_pipe, 5, "Five")
    case(data_pipe, 6, "Six")
    case(data_pipe, 7, "Seven")
    case(data_pipe, 8, "Eight")
    case(data_pipe, 9, "Nine")
    case(data_pipe, 10, "Ten")

    # Assign a default value
    case_default(data_pipe, "Unknown")

    # Apply the switch to capture data
    data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 999]
    expected_data_list = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                          "Unknown"]
    out_iterator = apply(data_pipe, data_list)
    print("output")
    print(list(out_iterator))
    print("expected output")
    print(expected_data_list)

