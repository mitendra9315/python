num=int(input("Enter number : "))
for i in range(1,num+1//2):
    if (i**2) == num:
        print(num," is a perfect sqaure")
        break
else:
    print(num,"is not a perfect square")