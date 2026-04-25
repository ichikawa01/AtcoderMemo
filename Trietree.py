trie = {}

# 共有接頭辞のカウント用
# def insert(word):
#     node = trie
#     count = 0
#     for char in word:
#         if char not in node:
#             node[char] = {'cnt': 0}
#         node = node[char]
#         node['cnt'] += 1
#         count += node['cnt']
#     node['$'] = True  # 終端マーカー
#     global ans
#     ans += count - len(word)

def insert(word):
    node = trie
    for char in word:
        node = node.setdefault(char, {})
    node['$'] = True  # '$'は単語の終端を示すマーカー

def search(word):
    node = trie
    for char in word:
        if char not in node:
            return False
        node = node[char]
    return '$' in node

def starts_with(prefix):
    node = trie
    for char in prefix:
        if char not in node:
            return False
        node = node[char]
    return True


N = int(input())
S = list(input().split())
for s in S:
    insert(s)
