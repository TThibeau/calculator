import os
from art import logo

mem = None

def calculate(n1,n2,operation):
    if operation == "+": return n1+n2
    if operation == "-": return n1-n2
    if operation == "*": return n1*n2
    if operation == "/": return n1/n2
    print("No valid input")

while True:
    os.system('cls||clear')
    print(f"{logo}\n") 

    if mem is None: n1 = float(input("What's the first number?: "))
    if mem is not None: 
        print(f"Previous number: {mem}")
        n1 = mem

    operation = input("+\n-\n*\n/\nPick an operation: ")
    n2 = float(input("What's the next number?: "))
    result = round(calculate(n1,n2,operation),2)

    print(f"{n1} {operation} {n2} = {result}") 
    
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if choice == "quit": break
    if choice != "y": 
        mem = None 
    else:
        mem = result
