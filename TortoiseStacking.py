
def enter():
    lines = []
    line = input()
    while line:
        lines.append(line)
        line = input()
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
    return lines

def stack(tortoises):
    tortoises = sorted(tortoises, key=getSecond)
    hold = [float("inf") for _ in tortoises]
    hold[0] = 0
    lq = 0
    for w, s in tortoises:
        for i in range(lq, -1, -1):
            if s > hold[i]+w and w + hold[i] < hold[i+1]:
                hold[i+1] = hold[i]+w
                lq = max(lq, i+1)
    return lq


def getSecond(element):
    return element[1]

def main():
    t = enter()
    return stack(t)

print(main())
