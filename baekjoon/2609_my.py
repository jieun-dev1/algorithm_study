#최대 공약수
#name error = value error 가 뜸.
#아래와 같이하면 name이나 value 에러로 런타임에러다.
# a = int(input())
# b = int(input())

a, b = input().split()
a = int(a)
b = int(b)
# a = 24
# b = 16


def gcd(a,b):
    while b > 0:
        a,b = b, a % b
    return a

def lcm(a,b):
    return a*b//gcd(a,b)

print(gcd(a,b))
print(lcm(a,b))
