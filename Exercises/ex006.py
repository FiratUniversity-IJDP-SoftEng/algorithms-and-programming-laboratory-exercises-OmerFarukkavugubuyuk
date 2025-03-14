# Your Student ID:230543015
# Your Name and Surname: Ömer Faruk Kavuğubüyük
numbers = list(range(1, 11))

print("Original list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)

numbers.extend([11, 12, 13])
print("Extended list:", numbers)

print("Length of the list:", len(numbers))

numbers.pop(0) 
numbers.pop(-1)
print("List after removing first and last elements:", numbers)

even_numbers = sorted([num for num in numbers if num % 2 == 0])
print("Sorted even numbers list:", even_numbers)
