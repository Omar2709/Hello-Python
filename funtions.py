def calculate_tax(bill, tax_rate):
    return round((bill * tax_rate) / 100, 2)

print ("Total tax is: ", calculate_tax(1264.25, 5))

print ("Total tax is: ", calculate_tax(2455.36, 10))