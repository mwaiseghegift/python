#the text to add
text = "\nThis text wa added"

"""the write operations
We use a to append

"""
file1 = open("file.txt", 'a')
file1.write(text)
file1.close()