def anagramCheck(s1, s2):
    dict1 = {}
    dict2 = {}
    for i in s1:
        dict1[i] = dict1.get(i, 0) + 1

    for i in s2:
        dict2[i] = dict2.get(i, 0) + 1

    if dict1 == dict2:
        print("Anagram!")
    else:
        print("Not an Anagram!")


anagramCheck("apple", "elppa")
