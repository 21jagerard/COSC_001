fp = open("data", "r")  # r for read the file, w for write the file

fp_w = open("newdata", "w")

for l in fp:
    # print(l, end = "")  # end = "" gets rid of the extra spaces
    wlist = l.split(",")  # \n is the new line command

    for i in range(len(wlist)):
        wlist[i] = wlist[i].strip()

    # print(wlist)
    # fp_w.write(wlist[0]+"\n")
    # fp_w.write(str(100)+"\n")

    print(wlist)
    print(int(wlist) + 1)

#
#
# s = "aaaaaadartmouthaaaa"
# s = s.strip("a")
# print(s)

fp.close()  # whenever you open a file, you also need to close the file
fp_w.close()