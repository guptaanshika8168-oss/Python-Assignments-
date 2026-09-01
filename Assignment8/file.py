File1 = open("Assignment8/APP1.txt", "r")
lines = File1.readlines()
File1.close()
print("Total number of lines n the file APP1.txt: ", len(lines))
First_two_lines = lines[0:2]
print("\nFisrt two lines of file: \n")
for i in First_two_lines:
    print(i)
File2 = open("Output.txt", "w")
File2.writelines(First_two_lines)
print("\nFirst two lines of APP1.txt file are written to output.txt ")
File2.close()