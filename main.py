from sanstem import SanskritStemmer

stemmer = SanskritStemmer()

inflected_noun = "गजेन"
stemmed_noun = stemmer.noun_stem(inflected_noun)
print(stemmed_noun)
