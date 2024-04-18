def equilateral(sides):
    if istriangle(sides):
        if sides[0] == sides[1] and sides[0] == sides[2]:
            return True
        else:
            return False
    else:
        return False



def isosceles(sides):
    if istriangle(sides):
        if (sides[0] == sides[1] or sides[0] == sides[2] or sides[1] == sides[2]):
            return True
        else:
            return False
    else:
        return False


def scalene(sides):
    if istriangle(sides):
        if (sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]):
            return True
        else:
            return False
    else:
        return False
    
def istriangle(sides):
    try:
        float(sides[0])
        float(sides[1])
        float(sides[2])
    except IndexError:
        return False
    except ValueError:
        return False
    else:
        if (sides[0] + sides[1] > sides[2]) and (sides[0] + sides[2] > sides[1]) and (sides[1] + sides[2] > sides[0]):
            return True
        else:
            return False

sides = [2, 3, 4]
print (istriangle(sides))
print (scalene(sides))
print (equilateral(sides))
print (isosceles(sides))