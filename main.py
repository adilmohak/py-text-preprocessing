from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

msg = """
    internationalization Hello Mr Abebe ,how are doing to day? 
    I think it is fine. The weather is  great and the teaching is stil contunied.
"""

print("sent_tokenize", sent_tokenize(msg))
print("word_tokenize", word_tokenize(msg))

# for i in word_tokenize(msg):
#     print(i)

# for i in sent_tokenize(msg):
#     print(i)

stop_words = set(stopwords.words("english"))
print(stop_words)
words = word_tokenize(msg)

filter_sentence = []

for w in words:
    if w not in stop_words:
        filter_sentence.append(w)
print("filter_sentence:", filter_sentence)

# msg2 = ["ptyhon","pythoner","pythoning","pythoed"]
stem_words = []
ps = PorterStemmer()
for w in msg:
    stem_words.append(f"{w}: {ps.stem(w)}")

print("stem_words:", stem_words)
