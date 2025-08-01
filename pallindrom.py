def is_paali(s:str) -> bool:
    return s==s[::-1]

def pallindrome (words):
    word_ind = {word: i for i, word in enumerate(words)}
    count = 0 

    for i, word in enumerate(words):
        for cut in range (len(word)+1):
            pref = word[:cut]
            suff = word[cut:]

            if is_paali(pref):
                rev_suff = suff[::-1]
                if rev_suff in word_ind and word_ind[rev_suff] != i:
                    count += 1

            if cut != len(word) and is_paali(suff):
                rev_pref = pref[::-1]
                if rev_pref in word_ind and word_ind[rev_pref] != i:
                    count += 1
    return count

n = int(input())
for i in range (0,n):
    words = input().split()

res = pallindrome(words)
print(res)