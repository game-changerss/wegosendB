import sys

input = sys.stdin.readline

arr = list(input().rstrip())  # 문자열을 하나의 리스트로 받는것.(list)

result = [""] * len(arr) #c++ malloc 으로 생각하면됨

최종커밋

def solution(start, arr):
    if not arr:
        return
    min_val = min(arr)
    temp = arr.index(min_val)

    result[start + temp] = min_val
    print("".join(result))
    solution(start + temp + 1, arr[temp + 1:])
    # 가장 작은 거 기준으로 오른쪽으로 먼저 재귀해야 가장 사전순으로 작은 값이됨
    # ex) A x->  CA  // A -> AQ  // 이와 같이 가장작은거 기준 왼쪽으로 먼저 값을넣게되면
    # 사전순서를 만족 시킬수 없다.
    solution(start, arr[:temp])


solution(0, arr)