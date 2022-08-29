w = input("Enter Any Word Or Number Or Any Special Characters : ")
vowel = ['a', 'e', 'i', 'o', 'u']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
sc = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '+', '_', '=', ';', ':', '"', "'", '|', ',', '.', '<', '>', '/', '?']
cb = ['{', '}']
b = ['(', ')']
sb = ['[', ']']
i = 0
c = 0
v = 0
s = 0
n = 0
scv = 0
cbv = 0
bv = 0
sbv = 0
while i < len(w):
    if w[i] != ' ':
        if w[i] not in vowel and w[i] not in num and w[i] not in sc and w[i] not in b and w[i] not in sb and w[i] not in cb:
            c += 1
        elif w[i] in vowel:
            v += 1
        elif w[i] in num:
            n += 1
        elif w[i] in sc:
            scv += 1
        elif w[i] in b:
            bv += 1
        elif w[i] in sb:
            sbv += 1
        elif w[i] in cb:
            cbv += 1
    else:
        s += 1
    i += 1
print(f"There Are {i - s} Letters And {s} Spaces In {w}")
print(f"There Are {c} Consonants In {w}")
print(f"There Are {v} Vowels In {w}")
print(f"There Are {n} Numbers In {w}")
print(f"There Are {scv} Special Characters In {w}")
print(f"There Are {bv} Brackets In {w}")
print(f"There Are {sbv} Square Brackets In {w}")
print(f"There Are {cbv} Curly Brackets In {w}")
