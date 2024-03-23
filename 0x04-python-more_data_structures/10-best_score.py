#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = 0
    best_score_key = None

    for key, value in a_dictionary.items():
        if value > max_score:
            max_score = value
            best_score_key = key
    return best_score_key
