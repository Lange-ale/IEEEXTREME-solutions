def printOmino():
    for i in range(len(omino)):
        print(omino[i][0] + omino[i][1] + omino[i][2])


def turn():
    replace = {"(": ")", ")": "(", "\\": "/", "/": "\\", "<": ">", ">": "<", " ": " "}
    temp1 = omino[0][0]
    temp2 = omino[1][0]
    temp3 = omino[2][0]
    omino[0][0] = replace[omino[0][-1]]
    omino[1][0] = replace[omino[1][-1]]
    omino[2][0] = replace[omino[2][-1]]
    omino[0][-1] = replace[temp1]
    omino[1][-1] = replace[temp2]
    omino[2][-1] = replace[temp3]


T = int(input())
for _ in range(T):
    D = int(input())
    omino = [[" ", "o", " "], ["/", "|", "\\"], ["/", " ", "\\"]]
    swapped = False
    for d in range(D):
        command = input()
        if command[:3] == "say":
            print(command[4:])
        elif command == "turn":
            turn()
            printOmino()
            if swapped:
                swapped = False
            else:
                swapped = True
        else:
            command = command.split()
            side = command[0]
            if swapped:
                if side == "left":
                    side = "right"
                elif side == "right":
                    side = "left"
            bodyPart = command[1]
            position = command[-1]
            if position == "head":
                if side == "left":
                    omino[0][-1] = ")"
                    omino[1][-1] = " "
                else:
                    omino[0][0] = "("
                    omino[1][0] = " "
            elif position == "hip":
                if side == "left":
                    omino[0][-1] = " "
                    omino[1][-1] = ">"
                else:
                    omino[0][0] = " "
                    omino[1][0] = "<"
            elif position == "start":
                if side == "left":
                    omino[0][-1] = " "
                    omino[1][-1] = "\\"
                else:
                    omino[0][0] = " "
                    omino[1][0] = "/"
            elif position == "out":
                if side == "left":
                    omino[-1][-1] = "\\"
                else:
                    omino[-1][0] = "/"
            elif position == "in":
                if side == "left":
                    omino[-1][-1] = ">"
                else:
                    omino[-1][0] = "<"
            printOmino()
