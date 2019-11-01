"""
Problem: sWAP cASE
https://www.hackerrank.com/challenges/swap-case/problem
"""

def swap_case(s: str) -> str:
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)