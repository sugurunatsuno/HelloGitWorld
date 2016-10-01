
# coding: utf-8

# In[1]:

print("Hello!")


# In[2]:

character = "0123456789abcdefghijklmnopqrstuvwxyz"
character_map = []
for i in character:
    character_map.append(i)


# In[18]:

def ten2nth(value, N):
    if(N > 36):
        N = 36
    elif(N < 2):
        N = 2
    character = "0123456789abcdefghijklmnopqrstuvwxyz"
    character_map = []
    for i in character:
        character_map.append(i)
    
    
    output = []
    while(value > 0):
        output.append(value % N)
        value = value // N
    output.reverse()
    output_character = ""
    for i in output:
        output_character = output_character + character_map[i]
    
    return output_character


# In[21]:

ten2nth(99999989,16)


# In[26]:

def nth2ten(strvalue, N):
    if(N > 36):
        N = 36
    elif(N < 2):
        N = 2
    character = "0123456789abcdefghijklmnopqrstuvwxyz"
    character_map = []
    for i in character:
        character_map.append(i)
    
    length = len(strvalue)
    output = 0
    for i in strvalue:
        output = output + character_map.index(i) * N ** (length - 1)
        length = length - 1
        
    return output


# In[27]:

nth2ten("ff", 16)


# In[ ]:



