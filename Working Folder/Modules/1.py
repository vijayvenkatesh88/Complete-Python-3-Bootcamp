def func():
	print("func in one.py")

print("Top Level in one.py")

if __name__=='__main__':
	print("One.py run directly")
else:
	print("one.py has been imported")