def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
display_menu()

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
          item = input("add an item")
          shopping_list.append(item)
          print(f'{item } has been added to the list')
            
        elif choice == '2':
            item = shopping_list.remove(item)
            print(f'your item has been removed is {item}')
        elif choice == '3':
           print(shopping_list)
         
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()