# https://leetcode.com/problems/substring-with-concatenation-of-all-words
"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
Example 1:

Input: s = "barfoothefoobarman", words = ["foo","bar"]

Output: [0,9]

Explanation:

The substring starting at 0 is "barfoo". It is the concatenation of ["bar","foo"] which is a permutation of words.
The substring starting at 9 is "foobar". It is the concatenation of ["foo","bar"] which is a permutation of words.

Example 2:

Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"]

Output: []

Explanation:

There is no concatenated substring.

Example 3:

Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"]

Output: [6,9,12]

Explanation:

The substring starting at 6 is "foobarthe". It is the concatenation of ["foo","bar","the"].
The substring starting at 9 is "barthefoo". It is the concatenation of ["bar","the","foo"].
The substring starting at 12 is "thefoobar". It is the concatenation of ["the","foo","bar"].

Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.
"""
from typing import List
from collections import defaultdict, Counter


class Solution:
    # def backtrack(
    #     self,
    #     words: List[str],
    #     ans: set,
    #     tmp: str,
    #     remained: defaultdict,
    #     curIdx: int,
    # ):
    #     if curIdx >= len(words):
    #         ans.add(tmp)
    #         return
    #     for (w, remain) in remained.items():
    #         if remain > 0:
    #             tmp += w
    #             remained[w] -= 1
    #             self.backtrack(words, ans, tmp, remained, curIdx + 1)
    #             remained[w] += 1
    #             tmp = tmp[:-len(w)]

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        ans = []
        word_counts = Counter(words)
        word_len = len(words[0])
        total_len = len(words[0]) * len(words)
        for start in range(len(s) - total_len + 1):
            isMatch = True
            seen = defaultdict(int)
            for i in range(start, start + total_len - word_len + 1, word_len):
                window = s[i:i+word_len]
                if word_counts[window] > 0:
                    seen[window] += 1
                    if seen[window] > word_counts[window]:
                        isMatch = False
                        break
                else:
                    isMatch = False
                    break
            if isMatch:
                ans.append(start)
        return ans


s = "barfoothefoobarman"
words = ["foo","bar"]
sol = Solution()
ans = sol.findSubstring(s, words)
print(ans)
