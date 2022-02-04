n=(input())
k=0
for x in n:
    k=k+ord(x)
if (int(k)>300):
    print("It is tasty!")
else:
    print("Oh, no!")