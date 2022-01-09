import os

write = open("WriteStreamFile.txt", "w")
write.write("HelloWorld!Here are WriteStream By Python")
write.close()
f = open("properties.JSON", "r", encoding='utf-8')
# print(f.readline())
readfile = f.readlines()

for temp in readfile:
    print(temp)

f.close()

print("------------------------")
path = os.listdir("../Test")
print(path)
# print("------------------------")
try:
    print("----------------------")
    ErrorFile = open("not-a-file")
    print("----------------------")
    try:
        print(ErrorFile.readline())
    finally:
        ErrorFile.close()
        print("file is closed")
except (NameError, IOError) as result:
    print("Error")
    print(result)
try:
    print("----------------------")
    exitFile = open("exitFile.txt")
    print("----------------------")
    try:
        print(exitFile.readline())
    finally:
        exitFile.close()
        print("file is closed")
except (NameError, IOError) as result:
    print("Error")
    print(result)