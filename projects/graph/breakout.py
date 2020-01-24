'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.

Note:
Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.


Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']

begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']

beginWord = "hungry"
endWord = "happy"
None
'''
import string
from util import Stack


f = open("words.txt", "r")
words = f.read().split("\n") 
f.close()

alphabet = list(string.ascii_letters)
word_options = set()
set_words = set(words)



def breakout(begin_word, end_word):
    stack = Stack()
    checked = set()
    stack.push([begin_word])

    if end_word not in set_words:
        print("not in words")
        return None
    if len(begin_word) != len(end_word):
        print('')
        return None
    count = 0
    while stack.size() > 0:
        transform = stack.pop()
        vertex = transform[-1]
        print("vertex", vertex)
        vertex_list = list(vertex)
        end_list = list(end_word)
        word_variations = []
        matched_variations = []
        if vertex not in checked:
            if vertex == end_word:
                return transform
            checked.add(vertex)
            for i in range(len(alphabet)):
                letter = alphabet[i]
                copy = vertex_list
                copy[count] = letter
                word_string = ''.join(copy)
                word_variations.append(word_string)
            count +=1
            print("word_variations", word_variations)
            for i in range(len(word_variations)):
                if word_variations[i] in set_words:
                    matched_variations.append(word_variations[i])
            print("matched", matched_variations)
            if matched_variations:
                new_transform = list(transform)
                length = len(matched_variations) - 1
                print('length', length)
                new_transform.append(matched_variations[length])
                print(new_transform)
                stack.push(new_transform)
                        


breakout('sail', 'boat')  
print(breakout('sail', 'boat')) 



