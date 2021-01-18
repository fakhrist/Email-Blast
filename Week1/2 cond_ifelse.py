a = 220
b = 33
c = 250

if b > a :
    print("B lebih besar dari A")
elif a == b :
    print("B sama dengan A")
elif b < a and c < a:
    print("A lebih besar dari B & c")
elif not(b < a and c > a):
    print("A lebih besar dari B, namun tidak dengan c")
else :
    print("Hayooo ngerti ga")