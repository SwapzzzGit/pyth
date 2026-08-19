"""
Write word_count(text) that returns how many words are in a string. 
Call it three times with different sentences.
"""

sen1 = "what you had before  that's the point. Same result, but now each step is a named tool you can reuse and test separately."
sen2 = "that's the early return style, and it's everywhere in real code."
sen3 = "ends the function immediately. Lines after it never run."

def word_count(text):
    clean = text.split()
    print(clean)
    return len(clean)

print(word_count(sen1))
print(word_count(sen2))
print(word_count(sen3))

"""
Dict from a function. 
Write describe(text) that returns a dict with three keys: 
chars, words, lines. Call it on some text and print result["words"].
"""
def describe(text):
    result = {
        "char":len(text),
        "words":len(text.split()),
        "lines":len(text.splitlines()),
    }
    return result

text = """Hello, how are you?
I am learning Python.
This is practice."""

result = describe(text)

print(result)
print(result['words'])




