arr=[4,8,9],[8,9,4],[9,8,6]
si=0
ei=0
while ei< len(arr):
    ce=ei
    while ce<len(arr):
        print(arr[si][ce])
        si=si+1
        ce=ce+1
    si=0
    ei=ei+1