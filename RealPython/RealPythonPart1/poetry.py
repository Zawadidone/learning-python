from random import choice

nouns = ["fossil",	"horse",	"aardvark",	"judge",	"chef",	"mango",	"extrovert", "gorilla"]
verbs = ["kicks",	"jingles",	"bounces",	"slurps",	"meows",	"explodes",	"curdles"]
adjectives = ["furry",	"balding",	"incredulous",	"fragrant",	"exuberant",	"glistening"]
prepositions = ["against",	"after",	"into",	"beneath",	"upon",	"for",	"in",	"like",	"over", "within"]
adverbs = ["curiously", "extravagantly",	"tantalizingly",	"furiously",	"sensuously"]


def makepoem():

    # pull up 3 nouns
    n1 = choice(nouns)
    n2 = choice(nouns)
    n3 = choice(nouns)
    while n1 == n2:
        n2 = choice(nouns)
    while n2 == n3 or n1 == n3:
        n3 = choice(nouns)

    # pull up 3 verbs
    v1 = choice(verbs)
    v2 = choice(verbs)
    v3 = choice(verbs)
    while v1 == v2:
        v2 = choice(verbs)
    while v2 == v3 or v3 == v1:
        v3 = choice(verbs)

    # pull up 3 adjectives
    a1 = choice(adjectives)
    a2 = choice(adjectives)
    a3 = choice(adjectives)
    while a1 == a2:
        a2 = choice(adjectives)
    while a2 == a3 or a3 == a1:
        a3 = choice(adjectives)

    # pull up 2 prepositions
    p1 = choice(prepositions)
    p2 = choice(prepositions)
    while p1 == p2:
        p2 = choice(prepositions)

    # pull up 1 adverb
    av1 = choice(adverbs)

    if "aeiouy".find(a1) != -1:
        a = "A"
    else:
        a = "An"

    poem = f"""{a} {a1} {n1} \n{a} {a1} {n1} {v1} {p1} the {a2} {n2} \n{av1}, the {n1} {v2} \nthe {n2} {v3} {p2} a {a3}
    {n3}"""
    return poem

poetic = print(makepoem())
