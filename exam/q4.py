class StringUtility(object):
    
    def count_vowels(words):
        vowels = ['a','e','i','o','u']
        count = 0
        for letter in words:
            if letter in vowels:
                count+=1
        return count

    def unique_vowels(words):
        vowels = ['a','e','i','o','u']
        count = 0
        unique = []
        for letter in words:
            if letter in vowels:
                if letter not in unique:
                    unique.append(letter)
        return unique

    def count_spaces(words):
        count = 0
        for letter in words:
            if letter ==' ':
                count+=1
        return count

def main():
    test = StringUtility
    text = 'How now a brown cow'
    print(test.count_vowels(text))
    print(test.unique_vowels(text))
    print(test.count_spaces(text))
main()