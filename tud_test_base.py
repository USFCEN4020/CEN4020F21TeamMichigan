"""
Functions for pytest that are used to test commandline input and outputs
via 54ny7's branch of Mauricio Anciche original file
https://gist.github.com/54ny7/c6bec797d8777573b155bd78b644a3e0
"""

import builtins

input_values = []
print_values = []


def get_display_output():
    '''Get the printed output in list from the test target'''
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    """Set the input in list for 'input()'
    ['first input for the code', 'second text', ...]"""
    global input_values

    def mock_input_output_start():
        def mock_input(s=None):
            if s is not None:
                print_values.append(s)
            return input_values.pop(0)

        global input_values, print_values

        input_values = []
        print_values = []

        builtins.input = mock_input
        builtins.print = lambda s: print_values.append(s)

    mock_input_output_start()
    input_values = mocked_inputs


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values, previous_input, previous_print

    input_values = []
    print_values = []

    previous_input = builtins.input
    previous_print = builtins.print

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def mock_input_output_end():
    builtins.input = previous_input
    builtins.print = previous_print


def set_input(mocked_inputs):
    global input_values
    input_values = mocked_inputs
