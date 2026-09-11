word = input("Enter the word to search: ")

count = 0

with open("input.txt", "r") as file:
    for line in file:
        if word in line:
            count += 1

print("Number of lines containing the word:", count)