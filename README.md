# Diachronic_distribution_of_senses - D3.8

This repo allows you to carry out an analysis of the diachronic distribution of senses. To do this please follow these steps:

**Download BabelNet and its API**

To download BabelNet and its API please follow the instructions at: https://babelnet.org/login

**Disambiguate corpora providing indication of time** 

To perform WSD we make available a state-of-the-art multilingual WSD system. To use please follow the instructions provided at: http://nlp.uniroma1.it/amuse-wsd/api-documentation.

**Extract a sense distribution by clustering specific time periods**

To do this, you can use the Python script extract_sense_distribution.py. Read carefully the comments inside the script.

**Extract a sample of different MFS in different time periods**

To this end, you can use the Python script extract_sample_of_different_MFS.py which allows you to extract a sample of senses which show variations in terms of MFS in the considered time periods.
