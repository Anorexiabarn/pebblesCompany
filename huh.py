#for x in range(1,20):
#    file = open("test%x"%x, 'w')
#    file.write('%x'%x)
#    for x in range(19,1):
#        file = open("test%x"%x, 'a')
#        file.write('%x'%x)
#    file.close()
num = 19
for x in range(1,9999):
    filename = "test%d.txt" % (x)
    writeFile = open(filename, 'w')
    writeFile.write("%d" % (num))
    writeFile.close()
    num -= 1