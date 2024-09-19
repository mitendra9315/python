def isValid(s):
    st=[]
    for i in range (len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[':
            st.append(s[i])
        elif s[i] == ')' and s[-1]!= '(' : return False
        elif s[i] == '}' and s[-1]!= '{' : return False
        elif s[i] == ']' and s[-1]!= '[' : return False
        else:
            st.pop(s[i])
    return len(st) == 0

def main():
    s="[{(})}]"
    ans= print(isValid(s))
    
main()
