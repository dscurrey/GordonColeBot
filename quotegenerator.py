import random

def gc_quote():
    quotes_tuple = []
    with open('quotes.txt', 'r') as quotes:
        for line in quotes:
            quotes_tuple.append(line)
        randQuote = random.choice(quotes_tuple)
        return randQuote
