import collections

""" 计数 """
# c = collections.Counter('abababa')
#
# for letter in 'ab':
#     print('{0}: {1}'.format(letter, c[letter]))


""" 双端队列 """
d = collections.deque('abcdef')
print('Deque', d)

d.extend('aa')
print('Extend', d)

# 从队尾添加元素
d.append('j')
print('Append', d)

# 从队首添加元素
d.appendleft('m')
print('Append Left', d)

# 从队尾出元素
end = d.pop()
print('End', end)

# 从队首出元素
front = d.popleft()
print('Front', front)
