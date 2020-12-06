inputlist = [line.strip() for line in open('input1.txt')]

for x in inputlist:
        y = 2020 - int(x)
        if str(y) in inputlist:
                print(str(x)+"*"+str(y)+"="+str(y * int(x)))

