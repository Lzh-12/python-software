brides = ['X', 'Y', 'Z']

for a in brides:
    for b in brides:
        for c in brides:
            if (a != 'X' and c != 'X' and c != 'Z') and (a != b and a != c and b != c):
                print(f"新郎A和{a}结婚")
                print(f"新郎B和{b}结婚")
                print(f"新郎C和{c}结婚")
                break
