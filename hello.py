import sys

def greet(greeted_name:str, shout_count:int=1):
    return f"Hello, {greeted_name}{shout_count*'!'}"
    
if len(sys.argv) == 3 :
    n = int(sys.argv[2])
elif len(sys.argv) == 2:
    n = 1
    
print(greet(sys.argv[1], n))