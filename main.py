from sanstem import SanskritStemmer

stemmer = SanskritStemmer()

inflected_nouns = ["रामेण", "गुरुणा", "सीतायाम्", "भवता", "हरिषु"]

for noun in inflected_nouns:

    stemmed_noun = stemmer.noun_stem(noun)

    print(noun, stemmed_noun, sep=" --> ")
