def latest(scores):
    try:
        return scores[-1]
    except NameError:
        raise Exception('List does not exist')


def personal_best(scores):
    try:
        return max(scores)
    except NameError:
        raise Exception('List does not exist')


def personal_top_three(scores):
    try:
        top_three = sorted(scores)
        top_three = top_three[::-1]
        return top_three[0:3]
    except NameError:
        raise Exception('List does not exist')
