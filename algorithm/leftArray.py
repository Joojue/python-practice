W = int(input())
words = input().split()

def left_Array():
        
        dpt=[0] * (len(words)+1)
        dpt[1] = (W - len(words[0]))**3

        for i in range(2,len(words)+1):
                add = 0
                dpt[i] = dpt[i-1] + (W-len(words[i-1]))**3
                add += len(words[i-1])
                j = i - 1
        
                while j > 0:
                        add += len(words[j-1])+1
                        if add > W:
                                break
                        dpt[i] = min(dpt[j-1]+(W-add)**3,dpt[i])
                        j -= 1
        

        return dpt[-1]

print(left_Array())