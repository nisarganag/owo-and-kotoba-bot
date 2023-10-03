from collections import Counter
import time

with open('words.txt', 'r') as f:
    dictionary = f.read()
dictionary = [x.lower() for x in dictionary.split('\n')]

def return_anagrams(letters: str) -> list:
    global dictionary
    assert isinstance(letters,
                      str), 'Scrambled letters should only be of type string.'
    letters = letters.lower()
    letters_count = Counter(letters)
    anagrams = set()

    for word in dictionary:
        if not set(word) - set(letters):
            check_word = set()
            for k, v in Counter(word).items():
                if v <= letters_count[k]:
                    check_word.add(k)
            if check_word == set(word):
                anagrams.add(word)

    anagrams.remove('')
    return [string for string in sorted(list(anagrams), key=lambda x: len(x)) if len(string) == len(letters)]

if __name__ == '__main__':
    for i in range(10):
        start = time.time()
        test_anagrams = return_anagrams(input('Enter scrambled letters: '))
        print(test_anagrams)
        stop = time.time()
        print(f"Number of anagrams: {len(test_anagrams)}")
        print(f"Time Taken: {round(stop - start, 2)} seconds")
    time.sleep(5)