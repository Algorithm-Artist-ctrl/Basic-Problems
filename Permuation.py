import itertools
s = input("Enter a string: ")
perms = itertools.permutations(s)
print("Permutations are:")
for p in perms:
    print("".join(p))
