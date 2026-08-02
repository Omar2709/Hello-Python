def sum_of(**kwargs):
    sum = 0
    for l, v in kwargs.items():
        sum += v
    return sum

print(sum_of(Coffee=2.99, Tea=2.50, Juice=3.00, Water=1.00, Soda=2.00))  # Output: 11.49