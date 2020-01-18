"""Find palindromes (letter palingrams) in a dictionary file"""
import load_dictionary
import dictionary_cleanup

word_list = dictionary_cleanup.cleanup(load_dictionary.load('words.txt'))

def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return True

    if word[:1] != word[-1:]:
        return False
    else:
         return is_palindrome(word[1:-1])


pali_list = [word for word in word_list if is_palindrome(word)]
print("\nNumber of palindromes found = {}\n".format(len(pali_list)))
print(*pali_list, sep='\n')
