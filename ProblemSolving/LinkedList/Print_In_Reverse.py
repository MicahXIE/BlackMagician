'''
Hackerank -- Print in Reverse

https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list-in-reverse/problem

'''

def reversePrint(head):

    if not head:
        return
    
    tmp = head
    res_lst = []
    res_lst_rv = []
    while(tmp):
        # insert at end of list
        res_lst.append(tmp.data)
        # insert at the front of list
        res_lst_rv.insert(0,tmp.data)
        tmp = tmp.next
    
    #res_lst_rv = res_lst[::-1]

    #multiple ways to print result
    #print('\n'.join([str(i) for i in res_lst[::-1]]))
    #print('\n'.join(map(str,res_lst[::-1])))
    print(*res_lst_rv, sep='\n')



