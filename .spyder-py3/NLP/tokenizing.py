from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem  import PorterStemmer

ps = PorterStemmer()
text_example = """Diverse and impactful on a number of fronts, CruzHacks 2019 was a success. 
                From January 18 to January 20, 2019, UCSC’s Stevenson Event Center was transformed into a bustling playground for our 
                diverse group of over 600 hackers to turn their visions for social change into tangible projects. 
                The 36 hours of hacking were as hectic as they were productive. As hackers downed bottle after 
                bottle of Yerba Mate and Soylent, mentors and your representatives were available to advise teams 
                on their project ideas and work out any challenges they encountered along the way."""

# =============================================================================
# Tokenize
# =============================================================================

#print(sent_tokenize(text_example)) #sentences list
#print(word_tokenize(text_example))  #words list

# for i in word_tokenize(text_example):
#     print(i)

# =============================================================================
# #Remove stop words              
# =============================================================================

stop_words = set(stopwords.words("english"))

words = word_tokenize(text_example)
filtered_text = []

for w in words:
    if w not in stop_words:
        filtered_text.append(w)
        
print(filtered_text)

# =============================================================================
# Stemming
# =============================================================================
for w in words:
    print(ps.stem(w))


# =============================================================================
# Part of Speech tagging
    #creates tuples of word & POS
# =============================================================================
sent = sent_tokenize(text_example)

#def process_content():
#    try:
#        for i in sent:
#            words = nltk.word_tokenize(i)
#            tagged = nltk.pos_tag(words)
#            print(tagged)
#    except Exception as e:
#            print(str(e))
#process_content()

# =============================================================================
# Chunking using POS tags & regular expression
# =============================================================================
def process_content():
    try:
        for i in sent:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP><NN>?}"""
            
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            
            #print(chunked)
            chunked.draw()
            
    except Exception as e:
        print(str(e))

process_content()
