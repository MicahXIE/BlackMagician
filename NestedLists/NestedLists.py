
'''
Given the names and grades for each student in a Physics class of N students, store them in a nested list and 
print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer,N, the number of students. 
The  2N subsequent lines describe each student over 2 lines; 
the first line contains a student's name, and the second line contains their grade.

Sample input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:
Berry
Harry

'''


# Solution 1 
if __name__ == '__main__':
    
    stu_lst = []
    name_lst = []
    score_lst = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_lst.append(name)
        score_lst.append(score)
        stu_lst.append([name,score])
    
    m = min(score_lst)
    while min(score_lst) == m:
        score_lst.remove(min(score_lst))
    
    n = min(score_lst)
    
    res_lst = []
    for item in stu_lst:
        if item[1] == n:
            res_lst.append(item[0])
    
    res_lst.sort()
    print(*res_lst, sep='\n')

# Solution 2 Very elegant one (https://github.com/jivoi/junk/blob/master/hackerrank/python/data-types/nested-list.py)
n = int(input())
marks = [[input(), float(input())] for _ in range(n)]
scores = sorted({s[1] for s in marks})
result = sorted(s[0] for s in marks if s[1] == scores[1])
print('\n'.join(result))





