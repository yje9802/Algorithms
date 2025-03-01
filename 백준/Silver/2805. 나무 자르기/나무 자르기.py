from sys import stdin

# H만큼 나무를 잘랐을 때 얻을 수 있는 총 길이
def get_wood_length(trees, H):
    return sum(tree - H for tree in trees if tree > H)

def find_max_height(trees, M):
    left, right = 0, max(trees)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        cut = get_wood_length(trees, mid)

        if cut >= M:  # 필요한 나무 길이보다 크거나 같으면 H 더 높게 설정 가능
            result = mid  # 정답 후보
            left = mid + 1
        else:  # 나무가 부족하면 H를 더 낮춤
            right = mid - 1

    return result

# 입력 처리
N, M = map(int, stdin.readline().split())
trees = list(map(int, stdin.readline().split()))

print(find_max_height(trees, M))