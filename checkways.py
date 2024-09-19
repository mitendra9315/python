def checkways(n,dp):
    if dp[n-1]!=0:
        return dp[n]
    if n<=3:
        return n
    a1= checkways(n-1,dp)
    dp[n-1]=a1
    a2= checkways(n-2,dp)
    dp[n-2]=a2
    return a1+a2

def main():
    n=5
    dp=[0 for i in range(n+1)]
    print(checkways(n,dp))
main()
     
