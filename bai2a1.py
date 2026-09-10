N = int(input())
# TODO: N có phải số chẵn?
print("YES" if N%2==0 else "NO")
# TODO: N vừa chia hết cho 3 vừa chia hết cho 5?
print("YES" if (N%3==0 and N%5==0) else "NO")
# TODO: N chia hết cho 3 nhưng không chia hết cho 7?
print("YES" if (N%3==0 and N%7!=0) else "NO")
# TODO: N chia hết cho 3 hoặc 7?
print("YES" if (N%3==0 or N%7==0) else "NO")
# TODO: N lớn hơn 30 và nhỏ hơn 50?
print("YES" if (N > 30 and N < 50) else "NO")
print("YES" if (N >= 30 and (N%2 == 0 or N%3==0 or N%5==0)) else "NO")
# TODO: N là số có 2 chữ số và chữ số tận cùng là số nguyên tố (2, 3, 5, 7)?
print("YES" if ((N >= 10 and N<=99) and (N%10 == 2 or N%10 == 3 or N%10==5 or N%10==7)) else "NO")
print("YES" if N <= 100 and N % 23 == 0 else "NO")
# TODO: N không thuộc đoạn [10, 20]?
print("YES" if (N < 10 or N > 20) else "NO")
# TODO: Chữ số tận cùng là bội số của 3 (0, 3, 6, 9)?
print("YES" if (N%10)%3 ==0 else "NO")
