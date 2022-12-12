# code golfed version (no regrets)
ls = list(map(lambda x:x[:3],open("day02.in").readlines()))
k = lambda c:(lambda d:[d%3,~-d%3][d<87])(~-ord(c))

# part 1
print(sum((lambda b,_,a:-~a+[0,6][~-a%3==b]+3*(a==b))(*map(k,l)) for l in ls))

# part 2
print(sum((lambda a,_,b:-~[~-a%3,3+a,-~a%3+6][b])(*map(k,l)) for l in ls))
