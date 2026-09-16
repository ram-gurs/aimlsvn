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

def find_maxfreq(stv : str):
  max_freq = {}
  for ch in stv:
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
s = "ASSAANNNA"
print(sol.longestPalindrome(s))


#Zigzag Conversion — Python Code Analysis
def zigzag_conversion(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)

# Reverse Integer
def reverse_integer(x: int) -> int:
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = int(str(x)[::-1])
    if reversed_x > 2**31 - 1:
        return 0
    return sign * reversed_x

# String to Integer (atoi)
def string_to_integer(s: str) -> int:
    s = s.strip()
    if not s:
        return 0

    sign = 1
    if s[0] in ['-', '+']:
        sign = -1 if s[0] == '-' else 1
        s = s[1:]

    result = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break

    result *= sign
    if result < -2**31:
        return -2**31
    if result > 2**31 - 1:
        return 2**31 - 1

    return result

# Palindrome Number
def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    if x == 0:
        return True
    s = str(x)
    return s == s[::-1]

# REGEX Regular Expression Matching
def isMatch(s: str, p: str) -> bool:
    memo = {}

    def dp(i, j):
        if (i, j) in memo:
            return memo[(i, j)]

        # If pattern is exhausted
        if j == len(p):
            return i == len(s)

        # First character match?
        first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

        # Handle '*' (zero or more of preceding element)
        if j + 1 < len(p) and p[j + 1] == '*':
            memo[(i, j)] = (
                dp(i, j + 2) or                # skip "x*" entirely
                (first_match and dp(i + 1, j)) # use one occurrence of x
            )
        else:
            memo[(i, j)] = first_match and dp(i + 1, j + 1)

        return memo[(i, j)]

    return dp(0, 0)
