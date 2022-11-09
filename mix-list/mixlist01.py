#!/usr/bin/env python3



mylist = ["192.168.0.5", 5060, "UP"]

mylist2 = [5060, "80", 55, "10.0.0.1", "ssh"]

print("ip address is " +  mylist[0])
print("port =" + str(mylist[1]))

print("new ip is " + mylist2[3])


wordbank = ["indentation", "spaces"]

tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]


wordbank.append(4)

num = (int(input("enter num")))

student_name = tlgstudents[2]
print("{student_name} always uses {num} {wordbank[1]}")
print(student_name,"always uses",num, wordbank[1])


# hmod u+x no_shebang.py
