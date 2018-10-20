##https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/sum-it-if-you-can-4867f851/


a = int(input())
sum = 0
if len(str(abs(a))) == 10:
    s = [int(x) for x in str(a)]
    for i in range(1,11):
        sum = sum + s[i-1]*i
        f = sum % 11
    if f == 0:
        print("Legal ISBN")
    else:
        print("Illegal ISBN")
else:
    print("Illegal ISBN")