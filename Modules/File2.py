import sys

sys.path.append(r'C:\Users\gauta\PycharmProjects\Python Concept - Gautam\Modules\File1' )

import File1

def add( a, b ):
    print( f"a+b = { a+b }" )

print("Inside File 2")

File1.f1()
File1.start()

add(5, 9)
