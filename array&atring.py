def isPairexist(arr,target):
    arr.sort()
    i,j=0,len(arr)-1
    while i<j:
        if arr[i]+arr[j] == target: return True
        if arr[i]+arr[j] > target: j-=1
        if arr[i]+arr[j]< target: i+=1
    return False

def main():
    arr=[3,-2,5,6,9,13,5,-12,8]
    target=14
    ans=isPairexist(arr,target)
    print(ans)
main()