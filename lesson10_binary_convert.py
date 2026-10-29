num = int(input("Enter a number: "))

if num == 0:
    print("0")
else:
    if isinstance(num, str):
        print("It is a string, try again please")
    else:
        result = ""
        while num > 0:
            result = str(num % 2) + result
            num = num // 2
        print(result)