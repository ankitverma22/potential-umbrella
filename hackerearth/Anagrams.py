# hackerearth anagram
# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/anagrams-651/

if __name__ == "__main__":
    t = int (input())
    for i in range(t):
        s1 = input()
        s2 = input()

        map1 = {}

        map1.get('c',0)
        map2 = {}

        for j in range(len(s1)):
            map1[s1[j]] = map1.get(s1[j],0) + 1

        for j in range(len(s2)):
            map2[s2[j]] = map2.get(s2[j],0) + 1

        combined_string = s1+s2
        unique_chars = list(set(combined_string))

        min_char_to_delete = 0
        for c in unique_chars:
            min_char_to_delete += abs(map1.get(c,0) - map2.get(c,0))

        print(min_char_to_delete)