import sys

s = sys.argv[1]

print("#1", s[2])
print("#2", s[4])
print("#3", len(s))
print("#4", s[0])
print("#5", s[-1])
print("#6", s[-2])
print("#7", s[3:8])
print("#8", s[-5:-1] + s[-1])
print("#9", s[2:])
print("#10", s[::2])
print("#11", s[1::3])
print("#12", s[::-1])
print("#13", s.find(' '))
print("#14", s[:-1])
print("#15", s[1:])
print("#16", s.lower())
print("#17", s.split())
print("#18", len(s.split()))
print("#19", [char for char in s])
print("#20", ''.join(sorted([ch for ch in s])))
print("#21", s if s.find(' ') == -1 else s[:s.find(' ')])
print("#22", s == s[::-1])
