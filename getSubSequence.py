def getSubSequence(arr,index=0,currAns=[]):
    if len(arr) == index:
        print(currAns)
        return
    getSubSequence(arr,index+1,currAns)
    getSubSequence(arr,index+1,currAns+[arr[index]])


def main():
    arr = [1,2,3]
    getSubSequence(arr,0,[])
main()