from get_data import *
from find_goal import *
from create_text import *

URL = "https://stevensducks.com/sports/mens-soccer/stats/2021/no-23-ithaca-college/boxscore/13121"
GAP = 10

def main():
    #get_data(URL)
    #check_string_for_goal('GOAL by STEVENS Cristiano Hocken (FIRST GOAL), Assist by Adam Silva.')
    #check_list_for_goals(get_data(URL))
    #get_goal_times(get_data(URL))
    #get_goal_scores(get_data(URL))
    create_message(get_data(URL),1)

if __name__ == "__main__":
    main()