s = input()
s = s + '_'
n = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        n += 1
    else:
        print(s[i] + str(n), end = '')
        n = 1