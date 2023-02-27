if __name__ == '__main__':

    # Calculator
    def add(n1, n2):
        return n1 + n2


    def subtract(n1, n2):
        return n1 - n2


    def multiply(n1, n2):
        return n1 * n2


    def divide(n1, n2):
        return n1 / n2


    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }


    def continuare2():
        while True:
            again = input("Did you finish. Y N: ").lower()
            print("test1")
            if again == "y" or again == "yes":
                print("test2")
                return False

            elif again == "n" or again == "no":
                print("test3")
                return True

    def startcalculation(num1= 0):
        if num1 == 0:
            num1 = int(input("What's the first number?: "))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        return answer
    def samenumber(resoults):
        while True:
            again = input(f"Use {resoults} as first number? Y N: ").lower()
            if again == "y" or again == "yes":
                return resoults
            elif again == "n" or again == "no":
                return 0
            else:
                print("i did not understand could you please say it again?")


    num1 = 0
    continuare = True

    while continuare:
        resoults = startcalculation(num1)
        continuare = continuare2()
        continuare = continuare
        num1 = samenumber(resoults)



