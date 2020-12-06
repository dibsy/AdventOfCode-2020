inputlist = [line.strip() for line in open('input1.txt')]

for x in inputlist:
        for y in inputlist:
                for z in inputlist:
                        if (int(x)+int(y)+int(z)) == 2020:
                                print(str(x)+"*"+str(y)+"*"+str(z)+"="+str(int(z) * int(y) * int(x)))
