def is_armstrong_number (number):
    number2 = 0
    power = len(str(number))
    
    for i in str(number) :
        number2 = int(i)**power + number2

    if number2 == number :
        return True
    else:
        return False
