#created class named palindromes
class palindromes:
    def __init__(self, word):
        self.word = word
        
    def printText(self):
        return self.word
    
    #method for returning the reverse of the word
    def reverse(self):
        return self.word[::-1]

  
word1 = palindromes(input("Enter the word: "))

#prints the word
print(word1.printText())

#prints the word in reverse
print(word1.reverse())