print("nhap van ban(nhap 'dont' ket thuc):")
lines = []
while True:
    line = input()
    if line.lower() == "dont":
        break
    lines.append(line)
print("\n chu in hoa:")
for line in lines:
    print(line.upper())
    