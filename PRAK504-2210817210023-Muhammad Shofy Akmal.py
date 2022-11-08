def reverse (A) :
    C = 0
    while int(A) != 0 :
        sisa = int(A) % 10
        C = C * 10 + sisa
        A = int(A) / 10
    return C
A, B = input().split()
A = reverse(A)
B = reverse(B)
C = A + B
print(reverse(C))