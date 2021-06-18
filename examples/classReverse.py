class palindromes:
    def __init__(self, word):
        self.word = word
        
    def printText(self):
        print(self.word)
        
    def reverse(self):
        print(self.word[::-1])
        
word1 = palindromes("next")

word1.printText()
word1.