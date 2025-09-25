text = "banana" 
keys = []
values = []
for char in text:
    if char not in keys:
        keys.append(char)
        values.append(text.count(char))

result = dict(zip(keys, values))
print(result)
