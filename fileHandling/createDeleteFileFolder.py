import os

#creating the file
file2 = open("created.txt", 'w')
file2.write("This is the written text")
file2.close()


if os.path.exists("created.txt"):
    os.remove("created.txt")
else:
    print("The file does not exist")

#to delete a folder
os.removedir("<folder_name>")