import sys
import json
print(sys.argv)

def do_addieren(args):
    left = args[0]
    right = args[1] 
    return left + right

def do_absolutwert(args):
    if args >= 0:
        return args
    return -args

def main():
    filename = sys.argv
    print(filename)
    with open(filename, "r") as f:
        program = json.load(f)
        if program[0] == "addieren":
            result = do_addieren(program[1:])
        elif program[0] == "absolutwert":
            result = do_absolutwert(program[1:])
        print(program[0])
    print(result)



##json it's a universal language for storage and exchange of data
