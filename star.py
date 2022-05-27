# 별찍기 - 크리스마스 트리 - Python

n = int(input())
for i in range(n):
    print(' '*(n-i-1) + '*'*(2*i+1))
'''          
print(' ' * (n-1) + '*' * 1 )
print(' ' * (n-2) + '*' * 3 )
print(' ' * (n-3) + '*' * 5 )
print(' ' * (n-4) + '*' * 7 )
print(' ' * (n-1) + '*' * 9 )
'''
