'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string,S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Scoring
A player gets +1 point for each occurrence of the substring in the string S.

For Example:
String  S = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

Input Format

A single line of input containing the string S. 
Note: The string S will contain only uppercase letters: [A-Z] .

Constraints

0 < len(S) < 10^6

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input:
BANANA

Sample Output:
Stuart 12

'''


#Solution 1 but complexity is not good
def minion_game_s1(string):
    str = string
    st_score = 0
    kv_score = 0
    vowels_lst = ['A','E','I','O','U']
    
    #get all the substr
    substr_lst = [str[i:i + x + 1] for x in range(len(str)) for i in range(len(str) - x)]
    
    #remove the duplicated element
    substr_set = set(substr_lst)
    
    for k in substr_set:
        if k[0] in vowels_lst:
            kv_score += substr_lst.count(k)
        else:
            st_score += substr_lst.count(k)
    
    if kv_score > st_score:
        print("Kevin", kv_score)
    elif kv_score < st_score:
        print("Stuart", st_score)
    else:
        print("Draw")

#Solution 2 refer to the forum and it is very nice
def minion_game_s2(string):
	str = string
	st_score = 0
	kv_score = 0

	vowels = 'AEIOU'

	for i in range(len(str)):
		if str[i] in vowels:
			kv_score += (len(str)-i)
		else:
			st_score += (len(str)-i)

    if kv_score > st_score:
        print("Kevin", kv_score)
    elif kv_score < st_score:
        print("Stuart", st_score)
    else:
        print("Draw")

    
if __name__ == '__main__':
    s = input()
    minion_game_s2(s)
