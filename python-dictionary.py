my_d = {1: 'Test', 'Name': 'Omar'}


my_d[1] = 'Test 1'
my_d['Name'] = 'Test 2'
my_d[2] = 'Test 3'

for key, value in my_d.items():
    print(str(key) + ": " + value)