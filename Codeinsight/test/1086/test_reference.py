import collections

def test(str0):
    char_count = collections.defaultdict(int)
    max_count = 0
    most_frequent_char = None

    for char in str0:
        char_count[char] += 1
        if char_count[char] > max_count:
            max_count = char_count[char]
            most_frequent_char = char

    return most_frequent_char, max_count

