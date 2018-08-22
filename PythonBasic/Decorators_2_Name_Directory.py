'''
Input Format

The first line contains the integer N, the number of people.
N lines follow each containing the space separated values of the first name, last name, age and sex, respectively.

Output Format

Output N names on separate lines in the format described above in ascending order of age.

Sample Input

3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
Sample Output

Mr. Mike Thomson
Ms. Andria Bustle
Mr. Robert Bustle
'''
import operator

def person_lister(f):
    def inner(people):
        # complete the function
        '''
        Nice solution! Should add int() in lambda function, I suppose some test cases (with ages greater than 100) 
        were added later. string 2 > 10, so need to use int()
		'''
        return map(f, sorted(people, key=lambda x: int(x[2])))
    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')