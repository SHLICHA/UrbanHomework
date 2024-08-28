def all_variants(text):
    l = 1
    while l != len(text) + 1:
        for j in range(len(text)):
            if j + l <= len(text):
                yield text[j:j + l]
        l += 1


a = all_variants('abc')
for i in a:
    print(i)