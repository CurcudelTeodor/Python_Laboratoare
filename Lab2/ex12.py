def group_by_rhyme(words):
    rhyme_groups = {}

    for word in words:
        rhyme = word[-2:]
        if rhyme in rhyme_groups:
            rhyme_groups[rhyme].append(word)
        else:
            rhyme_groups[rhyme] = [word]

    grouped_words = list(rhyme_groups.values())
    return grouped_words


def main():
    words = ['ana', 'banana', 'carte', 'arme', 'parte']
    rhyme_groups = group_by_rhyme(words)
    print(rhyme_groups)


if __name__ == "main":
    main()





