# Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    max_score = max(scores)
    modified_scores = list(filter(lambda a: a != max_score, scores))
    print(max(modified_scores))