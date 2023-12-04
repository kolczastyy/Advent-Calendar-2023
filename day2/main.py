def choseColor(color: str) -> int:
    maxR = 12
    maxG = 13
    maxB = 14
    if color == "green":
        return maxG
    if color == "red":
        return maxR
    if color == "blue":
        return maxB

with open("input.txt") as file:
    lines = file.readlines()
    result = 0
    
    for line in lines:
        line = line.strip()
        content = line.split(":")
        sets = content[1].split(";")
        
        flag = True
        for sset in sets:
            colors = sset.split(",")

            for color in colors:
                amount = color.split()
                if int(amount[0]) > choseColor(amount[1]):
                    flag = False
                    break
            if not flag: break

        if flag:
            result += int(content[0].split()[1])

print(result)