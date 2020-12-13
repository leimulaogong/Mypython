s = input()
t = ""
for ch in s:
    if 'a'<=ch<='z':
        t +=chr(ord('a')+((ord(ch)-ord('a')+3) % 26))
    elif 'A'<=ch<='Z':
        t +=chr(ord('A')+((ord(ch)-ord('A')+3) % 26))
    else:
        t += ch
print(t)
