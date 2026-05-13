def isAnagram( s, t):
        
        lists=list(t)
        for letters in s:
            if letters in lists:
                lists.remove(letters)
            else:
                return False
        if lists==[]:
            return True


s=input("What's s?")
t=input("What's t?")
print(isAnagram(s,t))