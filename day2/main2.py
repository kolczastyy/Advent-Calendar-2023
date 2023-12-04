with open("input.txt") as file:
    lines = file.readlines()
    result = 0
    
    for line in lines:
        line = line.strip()
        content = line.split(":")
        sets = content[1].split(";")
        
        flag = True
        maxG = 0
        maxR = 0
        maxB = 0
        for sset in sets:
            colors = sset.split(",")

            for color in colors:
                amount = color.split()
                if amount[1] == "green":
                    if int(amount[0]) > maxG:
                        maxG = int(amount[0])
                if amount[1] == "blue":
                    if int(amount[0]) > maxB:
                        maxB = int(amount[0])
                if amount[1] == "red":
                    if int(amount[0]) > maxR:
                        maxR = int(amount[0])

        result += maxG * maxR * maxB

print(result)