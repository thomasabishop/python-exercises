'''
Write a program which will find all such numbers which are divisible by
7 but are not a multiple of 5, between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on
a single line.
'''

# Declare new set
matches = set()
for i in range(200, 3200):
    if i % 7 == 0 and i % 5 != 0:
        matches.add(i)
convert_to_string = [str(num) for num in matches]
printable_string = ", ".join(convert_to_string)
print(printable_string)
