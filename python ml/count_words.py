"""Count words."""

def count_words(s, n):

    """Return the n most frequently occuring words in s."""

    # TODO: Count the number of occurences of each word in s

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)

    # TODO: Return the top n words as a list of tuples (<word>, <count>)
    return top_n


def test_run():
    """Test count_words() with some inputs."""
    print count_words("cat bat mat cat bat cat", 3)
    print count_words("betty bought a bit of butter but the butter was bitter", 3)


if __name__ == '__main__':
    words = "cat bat mat cat bat cat"
    words_list = words.split()
    # sorted_words = sorted(words_list, key=str.lower)

    # list
    # pairs = []
    # for w in words_list:
    #     pairs.append((w, words_list.count(w)))

    # diff_words_counts = list(set(pairs))
    # print diff_words_counts

    # dictionary
    dicts = {}
    for w in words_list:
        dicts.update({w: words_list.count(w)})
    print dicts
    # order words by it's occurence
    dicts_key_by_number = sorted(dicts, key=dicts.__getitem__, reverse=True)
     # occurence
    print type(dicts[dicts_key_by_number[0]])
    # key words
    print type(dicts_key_by_number[0])
    top_n = []
    for i in range(2):
        top_n.append((dicts_key_by_number[i], dicts[dicts_key_by_number[i]]))
    print top_n
    # test_run()