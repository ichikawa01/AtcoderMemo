"""
グリッドの左上から時計回りに文字を取り出す
"""

H, W = map(int, input().split())
G = [list(input()) for _ in range(H)]

def spiral_order(H, W, G):
    result = []
    left, right, top, bottom = 0, W - 1, 0, H - 1

    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            result.append(G[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(G[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(G[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(G[i][left])
            left += 1

    return result

spiral = spiral_order(H, W, G)
print(''.join(spiral))