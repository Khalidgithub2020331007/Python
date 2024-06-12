text = "Hello, world!"
replacements = {'H': 'h', 'w': 'W', '!': '.'}

for old, new in replacements.items():
    text = text.replace(old, new)

print(text)
