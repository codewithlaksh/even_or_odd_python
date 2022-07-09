def myFunction():
    list1 = []
    while True:
        userInp = input("Enter your number or press q to exit\n")

        if userInp == "q":
            evens = []
            odds = []

            for i in range(0, len(list1)):
                if int(list1[i]) % 2 == 0:
                    evens.append(list1[i])
                else:
                    odds.append(list1[i])
            print("Your list of numbers: ", list1)
            if len(evens) == 0:
                print("No even numbers detected.")
            else:
                print("Even numbers are:", evens)
            if len(odds) == 0:
                print("No odd numbers detected.")
            else:
                print("Odd numbers are:", odds)
            break
        else:
            try:
                userInp = int(userInp)
                if userInp not in list(list1):
                    list1.append(userInp)
            except ValueError:
                print("Error: You have entered a non integer or a decimal fraction number.")

if __name__ == "__main__":
    myFunction()