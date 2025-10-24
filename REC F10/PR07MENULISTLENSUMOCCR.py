
list1 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22]

list2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 30]

while True:
    print("\n--- MENU ---")
    print("1. Check whether lists are of same length")
    print("2. Check whether lists sum to same value")
    print("3. Check whether any value occurs in both lists")
    print("4. Display both lists")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        if len(list1) == len(list2):
            print("Both lists are same length.")
        else:
            print("Different lengths.")

    elif choice == '2':
        if sum(list1) == sum(list2):
            print("Both lists have same sum.")
        else:
            print("Different sums.")

    elif choice == '3':
        common = set(list1) & set(list2)
        if common:
            print(f"Common elements found: {common}")
        else:
            print("❌ No common elements between the two lists.")

    elif choice == '4':
        print(f"List 1: {list1}")
        print(f"List 2: {list2}")

    elif choice == '5':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
