def prnt_hello_world():
    print("Hello world!")

def try_multiplying(a,b):
    return a*b

def main():
    #This is my main function
    #This code contains sample codes of print hello world and multiplication

    a=19
    b =10


    c = try_multiplying(a, b)


    print("This is the result of multiplication")
    print(c)

    prnt_hello_world()

    def temp_func(cc, bcc):
        return cc+ bcc
    

    print("Result of adding 51 and 32 equals:", end=" ")    
    print(temp_func(51, 32))

    d =temp_func(5, 6)

    print("Addign 5 and 6 equals :- ",d)    


if __name__ == "__main__":
    main()