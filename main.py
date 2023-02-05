from math import floor

#determines if input is a number or not
def isNum(input):
    try:
        val = int(input)
        return True
    except:
        return False

#determines if a given nonnegative integer is prime and returns a boolean
def isPrime(num):

    #handles even numbers
    if num % 2 == 0 and num != 2:
        return False
    elif num == 2:
        return True

    #handles odd numbers > 1
    half = floor(num / 2)

    i = 3
    while (i < half):
        if num % i == 0:
            return False    
        i += 2
    
    return True

#runner of the entire program
def main():
    while True:

        #grabs user input
        givenNum = input("Enter a number: ")
        
        #check if given input is a number
        if isNum(givenNum):

            #checks if < 2  and returns 2 if so
            if float(givenNum) < 2:
                print("Finding closest prime... ")
                print("The closest prime to the given value: " + str(givenNum) + " is")
                print(str(2))
            else:
                #check if given num is prime
                if isPrime(int(givenNum)) and float(givenNum) - int(givenNum) == 0.0:
                    print("Given number is prime!")
                    
                #will find the closest prime to the given number
                print("Finding closest prime... ")
                
                i = 1
                while (not isPrime(int(givenNum) + i)) and (not isPrime(int(givenNum) - i)):
                    i += 1

                print("The closest prime to the given value: " + str(givenNum) + " is")
                if isPrime(int(givenNum) + i):
                    print(str(int(givenNum) + i))
                else:
                    print(str(int(givenNum) - i))
             
        else:
            print(str(givenNum) + " is NaN!")

        #grab user input to continue running main
        cont = input("Would you like to continue?:\n1 - YES\n0 - NO\n")

        #stop running
        if cont == str(0):
            print("Thank you for using this program!")
            break

        #invalid input so continue running
        elif cont != str(1):
            print("Invalid Input!\nRestarting program!")

main()