# --- Day 4: Secure Container ---
# You arrive at the Venus fuel depot only to discover it's protected by a password. The Elves had written the password on a sticky note, but someone threw it out.

# However, they do remember a few key facts about the password:

# It is a six-digit number.
# The value is within the range given in your puzzle input.
# Two adjacent digits are the same (like 22 in 122345).
# Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
# Other than the range rule, the following are true:

# 111111 meets these criteria (double 11, never decreases).
# 223450 does not meet these criteria (decreasing pair of digits 50).
# 123789 does not meet these criteria (no double).
# How many different passwords within the range given in your puzzle input meet these criteria?

# Your puzzle input is 359282-820401.

import re

def main():
    passwords = list()

    for num in range(359282, 820402):
        add = True
        for i, digit in enumerate(str(num)[1:]): #check that number never decreases
            if int(digit) < int(str(num)[i]):
                add = False
                break
        if re.search(r"(?:^|(.)(?!\1))(\d)\2(?!\2)", str(num))== None: #check for {2} repeating adjacent digits using regex \b backreference
            add = False
        
        if add:
            passwords.append(num)

    print(len(passwords))



if __name__ == "__main__":
    main()
