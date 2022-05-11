# Press Shift+F10 to execute it or replace it with your code.

file1 = open("words.xml", "r")
file2 = open("words2.xml", "w")
a = 0
file2.write("<?xml version=\"1.0\" ?> " + "\n")
file2.write("<wordList>" + "\n")
for line in file1:
    if line.__contains__("<word>"):
        # print(line + str(a),end='')

        data = (line.split("<word>")[1].split("<")[0])
        file2.write("<word data=\"" + data + "\"/>" + '\n')

    a += 1

file2.write("</wordList>" + "\n")

print(a)
