test_input = "/home/thomas/repos/advent_of_python/2022/02/input.test.txt"
main_input = "/home/thomas/repos/advent_of_python/2022/02/input.txt"

total_score = 0

# A Y -> rock, draw
# B X -> paper, lose


def calculate_response(opp_move, req_move):
    # If opponent choses rock
    if opp_move == 'A':
        if req_move == 'X':
            return 3
        elif req_move == 'Y':
            return 1
        else:
            return 2
    # If opponent choses paper
    elif opp_move == 'B':
        if req_move == 'X':
            return 1
        elif req_move == 'Y':
            return 2
        else:
            return 2
    elif opp_move == 'C':
        if req_move == 'X':
            return 2
        elif req_move == "Y":
            return 3
        else:
            return 1


with open(test_input, "r") as f:
    line = f.readline()
    while line:
        line = line.strip().replace(" ", "")
        opponent_move = line[0]
        required_move = line[1]
        total_score += calculate_response(opponent_move, required_move)
        line = f.readline()
print(total_score)
