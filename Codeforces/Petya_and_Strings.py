'''
    Problem Statement : Petya and Strings
    Link : https://codeforces.com/problemset/problem/112/A
    score : accepted
'''
string1 = input().lower()
string2 = input().lower()
if string1 < string2:
    print('-1')
elif string2 < string1:
    print('1')
else:
    print('0')

