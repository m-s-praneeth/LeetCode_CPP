class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        lst = [node for node in preorder.split(',')]
        #print(lst) ['9', '3', '4', '#', '#', '1', '#', '#', '2', '#', '6', '#', '#']
        stack = [] # Empty stack(list)
        if len(lst)<3:
            if (len(lst)==1 and lst[0]=='#'): #No nodes only hash
                return True
            else:#No or less hashes
                return False
        else:
            i = 0
            for node in lst:
                if node!='#':#NODE IS NUMBER
                    stack.append(node)
                else:#NODE IS HASH
                    if(len(stack)==0):
                        if(len(lst)==i+1):
                            return True
                        else:
                            return False
                    else:
                        stack.pop()
                i+=1