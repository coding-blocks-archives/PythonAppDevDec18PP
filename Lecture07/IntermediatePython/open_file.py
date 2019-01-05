filename = input("Enter filename: ")

try:
	f = open(filename, 'r')
except FileNotFoundError:
	print("File does not exist")
else:
	print(f.read())
	f.close()
finally:
	print("Exiting..")