from WhereStuffHappens import test

elapsedtimes = []
testamounts = 10
testnumber = 1

screenname = input('Enter Twitter Screen name here: ')

while testnumber <= testamounts:
    time = test.one_test(screenname)
    elapsedtimes.append(time)
    testnumber += 1

averagetime = sum(elapsedtimes) / float(len(elapsedtimes))
averagetimeString = str(averagetime)
print(averagetimeString)
print(elapsedtimes)
file = open("averagetime.txt", "w")
file.write(screenname+"\n")
file.write(averagetimeString+"\n")
