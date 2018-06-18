#https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/two-strings-4/

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        s1 = input()
        s2 = input()

        map1 = {}
        map2 = {}

        if(len(s1) == len(s2)):

            for j in range(len(s1)):
                map1[s1[j]] = map1.get(s1[j],0)+1
            for k in range(len(s2)):
                map2[s2[k]] = map2.get(s2[k],0)+1
            if(map1 ==map2):
                print("yes")
            else:
                print("No")

