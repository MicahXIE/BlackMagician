'''
Sample Input:
3
programming is awesome

Sample Output:
4

Explanation 1

There are 3 words in the input: programming, is and awesome.
The score of programming is 1 since it contains 3 vowels, an odd number of vowels. 
The score of is is also 1 because it has an odd number of vowels. 
The score of awesome is 2 since it contains 4 vowels, an even number of vowels. 
Thus, the total score is 1+1+2=4.

'''
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
        	# ++score equals +(+score) wont increase
            score += 1
    return score

n = int(input())
words = input().split()
print(score_words(words))