from find_goal import *


def create_message(lst,goal_num):

    messages=check_list_for_goals(lst)
    times=get_goal_times(lst)
    scores=get_goal_scores(lst)

    print(messages[goal_num-1]+'\n'+'Time: '+times[goal_num-1]+'\n'+'Score: '+scores[goal_num-1])






    #print(list_of_data)
