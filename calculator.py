def add(P, Q):
    return P + Q
def subtract(P ,Q):
    return P - Q
    def mutilpy(P, Q):
        return P * Q
        def divde(P, Q):
            return P/Q

print("please select the operation,")
print("a .Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("please enter the first choice(a/b/c/d): ")

num_1 = int(input("please enter the first number: "))
num_2 = int(input("please enter the secound number: "))

if choice == 'a':
    print(numb_1, "+", num_2, " = ", add(num_1, num_2))
elif choice == 'b':
    print(num_1, " - ",num_2, " = ", subtract(num_1, num_2))
elif choice == 'c':
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))
elif choice == 'd':
    print(num_1, " / ", num_2, " = ", divide(num_1,num_2))
else:
    print("this is an invalid input")