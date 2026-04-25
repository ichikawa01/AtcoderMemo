import itertools
"""

count: rangeでも代替できるやつ。start=, step=

cycle: 引数のイテレータを無限ループ

repeat: 引数をn回または無限回リピート

accumulate: 累積和

chain: 複数のイテレータを連結

chain.from_iterable: １個のイテレータから結合したイテレータを作る

compress: 引数のイテレータから要素を削除する 
dropwhile: 引数のイテレータから要素を削除する 
filterfalse: 引数のイテレータから要素を削除する
takewhile: 引数のイテレータから要素を取り出す

groupby: 引数のイテレータの要素をキーにグループ化

islice: 引数のイテレータから要素を取り出す

statmap: 引数のイテレータに関数を適用する

tee: 引数のイテレータを複数のイテレータに分割する

zip_longest: 引数のイテレータの要素を連結し、最長の長さのイテレータになるまで要素を追加する

product: デカルト積, 重複あり組み合わせ

permutations: 並び替え

combinations: 組み合わせ

combinations_with_replacement: 重複あり組み合わせ, (A, B)と(B, A)は重複しない


"""




"""
itertools.count(start, [,step]) -> iterator

無上限のrange関数、range(start infty, [,step])に相当する

eg: count(10) --> 10 11 12 13 14 ...
"""
for i in itertools.count(start=10, step=2):
    if i > 40:
        break
    print(i, end=' ') # -> 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40

"""
itertools.cycle(iterable) -> iterator

無限ループ回のfor文に相当する

eg: cycle('ABCD') --> A B C D A B C D ...
"""
count = 0
for i in itertools.cycle([5,4,3,2,1]):
    if count >= 10:
        break
    print(i, end=' ')
    count += 1 # -> 5 4 3 2 1 5 4 3 2 1

count = 0
for i in itertools.cycle((1,2,3)):
    if count >= 10:
        break
    print(i, end=' ')
    count += 1 # -> 1 2 3 1 2 3 1 2 3 1

"""
itertools.repeat(element, [,n]) -> iterator

elementを無限回またn回まで重複する
nを与えないと無限イテレータになる

eg: repeat(10, 3) --> 10 10 10
"""

list(itertools.repeat("a", 5)) # -> ['a', 'a', 'a', 'a', 'a']
for i in itertools.repeat(1, 5):
    print(i, end=' ') # -> 1 1 1 1 1

"""
itertools.accumulate(p, [,func]) -> iterator
デフォルトは累加関数で、funcを指定すると、いろんなカスタマイズ処理ができる

accumulate(p, func) -> p0, func(p0, p1), func(func(p0, p1), p2), ...
eg: accumulate([1,2,3,4,5]) --> 1 3 6 10 15　
"""
list(itertools.accumulate([1, 2, 3, 4, 5])) # -> [1, 3, 6, 10, 15]
for i in itertools.accumulate([1, 2, 3, 4, 5]):
    print(i, end=' ') # -> 1 3 6 10 15

import operator
data = [5, 4, 3, 2, 1]
list(itertools.accumulate(data, operator.mul)) # -> [5, 20, 60, 120, 120]
list(itertools.accumulate(data, lambda x, y: x+2*y)) # -> [5, 13, 19, 23, 25]

"""
itertools.chain(iterable1, iterable2, ...) -> iterator
複数なiterablesを一つのイテレータにまとめることが出来る、割と使えると思う

eg: chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
"""
list(itertools.chain([1, 2, 3], (4, 5, 6))) # -> [1, 2, 3, 4, 5, 6]
list(itertools.chain(map(str, [1, 2, 3]), map(str, (4, 5, 6)), "aabc")) 
# -> ['1', '2', '3', '4', '5', '6', 'a', 'a', 'b', 'c']

"""
itertools.chain.from_iterable(iterable) -> iterator

一個のiterableからchainのようなイテレータを作る、ただし、このiterableは複数なiterableを含む

eg:  chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
"""
list(itertools.chain.from_iterable(["abc", (1, 2, 3)])) # -> ['a', 'b', 'c', 1, 2, 3]

"""
itertools.compress(iterable, selectors) -> iterator

selectorsの評価値が真となるようなiterableの要素を取り出すイテレータを作る
ポジション的なfilterに相当する

eg:  compress('ABCDEF', [1,0,1,0,1,1]) --> A C E F
"""
list(itertools.compress([1,2,3,4,5,6], [1,0,1])) # -> [1, 3]

