def fixEmendedDoc(x: str) -> int:
    numbers = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for i in x:
        indexes = checkLetterNumbers(x)
        if i.isdigit():
            result = i
            break
        if x.index(i) in indexes.values():
            result = numbers[list(indexes.keys())[list(indexes.values()).index(x.index(i))]]
            break
    for i in x[::-1]:
        if i.isdigit():
            result += i
            break
        if x.index(i) in indexes.values():
            result += numbers[list(indexes.keys())[list(indexes.values()).index(x.index(i))]]
            break
    return int(result)

def checkLetterNumbers(x: str) -> dict:
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    indexes = dict()
    for i in numbers:
        if i in x:
            indexes[i] = x.index(i)
    return indexes

with open("input.txt") as file:
    lines = file.readlines()
    result = 0
    for line in lines:
        line = line.strip()
        result += fixEmendedDoc(line)

print(result)