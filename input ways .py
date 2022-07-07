'''input ways'''



# a=input()
# print('my name is',a)  #my name is ravi
# print('my name is',a,sep='-')  #my name is-ravi
# print('name',int(a))  #name 24
# print('name',float(a))  #name 24.0


# a=int(input())
# # print('my name is',a)  #my name is 23
# print('my name'+str(a))  #my name6
# print('my name',float(a))  #my name6.0 

a=input('name')
b=int(input('age'))
c=float(input('rank'))
# # # print(a,b,c)  #ravi 23 3.0
# # print(a,c,c)  #ra 3.0 3.0
# # print('you are',a,'age',b,'rank',c) # you are ra age 34 rank 5.0
# # print('you are'+a+'age'+str(b)+'rank'+str(c))   #you areraage45rank3.0
# print('you are %s and age %d and rank %.1f'(a,b,c))
print('name is{} and age is {} rank {}'.format(a,b,c))

