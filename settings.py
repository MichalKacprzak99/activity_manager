import pymongo

from pymongo import MongoClient
from PyQt5.QtWidgets import QMessageBox
root = MongoClient("localhost", 27017)
activity_adder_db = root['activity_adder_db']
user_activities = activity_adder_db['user_activities']
settings = activity_adder_db['settings']
options = ["time", "activity", "duration", "grade", "distance", "summary"]
road_to_master = [1, 5, 10, 20, 50, 100, 200, 500, 1000]


def sum_parameter(param: str, type_of_activity: str, coll_of_activity: pymongo.collection, period: int = 1) -> list:
    value_of_param = [daily_post[param] for daily_post in
                      coll_of_activity.find({"activity": type_of_activity}).sort("time")]

    def divide_list(list_to_divide: list, n: int):
        for i in range(0, len(list_to_divide), n):
            yield list_to_divide[i:i + n]

    value_of_param = list(divide_list(value_of_param, period))
    sum_in_duration = [sum(period) for period in value_of_param]
    return sum_in_duration


def longest_continuous_series(collection: pymongo.collection) -> int:
    date_daily_activity = [daily_post["time"] for daily_post in collection.find({}).sort("time")]
    difference_between_activity = [(date_daily_activity[i + 1] - date_daily_activity[i]).days for i in
                                   range(len(date_daily_activity[:-1]))]

    max_days = tmp = 0
    for diff in difference_between_activity:
        if diff in [0, 1]:
            tmp += 1
        else:
            if tmp > max_days:
                max_days = tmp
            tmp = 0
    return max_days


def check_if_current_goal_is_reached(type_of_activity: str, coll_of_activity: pymongo.collection,
                                     data_of_activities: pymongo.collection):
    number_of_reached_goals = 0
    for param in ["duration", "distance"]:
        current_goal = coll_of_activity.find_one({'activity': type_of_activity})['objective_' + str(param)]
        current_value = sum(sum_parameter(param, type_of_activity, data_of_activities))

        if current_value >= current_goal:
            number_of_reached_goals += 1
            next_goal = list(filter(lambda y: y > current_value, road_to_master))[0]
            coll_of_activity.update_one({'activity': type_of_activity},
                                        {"$set": {str('objective_' + param): next_goal}})
    if number_of_reached_goals > 0:
        msg = QMessageBox()
        msg.setWindowTitle("Achievements")
        msg.setText("You have completed {} challenges".format(number_of_reached_goals))
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(lambda: msg.exec_)
        x = msg.exec_()
