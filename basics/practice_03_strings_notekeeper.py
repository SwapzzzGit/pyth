
raw_text = "   Python is Great.   Python is EASY to learn   "

print("----BEFORE----")
print(raw_text)

clean_text = raw_text.strip().lower()

print("----AFTER----")
print(clean_text)
print(len(clean_text))

print("-----Reports-----")
print(f"mentioned python : {'Python' in raw_text}")
print(f"times python appears : {raw_text.lower().count("python")}")
print(f"characters removed : {len(raw_text) - len(clean_text)}")


title = "  my study notes  "

print(title.strip().upper())

print(clean_text.replace("python","[LANG]"))

print(f"First character : {clean_text[0]} and last character : {clean_text[-1]}.")

print(len)
#print(raw_text.strip(5))