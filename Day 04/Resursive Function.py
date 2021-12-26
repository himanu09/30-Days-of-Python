# Resursive Function

def num(a):
    if a==0 or a==1:
        return 1
    return a+(a-1)
s=num(10)
print(s)