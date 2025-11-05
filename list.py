# Step 1: Ask the user how many items they want to add
n = int(input("Number of items: "))

# Step 2: Collect items from the user
items = []
for i in range(n):
    item = input("Enter item: ")
    items.append(item)

# Step 3: Display the list (optional)
print("Your list:", items)

# Step 4: Ask the user what item they want to search
search_item = input("What do you want to search: ")

# Step 5: Use for loop and enumerate to find the position
found = False
for index, value in enumerate(items):
    if value == search_item:
        print(f"{search_item.capitalize()} is in {index} position.")
        found = True
        break

if not found:
    print(f"{search_item.capitalize()} is not in the list.")

# completion of program