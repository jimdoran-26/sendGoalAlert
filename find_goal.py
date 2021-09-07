def check_string_for_goal(str):
    #check if a string contains goal keyword
    if 'GOAL' in str:
        print(str)


def check_list_for_goals(lst):
    #return every string in a list that contains the word goal
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            if not (lst[i] in goals):
                goals += [lst[i]]
    return(goals)

def get_goal_times(lst):
    #get times of each goal
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [lst[i-1]]
    times=goals[0::2]
    return(times)

def get_goal_scores(lst):
    #get scores after each goal
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [lst[i-1]]
    score=goals[1::2]
    return(score)


def check_list_for_goals_elements(lst):
    #get the row in html that the goal is scored in
    goals = []
    for i in range(len(lst)):
        if lst[i].__contains__('GOAL'):
            goals += [i]
    return(goals)
