test1 = "   -123045"
s = "   -42"
s = "-42"
s2 = "4193 with words"
s3 = " with words 4333"
num_map = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}



def find_num(inputarr: str) -> str:
    inputarr = inputarr.lstrip().rstrip()
    array = inputarr.split(" ")
    print(array)
    for arr in array:
        if arr.isnumeric:
            print(arr)
            return arr

    return ""

def convertToInteger(inputstring: str) -> int:
    stripped = find_num(inputstring)
    if stripped == "":
        stripped = stripped.lstrip().rstrip()
    sign = "+"
    if stripped[0] == "-":
        sign = "-"
        stripped = stripped[1:]
    elif stripped[0] == "+":
        stripped = stripped[1:]

    constant = 10
    power = 0
    num = 0

    for i in reversed(stripped):
        num = num + num_map.get(i)*pow(constant, power)
        power += 1

    if sign == "-":
        num = num * -1

    print(num)

convertToInteger(s)
convertToInteger(s2)
convertToInteger(s3)