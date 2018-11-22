import sys
import random


def change(l, n):
    if l[n] == 0:
        return 1
    return 0


def print_message(letter, l):
    message = letter
    for num in l:
        message += " " + str(num)
    print(message)


def test_case():
    n = int(input())
    initial = []
    answer = []
    for i in range(n):
        r = random.randint(0, 1)
        initial.append(r)
        answer.append(r)
    initial_correct = 0

    for i in range(-1, n):
        if i == -1:
            print_message("Q", initial)
            initial_correct = int(input())
            continue
        initial[i] = change(initial, i)
        print_message("Q", initial)
        current_correct = int(input())

        if current_correct == n:
            print_message("A", initial)
            return

        if current_correct > initial_correct:
            initial_correct = current_correct
        else:
            initial[i] = change(initial,i)
        sys.stdout.flush()

    print_message("A", answer)
    return


t = int(input())
for i in range(t):
    test_case()
