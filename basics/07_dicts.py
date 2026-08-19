"""
Word frequency. Take a sentence, split it into words, 
and use the counting pattern to build a dict of how often each word appears. Print it.

"""
sentence = "the cat sat on the mat and the cat was happy"

words = sentence.split()
print(words)

patterns = {}

for word in words:
    if word in patterns:
        patterns[word] += 1
    else:
        patterns[word] = 1

print(patterns)

"""
Safe reads. Make a dict with three keys. Try reading a fourth key with [] and 
read the error name. Then do it again with .get() and with .get(key, "missing").

"""

my_dict = {
    "one": 1,
    "two": 2,
    "three": 3,
}

#print(my_dict["four"])          
print(my_dict.get("four"))           
print(my_dict.get("four", "missing")) 




