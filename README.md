# Diachronic Distribution of Senses - D3.8

This repo allows you to carry out an analysis of the diachronic distribution of senses. To do this please follow these steps:

**1. Download BabelNet and its API**

To download BabelNet and its API please follow the instructions at: https://babelnet.org/login

**2. Disambiguate corpora providing indication of time** 

To perform WSD we make available a state-of-the-art multilingual WSD system (Orlando et al. 2021). To use please follow the instructions provided at: http://nlp.uniroma1.it/amuse-wsd/api-documentation. If you use the WSD system online, which is the simplest way, please follow this example:

Example (online API): 
curl -X 'POST' \
  'http://nlp.uniroma1.it/amuse-wsd/api/model' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '[
  {"text":"The quick brown fox jumps over the lazy dog.", "lang":"EN"},
  {"text":"I walked along the river bank.", "lang":"EN"}
]' 

**3. Extract a sense distribution by clustering specific time periods**

To do this, you can use the Python script extract_sense_distribution.py. Read carefully the comments inside the script.

**4. Extract a sample of different MFS in different time periods**

To this end, you can use the Python script extract_sample_of_different_MFS.py which allows you to extract a sample of senses which show variations in terms of MFS in the considered time periods.

# References

Orlando, R., Conia, S., Brignone, F., Cecconi, F., & Navigli, R. (2021, November). AMuSE-WSD: An all-in-one multilingual system for easy Word Sense Disambiguation. In Proceedings of the 2021 Conference on Empirical Methods in Natural Language Processing: System Demonstrations (pp. 298-307).

