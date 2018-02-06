#Quiz Week 1 complete

def f(x):
  d=0
  while x > 1:
    (x,d) = (x/2,d+1)
  return(d)

print(f(31415927))


def h(m,n):
  ans = 1
  while (n > 0):
    (ans,n) = (ans*m,n-2)
  return(ans)

print(h(6,8))


def h(n):
  f = 0
  for i in range(1,n+1):
    if n%i == 0:
      f = f + 1
  return(f == 2)

print(h(121))


def f(m):
  if m == 0:
    return(1)
  else:
    return(m*f(m-1))
print(f(10))