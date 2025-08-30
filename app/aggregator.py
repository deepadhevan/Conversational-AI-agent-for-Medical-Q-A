from collections import Counter

def aggregate(answers):
    most_common = Counter(answers).most_common(1)
    return most_common[0][0] if most_common else answers[0]
