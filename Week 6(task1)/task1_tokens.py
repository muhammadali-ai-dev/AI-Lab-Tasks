import re
samples = ["AI, search!", "I can't log in.", "help@example.com",
"یہ ایک مثال ہے" ,"" ,"2.1 version 4944CS "]
for text in samples:
 ws = text.split()
 words = re.findall(r"\b\w+\b", text, flags=re.UNICODE)
 print(repr(text), "whitespace:", ws, len(ws))
 print("word-like:", words, len(words))
assert re.findall(r"\b\w+\b", "") == []
