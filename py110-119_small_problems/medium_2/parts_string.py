def parts(string):
     return [ s[n:] for n, s in enumerate(string) ]

word = 'Sesquipedalianism'
print(parts(word))  # ['S', 'Se', 'Ses', 'Sesq', 'Sesqu', 'Sesqui', 'Sesquip', 'Sesquipe', ...]
