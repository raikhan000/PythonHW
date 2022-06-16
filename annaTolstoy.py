import sys
import random
def make_text():
    text = sys.stdin.read().replace("\n    ", " ** ").split()
    length = len(text)
    random_number = random.randint(0, length)
    ans = " ".join(text[random_number:random_number + L])
    return ans.replace(" ** ", "\n    ")

L = int(input())
print(make_text())



