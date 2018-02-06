m = int(input("Enter Larger Number"))
n = int(input("Enter Smaller Number"))

def gcd(m,n):
    if m < n:
        (m,n) = (n,m)
    else:
        while (m%n) !=0:
            (m,n) = (n , m%n)

    return(n)

print("Gratest Common Factor is : ")
print(gcd(m,n))