
#This is one way of getting n longest unique words

def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)
    longest_words = []

    while len(longest_words) < n:
        current_longest = ''
        for word in words:
            if len(word) > len(current_longest):
                current_longest = word

        unique_words.remove(current_longest)
        longest_words.append(current_longest)

def get_unique_words(words):
    unique_words = []
    for word in words:
        if words.count(word) == 1:
            unique_words.append(word)

    return unique_words

#OR IN A SIMPLEST WAY
def get_n_longest_unique_words(words, n):
    unique_words = get_unique_words(words)

    sorted_words = sorted(unique_words, key=len, reverse=True)

    return sorted_words[:n]
