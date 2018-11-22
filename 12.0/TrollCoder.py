import sys

n = int(input())

initial = [0]*n
answer = [0]*n
initial_correct = 0


def print_message(letter, l):
    message = letter
    for num in l:
        message += " " + str(num)
    print(message)


for i in range(-1, n):
    if i == -1:
        print_message("Q", initial)
        initial_correct = int(input())
        continue
    initial[i] = 1
    print_message("Q", initial)
    current_correct = int(input())

    if current_correct > initial_correct:
        answer[i] = 1
    else:
        answer[i] = 0
    initial[i] = 0
    sys.stdout.flush()

print_message("A", answer)