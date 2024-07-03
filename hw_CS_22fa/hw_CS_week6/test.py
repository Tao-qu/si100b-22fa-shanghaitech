# alist = [i + j for j in ["A","K","Q","J","T","9","8","7","6","5","4","3","2"] for i in ["S","H","C","D"] ]
# print(alist)

# n,m = input().split(",")
# print(n,m)

# hand_card = eval(input())
# print(hand_card[1])

# # input comma separated elements as string 
# str = str (input ("Enter comma separated integers: "))
# print ("Input string: ", str)
 

# # conver to the list
# list = str.split (",")
# print ("list: ", list)
 
# # convert each element as integers
# li = []
# for i in list:
# 	li.append(int(i))
 
# # print list as integers
# print ("list (li) : ", li)


# hand_card = (",".join(open("test.csv").read().split())).split(",")
# print(hand_card)

# a = input().split(",")
# dict = {}
# for key in a: 
# 	dict[key] = dict.get(key, 0) + 1
# print (dict)

# a = [1,1,1,2,2,3,3,3,3]
# dict = {}
# for key in a: 
# 	dict[key] = dict.get(key, 0) + 1
# print (dict.values())
# print (type(dict.values()))

# a = [1,1,1,2,2,3,3,3,3]
# dict = {}
# for key in a: 
# 	dict[key] = dict.get(key, 0) + 1
# # for value in dict.values():
# # 	print(value)
# print(dict[1])
# print(type(dict[1]))

# hand_card = input().split(",")
# print(hand_card)
# suit_card = [hand_card[i][1] for i in range(len(hand_card))]
# print(suit_card)
# suit_dict = {}
# for key in suit_card:
#     suit_dict[key] = suit_dict.get(key, 0) + 1
# print(suit_dict)

# a = {'H':5}
# print(a.keys())
# print(type(a.keys()))
# print(list(a.keys()))

# flush = ["A","T","J","Q","K"]
# if "A" and "T" and "J" and "Q" and "K" in flush:
# 	print("ok")

# a = input().split()
# print(a)

# def SF(flush):
#         n = flush[0]
#         cons = 1
#         for i in flush:
#             if i == n + 1:
#                 n = i
#                 cons = cons + 1
#                 print(cons)
#                 if cons >= 5:
#                     break
#             else:
#                 n = i
#                 cons = 1
#         return cons
# flush = [1,3,5,7,9,11,13]
# print(SF(flush))

# n = 3
# for i in range(n):
#     x = input()
#     print(x)

# n = 3
# a = []
# for i in range(n):
#     a.append(input())
# print(a)

# def a():
#     print(1)
#     return 0
# if a() == 0:
#     print(2)

# a = {"A":14,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13}
# print(a.keys())
# print(type(a.keys()))
# print([*a])
# print(type([*a]))
# print([*a].sort())
# print(sorted([*a]))

# def A(a):
#     print(a)
#     a.append(1)
#     print(a)
# a = [1]
# A(a)
# A(a)

# hand_card = ["SA","S2"]
# cor = {"A":14,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13}
# # num_hand = (cor[hand_card[i][1]] for i in range(len(hand_card)))
# # print(type(cor[hand_card[0][1]]))
# # print(type(num_hand))

# num_hand = []
# for i in hand_card:
#     num_hand.append(cor[i[1]])
# print(num_hand)

# def A(a):
#     a.pop()
#     print(a)
#     return 0
# a=[1,2,3,4,5,6,7]
# print(a)
# A(a)
# print(a)

# def A():
#     print(a)
# a=1
# A()

# a = [1]
# a = [1,2]
# print(a)

# def A():
#     return a
# a = 1
# print(A())

# def A():
#     return [1,2]
# print(A()[0])

# def A():
#     a.append(1)
#     b += 1
#     return 0
# a = []
# b = 0
# print(a,b)

# a = []
# b = [1,2]
# c = [3,4,5]
# a = b + c
# print(a)
# print(a)
# a.extend(b)
# print(a)
# a.extend(c)
# print(a)

# def A():
#     a += 1
#     return 0
# a = 0
# print(a)

# def B(b):
#     b += 1
#     return 0
# b = 0
# print(b)

a = 1
a -= 1
print(a)