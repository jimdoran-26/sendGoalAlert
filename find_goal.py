def check_string_for_goal(str):
    if 'GOAL' in str:
        print(str)


def check_list_for_goals(lst):
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [lst[i]]
    print(goals[1::2])

def check_list_for_goals_elements(lst):
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [i]
    print(goals)