def solution(prices):
    # answer = 몇초 후 가격이 떨어지는지 저장하는 배열
    answer = [len(prices)-i-1 for i in range(len(prices))]

    # stack = prices의 인덱스를 차례로 담아두는 배열
    stack = [0]

    for i in range(1, len(prices)):
        while stack:
            index = stack[-1]

            # 주식 가격이 떨어졌다면
            if prices[index] > prices[i]:
                answer[index] = i - index
                stack.pop()

            # 떨어지지 않았다면 다음 시점으로 넘어감 (주식 가격이 계속 증가하고 있다는 말)
            else:
                break

        # 스택에 추가한다.
        # 다음 시점으로 넘어갔을 때 다시 비교 대상이 될 예정이다.
        stack.append(i)

    return answer
