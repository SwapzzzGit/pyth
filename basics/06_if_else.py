text = """Python is a popular programming language. It is easy to learn and widely used
for web development, data science, artificial intelligence, automation, and many other
areas. Python provides many built-in functions, and libraries that make programming.
"""

chars = len(text)

if chars < 100:
    print("tiny")
elif chars <= 250:
    print("huge")