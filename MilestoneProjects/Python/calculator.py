print('''
1 ADD
2 SUBTRACT
3 MULTIPLY
4 DIVIDE
5 MODULUS
6 EXPONENT
7 FLOOR DIVISION
''')
num1=int(input("Enter the value1:-"))
num2=int(input("Enter the value2:-"))
opr=input("Enter the opr...(1,2,3,4,5,6,7)")
if opr=="1":
    print(num1+num2)
elif opr=="2":
    print(num1-num2)
elif opr=="3":
    print(num1*num2)
elif opr=="4":
    print(num1/num2)
elif opr=="5":
    print(num1%num2)
elif opr=="6":
    print(num1**num2)
elif opr=="7":
    print(num1//num2)

else:
    print("Invalid opr...")