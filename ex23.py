def n1():
    lst1 = []
    lst = input("Enter a list of number: ")
    for i in lst.split():
        lst1.append(int(i))
    return lst1

def N1():
    lst1 = []
    lst = input("Enter another list of number: ")
    for i in lst.split():
        lst1.append(int(i))
    return lst1

def n2(lst):
    n = len(lst)
    i = 0
    while i < n:
        print(f"{lst[i]}X^{i}")
        i += 1

def N2(lst):
    n = len(lst)
    for i in range(n):
        print(lst[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")

def n3(lst, x):
    n = len(lst)
    i = 0
    value = 0
    while i < n:
        value += lst[i]*(x**(i))
        i += 1
    return value


def add(lst1, lst2):
    m = len(lst1)
    n = len(lst2)
    size = max(m, n);
    sum = [0 for i in range(size)]

    # Initialize the product polynomial

    for i in range(0, m, 1):
        sum[i] = lst1[i]

    # Take ever term of first polynomial
    for i in range(n):
        sum[i] += lst2[i]

    return sum


def substraction(lst1, lst2):
    m = len(lst1)
    n = len(lst2)
    size = max(m, n);
    sub = [0 for i in range(size)]

    # Initialize the product polynomial

    for i in range(0, m, 1):
        sub[i] = lst1[i]

    # Take ever term of first polynomial
    for i in range(n):
        sub[i] *= lst2[i]

    return sub


def multiplication(lst1, lst2):
    m = len(lst1)
    n = len(lst2)
    size = max(m, n);
    mul = [0 for i in range(size)]

    # Initialize the product polynomial

    for i in range(0, m, 1):
        mul[i] = lst1[i]

    # Take ever term of first polynomial
    for i in range(n):
        mul[i] *= lst2[i]

    return mul

def menuA(n, array):

    if n==1:
        print("1. Read a polynomial from keyboard")
        print("2. Print a polynomial")
        print("3. Calculate the value of a polynomial with a value of variable x (as a parameter of the function)")
        print("4. Calculate the sum of two polynomials")
        print("5. Calculate the substraction of two polynomials")
        print("6. Calculate the multiplication of two polynomials")
        print("7. Exit!")
        lst = n1()
        print("________________________________________________________\n")
        print("Are you want to continue choose another option ?")
        answer = input("Enter your choice: \n yes or no \n")
        if answer == "yes":
            op = int(input("Enter your option:"))
            menuA(op, lst)
        else:
            exit()
    elif n==2:
        N2(array)
        print("\n________________________________________________________\n")
        print("Are you want to continue choose another option ?")
        answer = input("Enter your choice: \n yes or no \n")
        if answer == "yes":
            op = int(input("Enter your option:"))
            return menuA(op, array)
        else:
            exit()
    elif n==3:
        print("Polymial:")
        N2(array)
        valuex = float(input("enter value x:"))
        print(f"value of polymial when x = {valuex} is {n3(array, valuex)}")
        print("\n________________________________________________________\n")
        print("Are you want to continue choose another option ?")
        answer = input("Enter your choice: \n yes or no \n")
        if answer == "yes":
            op = int(input("Enter your option:"))
            return menuA(op, array)
        else:
            exit()
    elif n==4:
        l2 = N1()
        sumP = add(array, l2)
        print("Sum of two polymial is:")
        N2(sumP)
        print("\n________________________________________________________\n")
        print("Are you want to continue choose another option ?\n")
        answer = input("Enter your choice: \n yes or no \n")
        if answer == "yes":
            op = int(input("Enter your option:"))
            return menuA(op, array)
        else:
            exit()
    elif n==5:
        l2 = N1()
        sub = substraction(array, l2)
        print("Substraction of two polymial is:")
        N2(sub)
        print("\n________________________________________________________\n")
        print("Are you want to continue choose another option ?")
        answer = input("Enter your choice: \n yes or no \n")
        if answer == "yes":
            op = int(input("Enter your option:"))
            return menuA(op, array)
        else:
            exit()
    elif n==6:
        l2 = N1()
        mul = multiplication(array, l2)
        print("Multiplication of two polymial is:")
        N2(mul)
        print("\n________________________________________________________\n")
        print("Are you want to continue choose another option ?")
        answer = input("Enter your choice: \n yes or no \n")
        if answer == "yes":
            op = int(input("Enter your option:"))
            return menuA(op, array)
        else:
            exit()
    elif n==7:
        exit()
    else:
        print("Your option is not in our menu! Please choose another option")
        menuA(1, 0)

if __name__ == "__main__":
    menuA(1, 0)