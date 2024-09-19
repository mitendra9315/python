















def main():
    arr=[-3,2,9,8,-3,5,2,1]
    n=len(arr)
    queries = [[5,7],[2,7],[1,6],[3,7],[0,4]]
    ps=[0 for i in range(n)]

    for i in range(n):
        if i == 0:
            ps[i]=arr[i]
        else:
            ps[i]= ps[i-1] + arr[i]
    for q in queries:
        si=q[0]
        ei=q[1]
        if si ==0:
            print(ps[ei],end=" ")
        else:
            print(ps[ei]-ps[si-1],end=" ")
main()
 