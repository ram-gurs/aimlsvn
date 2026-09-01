# -*- coding: utf-8 -*-
def is_palindrome(s: str) -> bool:
    return s == s[::-1]
print(is_palindrome("racecar"))

#def is_palindrome(s:str) -> bool:
s='racecars'
if s == s[::-1]:
  print("Palindrome")
else:
  print("Not a palindrome")

def is_palindrome(s1: str) -> bool:
  s1 = s1[::-1]
  return True if s1 == s1 else False
print(is_palindrome("racecar"))

# FIND  FREQ OF THE EACH CHAR IN THAT STRING
def find_freq(st:str):
  freq = {}
  for ch in st:
    freq[ch] = freq.get(ch,0)+1

  return freq

print(find_freq('xxvvvdddf'))

# FIND MAX FREQ OF THE CHAR IN THAT STRING

def find_maxfreq(st : str):
  max_freq = {}
  for ch in st:
    max_freq[ch] = max_freq.get(ch,0)+1
  return max(max_freq, key=max_freq.get)
print(find_maxfreq('xxvvvdddf'))

# FIND  FREQ OF THE SPECIFIC CHAR IN THAT STRING
def find_spec_char(st : str, ch :str):
  spec_char = {}
  for ch in st:
    spec_char[ch] = spec_char.get(ch,0)+1
  return spec_char
print(find_spec_char(st='xxxddf', ch='x'))

# DEFINE A GIVEN STRING IS_PALINDROME
def is_palindromic_string(st : str) -> bool:
   return True if st == st else False
print(is_palindromic_string('racecar'))

# FIND THE LONGEST PALINDROME IN A STRING
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2:
            return s

        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left+1:right]

        longest = ""

        for i in range(len(s)):
            # Odd-length palindrome
            p1 = expand(i, i)
            # Even-length palindrome
            p2 = expand(i, i+1)

            longest = max(longest, p1, p2, key=len)

        return longest
sol = Solution()
s = "babad"
print(sol.longestPalindrome(s))