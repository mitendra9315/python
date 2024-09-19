def checkPalindrome(str):
    if len(str)<=1:
        return True
    if str[0]!=str[-1]: 
        return False
    return checkPalindrome(str[1:len(str)-1])
print(checkPalindrome("miten"))