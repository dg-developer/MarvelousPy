from src.marvelous import switch
from src.pipe.switch.SwitchBlock import binary_switch
from src.typeutils import is_iterable


def generate_repeated_list(item, repetitions):

    # return binary_switch(is_iterable) \
    #     .add_true(lambda item: item * repetitions) \
    #     .add_false(lambda item: [item] * repetitions) \
    #     .apply(item)

    # fcn(is_iterable,
    #     lambda item: item * repetitions,
    #     lambda item: [item] * repetitions)

    if is_iterable(item):
        return item * repetitions
        # [item for i in range(0, repetitions)]
    else:
        return [item] * repetitions

def flatten(nested_list):
    # https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    # https://iteration-utilities.readthedocs.io/en/latest/generated/deepflatten.html
    for x in nested_list:
        if isinstance(x, Iterable) and not isinstance(x, (str, bytes)):
            for sub_x in flatten(x):
                yield sub_x
        else:
            yield x
