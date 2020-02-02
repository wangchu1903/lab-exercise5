
def isPalRec(st, s, e):
    if (s == e):
        return True

    if (st[s] != st[e]):
        return False


    if (s < e + 1):
        return isPalRec(st, s + 1, e - 1)

    return True


def isPalindrome(st):
    n = len(st)

    if (n == 0):
        return True

    return isPalRec(st, 0, n - 1)

num = 12321
if isPalindrome(str(num)):
    print("Yes")
else :
    print("No")