# dao nguoc chuoi bang de quy
def revert(input_string):
    if len(input_string) == 1:
        return input_string
    return revert(input_string[1:]) + input_string[0]

# kiem tra chuoi anagram


def are_anagrams(str1, str2):
    char1_dict = {}
    char2_dict = {}
    for c in str1:
        char1_dict[c] = char1_dict.get(c, 0) + 1

    for c in str2:
        char2_dict[c] = char2_dict.get(c, 0) + 1
    return char1_dict == char2_dict

# kiem tra chuoi palindrome


def is_palindrome(input_string):
    left = 0
    right = len(input_string) - 1
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
    return True

# tim chuoi palindrome dai nhat
# def find_longest_palindrome(input_string):

# tinh tong 2 so cuc lon


def get_big_numbers_sum(a, b):
    m = len(a)
    n = len(b)
    T = max(m, n)
    res = ""
    flag = 0
    for t in range(T + 1):
        x = m - 1 - t
        y = n - 1 - t
        X = 0
        Y = 0
        if x >= 0:
            X = int(a[x])
        if y >= 0:
            Y = int(b[y])
        ans = X + Y + flag
        if ans > 9:
            ans -= 10
            flag = 1
        else:
            flag = 0
        res = str(ans) + res
    return res

# tim ky tu khong trung lap dau tien


def find_first_non_duplicate(input_string):
    count_dict = {}
    for c in input_string:
        count_dict[c] = count_dict.get(c, 0) + 1
    for idx, c in enumerate(input_string):
        if count_dict[c] == 1:
            return idx
    return -1
