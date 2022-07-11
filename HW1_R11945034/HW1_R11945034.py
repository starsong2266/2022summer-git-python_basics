with open("../HW1/HW1.txt", 'r') as myfile:
    lines_count = 0
    garbled = 0
    stat_before = [0, 0, 0, 0, 0, 0]
    stat_after = [0, 0, 0, 0, 0, 0]
    for line in myfile.readlines():
        lines_count += 1
        lengthA = len(line) - 1 # no \n
        if(lengthA <= 40):
            stat_before[0] += 1
        elif(lengthA <= 50 and lengthA > 40):
            stat_before[1] += 1
        elif(lengthA <= 60 and lengthA > 50):
            stat_before[2] += 1
        elif(lengthA <= 70 and lengthA > 60):
            stat_before[3] += 1
        elif(lengthA <= 80 and lengthA > 70):
            stat_before[4] += 1
        elif(lengthA > 80):
            stat_before[5] += 1

        if('?' in line or '!' in line or '+' in line or '-' in line):
            garbled += 1
            for ch in "!?+-":
                line = line.replace(ch, '')
        lengthB = len(line) - 1 # no \n
        if(lengthB <= 40):
            stat_after[0] += 1
        elif(lengthB <= 50 and lengthB > 40):
            stat_after[1] += 1
        elif(lengthB <= 60 and lengthB > 50):
            stat_after[2] += 1
        elif(lengthB <= 70 and lengthB > 60):
            stat_after[3] += 1
        elif(lengthB <= 80 and lengthB > 70):
            stat_after[4] += 1
        elif(lengthB > 80):
            stat_after[5] += 1

        #print(lines_count, lengthA, lengthB)
with open("HW1_R11945034.txt", 'w') as myfile2:
    myfile2.write("There are {} sentences in HW1.txt. {} of them include !?+-.\n".format(lines_count, garbled))
    myfile2.write("length before trim after trim\n")
    for i in range(0, 6):
        if(i != 5):
            myfile2.write("  <={}{:>12d}{:>11d}\n".format((i+4)*10, stat_before[i], stat_after[i]))
        else:
            myfile2.write("   >80{:>12d}{:>11d}\n".format(stat_before[i], stat_after[i]))
