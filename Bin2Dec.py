def binary_to_decimal(binary):
    result = 0
    for i in range(len(binary)):
        if binary[i] == '1':
            result += 2**abs(len(binary)-i-1)
    return result

first = True
while True:
    if not first:
        answer = input("Enter 'yes' to enter another binary number? Anything else otherwise ")
        if answer != "yes":
            exit(0)
    binary = input("Enter a binary number, any bit length: ")
    error = False
    for i in range(len(binary)):
        if binary[i] != '0' and binary[i] != '1':
            print("ERROR, input not expected")
            error = True
            break
    if error:
        first = True
        continue
    print(binary,"in decimal numbers is",binary_to_decimal(binary))
    first = False

