def fun(n):
    if (n<=2):
        return
    fun(n-2)
    print(n)
fun(89)