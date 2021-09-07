def check_string_for_goal(str):
    if 'GOAL' in str:
        print(str)


def check_list_for_goals(lst):
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [lst[i]]
    print(goals[1::2])

def get_goal_times(lst):
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [lst[i-1]]
    times=goals[0::2]
    print(times)

def get_goal_scores(lst):
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [lst[i-1]]
    score=goals[1::2]
    print(score)


def check_list_for_goals_elements(lst):
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [i]
    print(goals)