def square(number):
    grains = 2 ** (number - 1)
    if number < 1 or number > 64:
        raise ValueError ("square must be between 1 and 64")
    else:
        return grains

def total():
    grains = 2 ** 64 - 1
    return grains

