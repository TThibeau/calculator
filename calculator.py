import os
from art import logo

mem = None

def calculate(n1,n2,op):
    if op == "+": return n1+n2
    if op == "-": return n1-n2
    if op == "*": return n1*n2
    if op == "/": return n1/n2
    print("No valid input")

while True:
    os.system('cls||clear')
    print(f"{logo}\n") 

    if mem is None: nr1 = float(input("What's the first number?: "))
    if mem is not None: 
        print(f"Previous number: {mem}")
        nr1 = mem

    operation = input("+\n-\n*\n/\nPick an operation: ")
    nr2 = float(input("What's the next number?: "))
    result = round(calculate(nr1,nr2,operation),2)

    print(f"{nr1} {operation} {nr2} = {result}") 
    
    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()

    if choice == "quit": break
    if choice != "y": 
        mem = None 
    else:
        mem = result
