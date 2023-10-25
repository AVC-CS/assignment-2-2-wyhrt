def main():
    """
    ##################################################
    # Comlete your code here
    Use the same variables: celsius fahrenheit 
    ##################################################
    """
    while True:
        try:
            conversion_type = input("Which unit is your input temprature in? (C/F): " )
        except EOFError:
           break

        if conversion_type == "c" or conversion_type == "C":
         celsius = float(input("Input your celsius Temperature: "))
         fahrenheit = celsius * 1.8 + 32
         print("%i °C = %i °F" % fahrenheit)
         return celsius, fahrenheit
         exit

        if conversion_type == "f" or conversion_type == "F":
         fahrenheit = float(input("Input your fahrenheit Temperature: "))
         celsius = (fahrenheit - 32) * 5/9
         print("%i °F =  %i °C" %(fahrenheit,celsius)) 
         return celsius, fahrenheit
         exit

        else:
            print ("Unknown Temperature Type! Try Again.")
            continue


    """
    ########################################
    # Do not delete the return statement
    ########################################
    """

    ## return celsius, fahrenheit


if __name__ == '__main__':
    main()
