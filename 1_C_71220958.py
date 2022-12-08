def reverse(ab):
    str = ""
    for i in ab:
        str = i + str
    return str

ab = str(input("masukan kata atau angka : "))
print (reverse(ab))