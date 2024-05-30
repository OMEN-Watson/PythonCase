x = 27

def increment_x():
    print("x before increment:", x)
    x = x + 1
    print("x after increment:", x)

increment_x()

print("(global) x after function:", x)