"""
itertools.dropwhile(predicate, iterable) -> iterator

iterableの各要素に対して、predicateの評価値が偽になったら、その要素から、以降の要素を返すイテレータを作る
使い方いまいちわからないが、何かしらの条件を満たさない時点を探し、その後残り要素に対し他の処理をしたい時に使えるかも

eg: dropwhile(lambda x: x<5, [1,4,6,4,1]) --> 6 4 1
"""
list(itertools.dropwhile(lambda x: x < "b", sorted(["a", "r", "e", "c", "d"])))
# -> ['c', 'd', 'e', 'r']

"""
itertools.filterfalse(predicate, iterable) -> iterator

filterの逆、predicateの評価値が偽となる要素を出力するイテレータ
filterを使えば同じこともできる気がするが、謎だ

eg: filterfalse(lambda x: x%2, range(10)) --> 0 2 4 6 8
"""
list(itertools.filterfalse(lambda x: x % 2 == 0, range(10))) # -> [1, 3, 5, 7, 9]
list(filter(lambda x: x % 2 != 0, range(10))) # -> [1, 3, 5, 7, 9]

"""
itertools.groupby(iterable, [, key]) -> iterator

SQLが使えないときに使うときらしい、ただし、使う前に必ずiterableをソートしておくこと

key はソートを指定する関数を指定できる

どこで使えばよいかまだいまいちだけど
"""
a = [("b", 3), ("a", 1), ("c", 2), ("a", 2), ("b", 1)]
a.sort(key=operator.itemgetter(0))
for (k, g) in itertools.groupby(a, key=operator.itemgetter(0)):
    print("key: {}".format(k), list(g))
# key: a [('a', 1), ('a', 2)]
# key: b [('b', 1), ('b', 3)]
# key: c [('c', 2)]

l = [1, 2, 3, 4, 6, 8]
grouped = itertools.groupby(l, key=lambda x: x%2)
for k, g in grouped:
    print(list(g))
# [1]
# [2]
# [3]
# [4, 6, 8]

A = "aaabbbcccd"
S =  [''.join(group) for _, group in itertools.groupby(A)]
# -> ['aaa', 'bbb', 'ccc', 'd'] 

# '0' の最大連続長を計算
s = "001110000110100"
max_zeros = max((len(list(g)) for k, g in itertools.groupby(s) if k == '0'), default=0)
# -> 4

"""
itertools.islice(iterable, [,start], stop, [,step]) -> iterator

stopを指定しないといけないので、末尾まで指定したいとき、Noneとおけばよい
スライスの結果をイテレータとして返す
メモリ的に考えると使えそう

eg:  islice('ABCDEFG', 2, None) --> C D E F G
"""
list(itertools.islice('ABCDEFG', 2)) # -> ['A', 'B']
list(itertools.islice('ABCDEFG', 2, None)) # -> ['C', 'D', 'E', 'F', 'G']
list(itertools.islice(range(10000000), 12345, None, 1000000))
# [12345,
#  1012345,
#  2012345,
#  3012345,
#  4012345,
#  5012345,
#  6012345,
#  7012345,
#  8012345,
#  9012345]

"""
itertools.starmap(function, iterable) -> iterator

iterableの各要素に指定されたfunctionを適用して計算した結果をイテレータとして返す

eg: starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
"""
list(itertools.starmap(lambda x, y, z: (x - y)**z, [(1, 2, 2), (2, 0, 3), (3, 1, 4)]))
# -> [1, 8, 16]

"""
itertools.takewhile(predicate, iterable) -> iterator

dropwhileの逆、iterableの各要素に対して、predicateの評価値が真であれば、その要素を出力し、
偽になったときから以降の要素を無視するイテレータを作る
おそらくdropwhileと同じくbreak pointを探すときに使えると思う

eg: takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
"""
list(itertools.takewhile(lambda x: x < "b", sorted(["a", "r", "e", "c", "d"]))) # -> ['a']
list(itertools.dropwhile(lambda x: x < "b", sorted(["a", "r", "e", "c", "d"]))) # -> ['c', 'd', 'e', 'r']

"""
itertools.tee(iterable, n=2) -> n_iterators

一つのiterableからn個のイテレータを作る、各イテレータが独立となる
戻り値が複数なイテレータになることに注意

"""
it1, it2, it3 = itertools.tee(range(5), 3)
list(it1) # -> [0, 1, 2, 3, 4]
next(it2) # -> 0
list(it2) # -> [1, 2, 3, 4]
tuple(it3) # -> (0, 1, 2, 3, 4)

"""
itertools.zip_longest(iterable1, iterable2, ..., fillvalue=None) -> iterator
zipしたいiterablesの長さが一致しないとき使う、不足な値はfillvalueで指定できる。

eg: zip_longest('ABCD', 'xy', fillvalue='-') --> Ax By C- D-
"""
for a, b, c in zip([1, 2], [3, 4], [5, 6]):
    print(a, b, c)
# 1 3 5
# 2 4 6

