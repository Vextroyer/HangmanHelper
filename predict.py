#Given a corpus of spanish words and a word with some letters known and others unknown
#give a suggestion about the next letter.

import json
import sys

word_list = []
with open("index.json") as index:
    word_list = json.load(index)

query = sys.argv[1] #The word to query about.
length = len(query)
objective = 0 # The amount of known letters on the query
for i in range(0,length):
    if query[i] == "_":
        objective = objective + 1
objective = length - objective

#Get every word matching length of query and matching letters with query
candidates = []
for word in word_list:
    if len(word) == length:
        matches = 0
        for i in range(0,length):
            if query[i] == word[i]:
                matches = matches + 1
        if matches == objective:
            candidates.append(word)

# Print candidates if there are a few
if len(candidates) <= 10:
    print(candidates)


# Print for each letter on a candidate and not in the query print the proportion
# wich represents.
frequencies = {}
total_frequency = 0
for word in candidates:
    for l in word:
        if l in query:
            continue
        if l in frequencies.keys():
            frequencies[l] = frequencies[l] + 1
        else:
            frequencies[l] = 1
        total_frequency = total_frequency + 1
for key in frequencies.keys():
    print(f"{key} ~ {(frequencies[key] / total_frequency) * 100}")