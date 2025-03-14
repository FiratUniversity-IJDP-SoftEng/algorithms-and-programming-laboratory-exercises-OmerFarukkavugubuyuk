# Your Student ID:230543015
# Your Name and Surname: Ömer Faruk Kavuğubüyük
input = input("Enter a string: ")

counter = {}
for char in input:
    counter[char] = counter.get(char, 0) + 1

print("Character frequencies:")
for char in sorted(counter):
    print(f"{char}: {counter[char]}")
