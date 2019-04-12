# Solution one

def anagram_solution_1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False
        
        while pos2 < len(a_list) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 += 1
            

        if found:
            a_list[pos2] = None
        else:
            still_ok = False
        
        pos1 += 1
    
    return still_ok


# print(anagram_solution_1('george','eorgeg'))


# Solution two

def anagram_solution_2(s1,s2):
    a_list = list(s1)
    b_list = list(s2)

    if len(a_list) == len(b_list):
        a_list.sort()
        b_list.sort()

        pos = 0
        matches = True

        while pos < len(a_list) and matches:
            if a_list[pos] == b_list[pos]:
                pos += 1
            else:
                matches = False

        return "String are anagrams " + str(matches)
    else:
        return "Unequal Strings, we can't proceed"

print(anagram_solution_2('george','eoogeg'))