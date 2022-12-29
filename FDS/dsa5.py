# string declearation

def create():
    x = input("\nenter your string :")
    return x

def longword(x): 
    tmp = x.split()
    max = 0
    for i in tmp:
        if len(i)>max:
            max = len(i)
            word = [i]
    print("\n '%s' is the longest word in the string,it is %d characters long." %(word[0],max))


def freqchar(st,ch):
    count = 0
    for i in range (0,len(st)):
        if st[i] == ch:
            count += 1
    print("\n '%s'appears %d times in your string." %(ch,count))

def palindrome(x):
    tmp = x[::-1]
    if x == tmp:
        return true
    else:
        return false


def look(st,sub_st):
    tmp = st.split()
    if sub_st in tmp:
        ind_list = tmp.index(sub_st)
        ind_str = 0
        for i in tmp [o:ind_list]:
            ind_str += len(i) + 1
        print("\n '%s' substring first appears at %d  index in your string" %(sub_st,ind_str))

    else:
       print("\n entered substring not found!!")


def countall(st):
    count = {}
    tmp = st.split()
    for i in tmp:
        occ = 0
        for j in tmp:
            if i == j:
                occ += 1
            count[i] = occ
    print("\n word \t count")
    for i in count.keys():
        print(i,"\t",count[i])

# calling the functions
longword(create())
freqchar(create(),input("\n enter your character: "))
look(create(),input("\n enter substring to look for: "))
countall(create())
    
