#A positive integer m is a sum of squares if it can be written as k + l where k > 0, l > 0 and both k and l are perfect squares.
#Write a Python function sumofsquares(m) that takes an integer m returns True if m is a sum of squares and False otherwise.
# (If m is not positive, your function should return False.)
#Here are some examples to show how your function should work.

#>>> sumofsquares(41)
#True
#>>> sumofsquares(30)
#False
#>>> sumofsquares(17)
#True

def sumofsquares(m):
    if m<0:
        return False
    else:
        for i in range(1, int(m**0.5)+1):
            for j in range(1, int(m*0.5)+1):
                ans = i**2 + j**2
                if ans == m:
                    return True
                elif ans>m:
                    break
        return False
print(sumofsquares(41))


#A string with parentheses is well bracketed if all parentheses are matched:
# every opening bracket has a matching closing bracket and vice versa.
#Write a Python function wellbracketed(s) that takes a string s containing parentheses
#  and returns True if s is well bracketed and False otherwise.
#Hint: Keep track of the nesting depth of brackets.
# Initially the depth is 0. The depth increases with each opening bracket and decreases with each closing bracket.
# What are the constraints on the value of the nesting depth for the string to be wellbracketed?
#Here are some examples to show how your function should work.

#>>> wellbracketed("22)")
#False
#>>> wellbracketed("(a+b)(a-b)")
#true
#>>> wellbracketed("(a(b+c)-d)((e+f)")
#False

def wellbracketed(s):
    depth = 0
    for i in range(len(s)):
        if s[i] == "(":
            depth += 1
        elif s[i] == ")":
            if depth>0:
                depth -= 1
            else:
                return False
    return depth==0

print(wellbracketed("(a(b+c)-d)((e+f)"))


#A list rotation consists of taking the last element and moving it to the front.
# For instance, if we rotate the list [1,2,3,4,5], we get [5,1,2,3,4].
# If we rotate it again, we get [4,5,1,2,3].
#Write a Python function rotatelist(l,k) that takes a list l and a positive integer k and returns the list l after k rotations.
# If k is not positive, your function should return l unchanged.
# Note that your function should not change l itself, and should return the rotated list.
#Here are some examples to show how your function should work.

#>>> rotatelist([1,2,3,4,5],1)
#[5, 1, 2, 3, 4]
#>>> rotatelist([1,2,3,4,5],3)
#[3, 4, 5, 1, 2]
#>>> rotatelist([1,2,3,4,5],12)
#[4, 5, 1, 2, 3]

def rotatelist(i,k):
    if k<0:
        return i
    else:
        k = k%len(i)
        return i[-k:]+i[:-k]

print(rotatelist([1,2,3,4,5],12))

