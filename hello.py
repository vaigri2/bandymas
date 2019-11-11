import sys

def greet(greeted_name:str):
    print(f"Hello, {greeted_name}!")
    
greet(sys.argv[1])