for a, b, c, d in itertools.zip_longest([1, 2], [3, 4, 7], [5], "6"):
    print(a, b, c, d)
# 1 3 5 6
# 2 4 None None
# None 7 None None

for a, b, c, d in itertools.zip_longest([1, 2], [3, 4, 7], [5], "6", fillvalue="?"):
    print(a, b, c, d)
# 1 3 5 6
# 2 4 ? ?
# ? 7 ? ?

"""
itertools.product(iterable1, ..., [,repeat=1]) -> iterator
入力されたiterablesのデカルト積/直積を返すイテレータを作る
repeatを指定すると、iterablesの数を倍にすることができる
product(A, repeat=4)はproduct(A, A, A, A)と同じとなる

eg: product('ABCD', repeat=2) --> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
"""
list(itertools.product("AB", repeat=3))
# [('A', 'A', 'A'),
#  ('A', 'A', 'B'),
#  ('A', 'B', 'A'),
#  ('A', 'B', 'B'),
#  ('B', 'A', 'A'),
#  ('B', 'A', 'B'),
#  ('B', 'B', 'A'),
#  ('B', 'B', 'B')]

list(itertools.product("ABC", "123"))
# [('A', '1'),
#  ('A', '2'),
#  ('A', '3'),
#  ('B', '1'),
#  ('B', '2'),
#  ('B', '3'),
#  ('C', '1'),
#  ('C', '2'),
#  ('C', '3')]

"""
itertools.permutations(iterable, [,r]) -> iterator

iterableから順列を返すイテレータを作る, rは順列の長さを指定できる
rを指定しないと全順列となる

eg: permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
"""
list(itertools.permutations("ABC"))
# [('A', 'B', 'C'),
#  ('A', 'C', 'B'),
#  ('B', 'A', 'C'),
#  ('B', 'C', 'A'),
#  ('C', 'A', 'B'),
#  ('C', 'B', 'A')]

l = ['a', 'b', 'c', 'd']
for v in itertools.permutations(l):
    print(v)
# ('a', 'b', 'c', 'd')
# ('a', 'b', 'd', 'c')
# ('a', 'c', 'b', 'd')
# ('a', 'c', 'd', 'b')
# ('a', 'd', 'b', 'c')
# ('a', 'd', 'c', 'b')
# ('b', 'a', 'c', 'd')
# ('b', 'a', 'd', 'c')
# ('b', 'c', 'a', 'd')
# ('b', 'c', 'd', 'a')
# ('b', 'd', 'a', 'c')
# ('b', 'd', 'c', 'a')
# ('c', 'a', 'b', 'd')
# ('c', 'a', 'd', 'b')
# ('c', 'b', 'a', 'd')
# ('c', 'b', 'd', 'a')
# ('c', 'd', 'a', 'b')
# ('c', 'd', 'b', 'a')
# ('d', 'a', 'b', 'c')
# ('d', 'a', 'c', 'b')
# ('d', 'b', 'a', 'c')
# ('d', 'b', 'c', 'a')
# ('d', 'c', 'a', 'b')
# ('d', 'c', 'b', 'a')

list(map(lambda x: int(x[0]) + int(x[1]), itertools.permutations("12345", 2)))
# ->[3, 4, 5, 6, 3, 5, 6, 7, 4, 5, 7, 8, 5, 6, 7, 9, 6, 7, 8, 9]

"""
itertools.combinations(iterable, r) -> iterator

iterableから組み合わせを返すイテレータを作る、permutationsと違って、rの指定は必須

eg: combinations('ABCD', 2) --> AB AC AD BC BD CD
"""
list(itertools.combinations("ABCDE", 2))
# [('A', 'B'),
#  ('A', 'C'),
#  ('A', 'D'),
#  ('A', 'E'),
#  ('B', 'C'),
#  ('B', 'D'),
#  ('B', 'E'),
#  ('C', 'D'),
#  ('C', 'E'),
#  ('D', 'E')]

"""
itertools.combinations_with_replacement(iterable, r) -> iterator

combinationsと似ているが、違うところとしては組み合わせのとき重複ありを考える

eg: combinations_with_replacement('ABCD', 2) --> AA AB AC AD BB BC BD CC CD DD
"""
list(itertools.combinations_with_replacement("ABCDE", 2))
# [('A', 'A'),
#  ('A', 'B'),
#  ('A', 'C'),
#  ('A', 'D'),
#  ('A', 'E'),
#  ('B', 'B'),
#  ('B', 'C'),
#  ('B', 'D'),
#  ('B', 'E'),
#  ('C', 'C'),
#  ('C', 'D'),
#  ('C', 'E'),
#  ('D', 'D'),
#  ('D', 'E'),
#  ('E', 'E')]
