file = open("FileHandling/input.txt", "r")

lines = file.readlines()

print("Number of lines:", len(lines))

first_two_lines = lines[0:2]

file.close()

output_file = open("FileHandling/output.txt", "w")
output_file.writelines(first_two_lines)
output_file.close()

print("First two lines written to output.txt")