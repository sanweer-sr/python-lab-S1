
names = ["Alice", "Amanda", "Brian", "Catherine", "David", "Sara"]

count_a = 0


for name in names:
    count_a += name.lower().count('a')


print("List of names:", names)
print("Total occurrences of 'a':", count_a)
