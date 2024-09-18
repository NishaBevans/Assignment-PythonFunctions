#Task 1: Write a function that lets the user add items to a list.
shopping_list = []

def display_shopping_list():
    print("Your Shopping List:")
    for i, item in enumerate(shopping_list):
        print(f"{i+1}. {item}")
def add_item():
    item = input("Enter an item to add to your list: ")
    if item not in shopping_list:
        shopping_list.append(item)
        print(f"Added '{item}' to your list.")
#Task 2: Include a function that lets the user remove items from the list.
def remove_item():
    if shopping_list:
        print("Your Shopping List:")
        for i, item in enumerate(shopping_list):
            print(f"{i+1}. {item}")
        
        item_to_remove = int(input("Enter the number of the item to remove: ")) - 1
        try:
            del shopping_list[item_to_remove]
            print(f"Removed item from your list.")
        except IndexError:
            print("Invalid choice. Please choose a valid item number.")
    else:
        print("Your list is empty.")
#Task 3: Add a function that prints out the entire list in a formatted way.
while True:
    print("\nOptions:")
    print("1. Add an item")
    print("2. Remove an item")
    print("3. Display your shopping list")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_item()
    elif choice == "2":
        remove_item()
    elif choice == "3":
        display_shopping_list()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Please choose a valid option.")