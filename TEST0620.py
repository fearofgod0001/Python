# for i in range(5):
#     for j in range(5-i):
#         print('*',end="")
#     print()


# def gugu():
#     print('구구단')
# for i in range(1, 10):
#     print('%d단' % i)
#     for j in range(1, 10):
#         print('%d * %d = %d' % (i, j, i*j))
#     print()

# hobby = ['농구', '축구', '야구']
# q,r,s=hobby
# print(q)
# print(r)
# print(s)


# singer = ['IU', '아리아나그란데', '라붐', '초아']
# print(list(map(lambda x: len(x), singer)))
# print(dict(list(map(lambda x: len(x), singer))):singer)
# # print(dict(zip(map(lambda x: len(x), singer))))

singer = ['IU', '아리아나그란데', '라붐', '초아']
print({x: len(x) for x in singer})