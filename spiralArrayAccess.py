def printSpiral(arr):
    turn = 1
    count = 0
    n = len(arr)
    totalPrint = len(arr)*len(arr[0])
    fdri,fdcsi,fdcei = 0,0,n-1
    sdci,sdrsi,sdrei = n-1,1,n-1
    tdri,tdcsi,tdcei = n-1,n-2,0
    fodci,fodsri,foderi = 0,n-2,1
    while count < totalPrint:
        if turn == 1:
            for i in range(fdcsi,fdcei+1):
                print(arr[fdri][i],end=" ")
                count+=1
            fdri+=1
            fdcsi+=1
            fdcei-=1
            turn = 2
        elif turn == 2:
            for i in range(sdrsi,sdrei+1):
                print(arr[i][sdci],end=" ")
                count+=1
            sdci-=1
            sdrsi+=1
            sdrei-=1
            turn = 3
        elif turn == 3:
            for i in range(tdcsi,tdcei-1,-1):
                print(arr[tdri][i],end=" ")
                count+=1
            tdri-=1
            tdcsi-=1
            tdcei+=1
            turn = 4
        else:
            for i in range(fodsri,foderi-1,-1):
                print(arr[i][fodci],end=" ")
                count+=1
            fodsri-=1
            foderi+=1
            fodci+=1
            turn = 1
def main():
    arr = [[8,-3,9,2],[9,3,2,8],[1,10,11,15],[8,9,15,14]]
    printSpiral(arr)

main()
