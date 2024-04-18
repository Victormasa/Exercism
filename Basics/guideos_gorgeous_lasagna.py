"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer

EXPECTED_BAKE_TIME = 40
COOK_LAYERS = 2
# TODO: define the 'bake_time_remaining()' function

def bake_time_remaining(remaining_time):
    """Returns the remaining time"""
    time = EXPECTED_BAKE_TIME - remaining_time
    return time

def preparation_time_in_minutes(layers):
    """Returns the time you should be cooking only the layers"""
    time = COOK_LAYERS * layers
    return time

def elapsed_time_in_minutes(layers, elapsed_bake_time):
    """Returns the time you have been cooking"""
    time = layers * COOK_LAYERS + elapsed_bake_time
    return time


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here


# TODO: define the 'elapsed_time_in_minutes()' function
