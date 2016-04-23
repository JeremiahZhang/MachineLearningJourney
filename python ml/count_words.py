"""Count words."""

def count_words(s, n):

    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s

    words_list = s.split()
    unique_word_set = set(words_list)
    freq = {}
    for word in unique_word_set:
        freq[word] = words_list.count(word)

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    words_freq_pair = freq.items()
    words_freq_pair.sort(key=lambda pair: (-pair[1], pair[0]))
    # select the first n words_and freqruence pair
    top_n = words_freq_pair[:n]
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat zion", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    test_run()

# reference thanks
'''http://codereview.stackexchange.com/questions/118914/word-frequency-counter'''