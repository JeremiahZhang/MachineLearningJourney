"""Count words."""

def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    # TODO: Count the number of occurences of each word in s
    words_in_s = s.split()
    dicts = {}
    for w in words_in_s:
        dicts.update({w: words_in_s.count(w)})

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    dicts_word_by_occurence = sorted(dicts, key=dicts.__getitem__, reverse=True)
    top_n = []
    for i in range(n):
        top_n.append((dicts_word_by_occurence[i], dicts[dicts_word_by_occurence[i]]))

    top_n = sorted(top_n, key=lambda tup: (-tup[1], tup[0]))

    # TODO: Return the top n words as a list of tuples (<word>, <count>)

    return top_n

def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat zion", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)

if __name__ == '__main__':
    test_run()