total = input("Enter total value: ")

ifprint = input("Print results? (1 or 0): ")
print

maxq = total/25
print "Max Quarters:",maxq

maxd = total/10
print "Max Dimes:",maxd

maxn = total/5
print "Max Nickels:",maxn

maxp = total
print "Max Pennies:",maxp,"\n"

print "Finding all possibilities..."
for currq in range(0,maxq+1):
    for currd in range(0,maxd+1):
        for currn in range(0,maxn+1):
            for currp in range(0,maxp+1):
                if ((currq * 25) + (currd * 10) + (currn * 5) + (currp)) == total:
                    if ifprint == 1:
                        print currq,currd,currn,currp
                    count = count + 1
print "Done!\n"
print "Count:",count




