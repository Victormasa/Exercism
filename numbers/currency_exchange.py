import math
def exchange_money(budget, exchange_rate):
    money = budget / exchange_rate
    return money

def get_change(budget, exchanging_value):
    money = budget - exchanging_value
    return money

def get_value_of_bills(denomination, number_of_bills):
    money = denomination * number_of_bills
    return money

def get_number_of_bills(budget, denomination):
    money = budget // denomination
    return money

def get_leftover_of_bills(budget, denomination):
    money = budget % denomination
    return money

def exchangeable_value(budget, exchange_rate, spread, denomination):
    real_exchange = exchange_rate + ((exchange_rate/100)*spread)
    real_money = budget // real_exchange
    bills = real_money // denomination
    money = math.trunc(bills * denomination)
    return money
    