from textblob import TextBlob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

#print(blob.sentences)

#print(blob.words)

#print(blob.tags)

#print(blob.noun_phrases)

#print(round(blob.sentiment.polarity,3))
#print(round(blob.sentiment.subjectivity,3))

#for sentence in blob.sentences:
    #print(sentence)
    #print(round(sentence.sentiment.polarity,3))




from textblob.sentiments import NaiveBayesAnalyzer

blob = TextBlob(text, analyzer=NaiveBayesAnalyzer())

#print(blob.sentiment)

#for sentence in blob.sentences:
  #  print(sentence.sentiment)

spanish = blob.translate(to='es')
chinese = blob.translate(to = 'zh')

#print(spanish)

#print(chinese)

#print(chinese.translate())

#change word types
from textblob import  Word

index = Word('index')

#print(index.pluralize())

cacti = Word('Cacti')

#print(cacti.singularize())

#wordlist
animals = TextBlob('dog cat fish bird').words

#print(animals.pluralize())

#spellcheck and correction
word = Word('theyr')

#print(word.spellcheck())

#use correct() to use word with the highest confidence level
#print(word.correct())

#normalization
word1 = Word('studies')
word2 = Word('varieties')

#stem takes off popular endings, in this case 'es'
#print(word1.stem())
#print(word2.stem())

#lemmatize gives singular version of word
#print(word1.lemmatize())
#print(word2.lemmatize())

#definitions, synonyms, antonyms

happy = Word("happy")

print(happy.definitions)

print(happy.synsets)

#extract words from synsets
for s in happy.synsets:
  for l in s.lemmas():
    print(l.name())

synonym = happy.synsets[1].lemmas()[0].name()
print(synonym)

antonym = happy.synsets[0].lemmas()[0].antonyms()[0].name()
print(antonym)