from nltk.tokenize import sent_tokenize


def lines(a, b):
    """Return lines in both a and b"""

    # split both string based on the \n
    a = a.split("\n")
    b = b.split("\n")
    matches = []

    # check each line of a to see if it exist in b too.
    for line in a:

        if line not in matches and line in b:

            matches.append(line)

    return matches


def sentences(a, b):
    """Return sentences in both a and b"""

    # split (or tokenize) both string on to sentences
    a = sent_tokenize(a)
    b = sent_tokenize(b)
    matches = []

    # check each sentence of a to see if it exists in b
    for sentence in a:

        if sentence not in matches:

            if sentence in b:

                matches.append(sentence)

    return matches


def substrings(a, b, n):
    """Return substrings of length n in both a and b"""

    sub = ""
    matches = []

    # create a list of the a substrings.
    i = 0
    j = n
    aList = []

    # create a list of all possible substring of n length in a
    while(j <= len(a) + 1):

        sub = a[i:j]

        aList.append(sub)

        i += 1
        j += 1

    # Check each b substring to see if it is also an a substring.
    i = 0
    j = n

    while(j <= len(b) + 1):

        sub = b[i:j]

        if sub not in matches and sub in aList and len(sub) == n:

            matches.append(sub)

        i += 1
        j += 1

    return matches
