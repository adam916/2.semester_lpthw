from sys import argv

script, filename = argv

text = open(filename)

print(f"heres your file {filename}:")
print(text.read())
text.close()
print("type the filename again: ")
file_again = input(">")

text_again = open(file_again)

print(text_again.read())

text_again.close()

