"""
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i2 . 
Example
n = 3 
The list of non-negative integers that are less than n = 3 is [ 0, 1, 2 ]. Print the square of each number on a separate line.
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(0, n):
        print(i ** 2)

"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.

In the Gregorian calendar, three conditions are used to identify leap years:

The year can be evenly divided by 4, is a leap year, unless:
The year can be evenly divided by 100, it is NOT a leap year, unless:
The year is also evenly divisible by 400. Then it is a leap year.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. 

Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.
"""
def is_leap(year):
    leap = False
    
    # Write your logic here
    if (year % 400 == 0):
        return True
    if (year % 100 == 0):
        return leap
    if (year % 4 == 0):
        return True
    else:
        return False  
    
    return leap

year = int(input())
print(is_leap(year))

"""
The included code stub will read an integer, n, from STDIN.

Without using any strings methods, try to print the following:

123……..n

Note that “…..” represents the consecutive values in between.

Example

n = 5
Print the string 12345.
"""

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end="")

"""
You are given a string, and you have to validate whether it’s a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input Format
A single line of input containing a string of Roman characters.

Output Format
Output a single line containing True or False according to the instructions above.

Constraints
The number will be between 1 and 3999 (both included).
"""
regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'    # Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))

"""
Let’s dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a  or .

Concept

A valid mobile number is a ten digit number starting with a  or .

Regular expressions are a key concept in any programming language.

Input Format
The first line contains an integer N, the number of inputs.
N lines follow, each containing some string.

Constraints
1 <= N <= 10
2 <= len(Number) <= 15
Output Format
For every string listed, print “YES” if it is a valid mobile number and “NO” if it is not on separate lines. Do not print the quotes.
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]