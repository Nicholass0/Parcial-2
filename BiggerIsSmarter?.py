def read():
    lines = []
    line = input()
    while line:
        lines.append(line)
        line = input()
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
        lines[i].append(i+1)
        lines[i].append([])
    return lines

def lists(order): # takes list of 4-tuples
    a = []
    for i in range(len(order)): # create list "a" of IQ's
        a.append(order[i][1])
    n = len(order)             # n = number of elephants
    b = [0]*n                  # b = list of zeros with size n
    predecessors = [-1]*n      # predecessors = list of -1 with size n
    for i in range(n-2, -1, -1):
        m = max(b)             # m = biggest item in b
        index = b.index(m)     # index = index of biggest item in b
        if order[i][0] != order[i+1][0]:     # if the weights are not equal
             if order[i][1] < order[i+1][1]: # if the elephants IQ does not fit the sequence
                for j in range(i+1, n):      # iterate through previously investigated elephants
                    if order[i][1] > order[j][1]:   # if the IQ's fit the sequence
                        b[i] = b[j] + 1             # element of sequence list is one more than that of the compared elephant
                        predecessors[i] = j         # element of predecessors list is set to the index of the previous elephant in the sequence
                        break                       # break the loop
             if order[i][1] > order[i+1][1]:   # if the elephants IQ does fit the sequence
                b[i] = m + 1                   # element of sequence list is one more than the current max
                predecessors[i] = index        # element of predecessors list is set to the index of the previous element
        if order[i][0] == order[i+1][0]:    # if the weights are equal
            for k in range(i+2, n):         # iterate through the other previous elements
                if order[i][0] != order[k][0]:  # if the weight is not the same (greater)
                    if order[i][1] > order[k][1]:  # if the IQ fits the sequence
                        b[i] = b[k] + 1         # element of sequence list is one more than that of the compared elephant
                        predecessors[i] = k     # predecessor is set to the compared elephant
                        break
    for i in range(len(order)):              # set the last element of the tuple in the elephant list to be the number of longest sequence for that elephant
        order[i][3] = b[i]
    return (order, predecessors)


def takefirst(element):
    return element[0]

def sort(table):
    table = sorted(table, key = takefirst)   # sort elephants by weight
    for i in range(len(table)):              # iterate through elephants
        for j in range(i, len(table)):       # iterate through elephants on heavier side
            if (table[i][0] == table[j][0]) and (table[i][1] < table[j][1]): # if the weights are equal and the IQ
                    hold1 = table[i]                                         # is higher in the elephant further down
                    hold2 = table[j]                                         # then swap the elephants.
                    table[i] = hold2
                    table[j] = hold1
    return table

def main():
    yes = read()
    order = sort(yes)
    preds = (lists(order))[1]

    ma = 0
    for i in range(len(order)):
        if order[i][3] > ma:
            ma = order[i][3]
            ind = i
    ma = ma + 1
    final = []
    while ind != -1:
        final.append(order[ind][2])
        ind = preds[ind]
    return(ma, final)



print(main())
