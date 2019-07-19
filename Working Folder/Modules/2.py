import 1

print("Top level in two.py")

one.func()

if __name__=='__main__':
	print("two.py called direclty")
else:
	print("two.py imported")