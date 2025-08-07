from itertools import combinations

a, b = map(int, input().split(" "))
card = [i for i in range(1, 11)] * 2
card.remove(a)
card.remove(b)
c_list = list(combinations(card, 2))


def get_idx(a: int, b: int):
    if a == b:
        return 10 - a
    else:
        return 19 - ((a + b) % 10)


def get_pos(c_list, a, b):
    cnt = 0
    idx = get_idx(a, b)
    for c in c_list:
        idx2 = get_idx(c[0], c[1])
        if idx2 > idx:
            cnt += 1
    return cnt


value = get_pos(c_list, a, b) / len(c_list)
print(f"{value:.3f}")
