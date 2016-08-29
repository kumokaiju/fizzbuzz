n=1
li=[]
x=input()
if x==0:
    x=100

while n<=x:
  li.append(n)
  n+=1

n=1
while n<=x:
    if n%3==0 and n%5==0:
        li[n-1]="fizzbuzz"
    elif n%5==0:
        li[n-1]="buzz"
    elif n%3==0:
        li[n-1]="fizz"
    print li[n-1]
    n+=1