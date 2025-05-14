###
### PROBLEM STATEMENT
###
"""
Rating: 1949

Given two strings str1 and str2 of the same length, determine whether you can transform str1 into str2 by doing zero or more conversions.

In one conversion you can convert all occurrences of one character in str1 to any other lowercase English character.

Return true if and only if you can transform str1 into str2.


Example 1:

Input: str1 = "aabcc", str2 = "ccdee"
Output: true
Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that the order of conversions matter.

Example 2:

Input: str1 = "leetcode", str2 = "codeleet"
Output: false
Explanation: There is no way to transform str1 to str2.
 

Constraints:

1 <= str1.length == str2.length <= 10^4
str1 and str2 contain only lowercase English letters.

"""



###
### APPROACH
###
""" 

For this type of question, the more you think through examples, the more clear the question becomes.

Furthermore, it is important to note that you are converting str1 to str2 and don't have to worry about conversions the other way.

The crux of the problem is that each character in str1 must map to a singular character in str2. In fact, you could have a surjective mapping.



Base Case: if strings already equal, just return True.

Then, count the number of unique characters in both strings. If there are less unique characters in str1 than str2, then we know a bijective/surjective mapping is not possible.

Afterwards, we can check if there exists a mapping between each character in str1 to a unique character in str2.

The final condition was something I thought of immeditaly, but may not be obvious at first.

Essentially, you need to have a 'spare character' when you are transforming characters.

Take a look at the first example, if you directly converted 'aa' to 'cc', then when we convert the c's to e's, then we would have 'eedee' as the converted string, which is incorrect.

Therefore, we need to have some intermediary value for 'a' to convert to such that we do not have collisions.

There will always be a intermediary value as long as there exists a value that is not in our mapping.

If this doesn't seem intutive, I would suggest writing out examples.

"""

def canConvert(str1, str2):
  if str1 == str2:
    return True

  c1 = Counter(str1)
  c2 = Counter(str2)
  if len(c1) < len(c2):
      return False

  mapping = {}

  for char in range(len(str1)):
    if str1[char] not in mapping:
      mapping[str1[char]] = str2[char]
    elif mapping[str1[char]] != str2[char]:
      return False

  if len(set(mapping.values())) == 26:
    return False

  return True
