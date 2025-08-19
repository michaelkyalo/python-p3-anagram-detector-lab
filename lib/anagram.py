class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, words):
        """Return list of words that are anagrams of self.word"""
        return [w for w in words if sorted(w.lower()) == sorted(self.word) and w.lower() != self.word]
