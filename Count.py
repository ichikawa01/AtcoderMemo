from collections import Counter

c = Counter('deep insider')
print(c)
# 出力結果
#Counter({'e': 3, 'd': 2, 'i': 2, 'p': 1, ' ': 1, 'n': 1, 's': 1, 'r': 1})

print(c['d'])  # 2
print(c['D'])  # 0：含まれていなかった要素のカウントは0

l = ['foo', 'foo', 'bar', 'baz', 'baz', 'foo']
c = Counter(l)
print(c)  # Counter({'foo': 3, 'baz': 2, 'bar': 1})

# 一番たくさんある要素をmost_commonメソッドで調べる
l = ['foo', 'foo', 'bar', 'baz', 'baz', 'foo']
c = Counter(l)
mx = c.most_common()
print(mx)  # [('foo', 3), ('baz', 2), ('bar', 1)]

mx = c.most_common(2)  # 多い順にn個を取り出す
print(mx)  # [('foo', 3), ('baz', 2)]

for k, v in mx:
    print(f'item: {k}, occurrence: {v}')
# 出力結果：
#item: foo, occurrence: 3
#item: baz, occurrence: 2