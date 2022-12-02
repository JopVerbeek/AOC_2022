with open('input.txt') as f:
    turns = [turn.split(' ') for turn in f.read().splitlines()]

wins = [
    ('C', 'X'),
    ('A', 'Y'),
    ('B', 'Z')
]

draw = [
    ('A', 'X'),
    ('B', 'Y'),
    ('C', 'Z')
]

points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

win_draw_lose = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

find_choice = {
    'win': {'C': 'X',
            'A': 'Y',
            'B': 'Z'},

    'draw': {'A': 'X',
             'B': 'Y',
             'C': 'Z'},

    'lose': {'A': 'Z',
             'B': 'X',
             'C': 'Y'}
}

scores = {
    'win': 6,
    'draw': 3,
    'lose': 0
}

def Q1(turns):
    counter = 0
    for turn in turns:
        opponent, me = turn
        counter += points[me]

        if (opponent, me) in wins:
            counter += 6

        elif (opponent, me) in draw:
            counter += 3

    return counter

def Q2(turns):
    counter = 0
    for turn in turns:
        opponent, me = turn        
        strat = win_draw_lose[me]        
        choice_points = points[find_choice[strat][opponent]]     
        w_d_l = scores[strat]
        counter += choice_points + w_d_l

    return counter


if __name__ == '__main__':
    print(Q1(turns))
    print(Q2(turns))



   


