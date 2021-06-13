import random
def game():
    def decision():
        res = "a"
        while res.lower() != "y" and res.lower() != "n":
            res = input("Do you wanna play on?..y for yes n for no\n")
        return res
    while True:
        a = int(input("Input your bet starter\n"))
        b = int(input("Input your betting amount\n"))

        while  a>0 and a>b:
            r = random.randint(0,4)
            c = int(input("input your bet number between 0 and 3\n"))
            if c < 0 or c > 3 :
                print("Invalid!!!! Number must be between 0 and 3!!")
                continue
            else:
                if c == r:
                    a = a + b
                    print("You won!!..your money is",a)
                    if decision() == "y":
                        continue
                    else:
                        print("You walk away with",a,"Thanks for playing")
                        return
                    
                else:
                    a = a - b
                    print("You did not win.Your money is now",a)
                    if decision() == "y":
                          continue
                    else:
                        print("You walk away with",a,"Thanks for playing")
                        return
        if a <= 0:
            print("not enough money")
        else:
            print("Bet amount is greater than total amount")
        continue
    
if __name__ == "__main__":
    game()
