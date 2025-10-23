def input_list(n):
    """Helper function to input a list of integers"""
    lst = []
    for i in range(n):
        value = int(input(f"Enter element {i+1}: "))
        lst.append(value)
    return lst

def check_same_length(list1, list2):
    return len(list1) == len(list2)

def check_same_sum(list1, list2):
    return sum(list1) == sum(list2)

def check_common_elements(list1, list2):
    common = set(list1) & set(list2)
    return common


def main():
    print("Enter first list:")
    n1 = int(input("How many elements? "))
    list1 = input_list(n1)

    print("\nEnter second list:")
    n2 = int(input("How many elements? "))
    list2 = input_list(n2)

    while True:
        print("\n--- MENU ---")
        print("1. Check whether lists are of same length")
        print("2. Check whether lists sum to same value")
        print("3. Check whether any value occurs in both lists")
        print("4. Display both lists")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            if check_same_length(list1, list2):
                print("✅ Both lists are of the same length.")
            else:
                print("❌ Lists are of different lengths.")

        elif choice == '2':
            if check_same_sum(list1, list2):
                print("✅ Both lists have the same sum.")
            else:
                print("❌ Lists have different sums.")

        elif choice == '3':
            common = check_common_elements(list1, list2)
            if common:
                print(f"✅ Common elements found: {common}")
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

# Run the program
if __name__ == "__main__":
    main()
