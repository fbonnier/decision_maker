# main script
# Decision maker is a script calculating from a comparison report (https://github.com/fbonnier/file_comparison)
# some statistics in order to help or give a clue, an idea about the distance of two file contents.
# The distance is calculated using different algorithms.
# If it is possible, the maximum delta, the maximum distance between two data and the average distance between all comparable data
# are given

import os
import argparse
import json

def get_average_score (list_of_scores):
    assert len(list_of_scores) > 0, "List empty"
    return sum(list_of_scores)/len(list_of_scores)


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
        total_number_of_data = report_data[0]
        print (total_number_of_data)
        # print (report_data[1]["score"])
        print ([report_data[idx]["score"] for idx in range(1, len(report_data))])
        # list_of_scores = [report_data[idx]["score"] for idx in range(1, len(report_data))]
        # print (list_of_scores)
        # for idata in report_data:
        #     print (idata)


    exit (0)
