from collections import deque
def solution(card1, card2, goal):
    card1q = deque(card1)
    card2q = deque(card2)
    goalq = deque(goal)

    for _ in range(len(goal)):
        goalcard = goalq.popleft()
        if len(card1q) > 0 and card1q[0] == goalcard:
            card1q.popleft()
        elif len(card2q) > 0 and card2q[0] == goalcard:
            card2q.popleft()
        else:
            return "No"
    else:
        return "Yes"

card1 = ["i", "water", "drink"]
card2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

print(solution(card1, card2, goal))

