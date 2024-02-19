def isPalindrome(x: int) -> bool:
        stri = str(x)
        if len(stri) == 1:
            return True
        for  idx in range(len(stri)//2):
            #print(char, idx)
            if stri[idx] != stri[len(stri) - idx - 1]:
                return False
        return True

def isPalindrome_fast(x: int) -> bool:
    return str(x) == str(x)[::-1]

isPalindrome_fast(1000021)