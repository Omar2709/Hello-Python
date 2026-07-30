favorites = ['pizza', 'sushi', 'ice cream', 'tacos', 'pasta']

for idx, item in enumerate(favorites):
    print(idx, item)
    
count = 0
while count < len(favorites):
    print(f"I really like {favorites[count]}!")
    count += 1

# For loop with conditional statements
for dessert in favorites:
    if dessert == 'ice cream':
        print("Yes, one of my favorites is ", dessert)
        break
    else:
        print("No, Sorry, that dessert is not on my list")

food = input("What is your favorite dessert? ").strip().lower()
count = 0
while count < len(favorites):
    if favorites[count] == food:
        print("Yes, one of my favorites is ", favorites[count])
        break
    count += 1
else:
    print("No, Sorry, that dessert is not on my list")