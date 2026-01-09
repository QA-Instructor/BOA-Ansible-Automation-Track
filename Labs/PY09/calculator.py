#! venv/bin/python3

def calculate_total(subtotal: float, rate: float = 20) -> float:
    '''
    calcluate total amount, given subtotal and vat rate
    vat rate should be provided as a percentage
    >>> calculate_total(100, 20)
    120.0
    >>> calculate_total(10, 50)
    15.0
    '''
    vat = (rate / 100) * subtotal
    return subtotal + vat

def calculate_original(total: float, rate: float = 20) -> float:
    vat_as_rate = rate / 100
    return total / (1 + vat_as_rate)

def calc_input_vat(): # may throw ValueError
    values = input("Enter values in the format subtotal@rate: ")
    values = map(int, values.split('@'))
    return calculate_total(*values)
