# main script
# Decision maker is a script calculating from a comparison report (https://github.com/fbonnier/file_comparison)
# some statistics in order to help or give a clue, an idea about the distance of two file contents.
# The distance is calculated using different algorithms.
# If it is possible, the maximum delta, the maximum distance between two data and the average distance between all comparable data
# are given

import os
import argparse
import json
from Levenshtein import distance as lev

# class Delta:
#     distance = 0.
#     difference_method = ""
#
#     def __init__ (self, value1, value2):
#         try:
#             # Arithmetic distance for arithmetic types
#             self.distance = abs(value1 - value2)
#             self.difference_method = "arithmetic"
#         except:
#             try:
#                 # Levenshtein distance for strings
#                 self.distance = lev(value1, value2)
#                 self.difference_method = "levenshtein"
#             except Exception as e:
#                 print ("Delta computation: " + str(e))

def get_average_score (list_of_scores):
    assert len(list_of_scores) > 0, "List of scores empty"
    return sum(list_of_scores)/len(list_of_scores)

def get_delta_max (list_of_differences):
    list_of_deltas = []
    for icouple in list_of_differences:
        list_of_deltas.append(get_delta_max_1_file([float(icouple[ikey]) for ikey in icouple]))

    return list_of_deltas

def get_delta_max_1_file (list_of_deltas):
    return max (list_of_deltas)


if __name__ == "__main__":

    # 0: the report file is given as an entry
    parser = argparse.ArgumentParser(description='Computes file comparison using ')
    parser.add_argument('file', type=argparse.FileType('r'), metavar='file', nargs=1,
                        help='Report File to analyze')
    args = parser.parse_args()


    # 1: Open the JSON report containing differences and scores of two list of files
    with open (args.file[0].name, 'r') as report_file:
        report_data = json.load(report_file)

        # 2: Build the list of scores
        total_number_of_data = len(report_data)
        # print (report_data[1]["score"])
        print ("Scores: " + str([item["score"] for item in report_data]))

        list_of_scores = [float(item["score"]) for item in report_data]

        average_score = get_average_score (list_of_scores)
        print ("Average Score: " + str(average_score))

        list_of_differences = [item["differences"] for item in report_data]
        print ("Differences: " + str(list_of_differences))

        list_of_delta = []
        for idiff in list_of_differences:
            print ("idiff: " + str(idiff))
            # list_of_delta.append(list_of_differences[idiff])
        print ("Deltas: " + str(list_of_delta))



        # list_of_delta_max = get_delta_max (list_of_differences)
        # print ("Delta Max: " + str(list_of_delta_max))


        # list_of_scores = [report_data[idx]["score"] for idx in range(1, len(report_data))]
        # print (list_of_scores)
        # for idata in report_data:
        #     print (idata)


    exit (0)
