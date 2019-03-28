from nltk.corpus import wordnet

#synonyms of word "program"
syns = wordnet.synsets("program")

#print(syns)
print(syns[0].name())

print (syns[0].lemmas()[0].name())
print(syns[0].definition())
print(syns[0].examples())

# synonyms/antonyms of word "bad"
synonyms = []
antonyms = []
 
for syn in wordnet.synsets("bad"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#find similarity between words
w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("dog.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("animal.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("catch.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("cat.n.01")
w2 = wordnet.synset("kitten.n.01")
print(w1.wup_similarity(w2))



