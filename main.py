# main script
# Decision maker is a script calculating from a comparison report (https://github.com/fbonnier/file_comparison)
# some statistics in order to help or give a clue, an idea about the distance of two file contents.
# The distance is calculated using different algorithms.
# If it is possible, the maximum delta, the maximum distance between two data and the average distance between all comparable data
# are given

import os
import argparse
import json
import statistics

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

def get_delta_array_per_type (report_data):
    to_return = {"arithmetic": [], "levenshtein": []}
    for icouple in report_data:
        for item in icouple["differences"]:
            to_return[icouple["differences"][item]["type"]].append(icouple["differences"][item]["value"])

    return to_return


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
        # print ("Scores: " + str([item["score"] for item in report_data]))
        # list_of_scores = [float(item["score"]) for item in report_data]

        # 3: Build list of delta sorted by type (arithmetic, levenshtein distance)
        delta_per_type = get_delta_array_per_type (report_data)
        # print (delta_per_type)

        # 4-1: Arithmetic Statistics
        print ("===============================\n# Arithmetic\n===============================")
        print ("# Min value = " + str (min(delta_per_type["arithmetic"])))
        print ("# Max value = " + str (max(delta_per_type["arithmetic"])))
        print ("# Harmonic mean = " + str (statistics.harmonic_mean(delta_per_type["arithmetic"])))
        print ("# Mean (Average) = " + str (statistics.mean(delta_per_type["arithmetic"])))
        print ("# Median = " + str (statistics.median(delta_per_type["arithmetic"])))
        print ("# Median Low = " + str (statistics.median_low(delta_per_type["arithmetic"])))
        print ("# Median High = " + str (statistics.median_high(delta_per_type["arithmetic"])))
        print ("# Mode = " + str (statistics.mode(delta_per_type["arithmetic"])))
        print ("# Standard Deviation Population = " + str (statistics.pstdev(delta_per_type["arithmetic"])))
        print ("# Standard Deviation = " + str (statistics.stdev(delta_per_type["arithmetic"])))
        print ("# Population Variance = " + str (statistics.pvariance(delta_per_type["arithmetic"])))
        print ("# Variance = " + str (statistics.variance(delta_per_type["arithmetic"])))
        print ("===============================\n")

        # 4-2: Levenshtein Statistics
        print ("===============================\n# Levenshtein\n===============================")
        print ("# Min value = " + str (min(delta_per_type["levenshtein"])))
        print ("# Max value = " + str (max(delta_per_type["levenshtein"])))
        print ("# Harmonic mean = " + str (statistics.harmonic_mean(delta_per_type["levenshtein"])))
        print ("# Mean (Average) = " + str (statistics.mean(delta_per_type["levenshtein"])))
        print ("# Median = " + str (statistics.median(delta_per_type["levenshtein"])))
        print ("# Median Low = " + str (statistics.median_low(delta_per_type["levenshtein"])))
        print ("# Median High = " + str (statistics.median_high(delta_per_type["levenshtein"])))
        print ("# Mode = " + str (statistics.mode(delta_per_type["levenshtein"])))
        print ("# Standard Deviation Population = " + str (statistics.pstdev(delta_per_type["levenshtein"])))
        print ("# Standard Deviation = " + str (statistics.stdev(delta_per_type["levenshtein"])))
        print ("# Population Variance = " + str (statistics.pvariance(delta_per_type["levenshtein"])))
        print ("# Variance = " + str (statistics.variance(delta_per_type["levenshtein"])))
        print ("===============================\n")

        # 4-3: Key errors, missing data
        print ("===============================\n# Missing data\n===============================")
        print ("# Number of missing values = " + str (delta_per_type["missing"]))
        print ("===============================\n")


        # average_score = get_average_score (list_of_scores)
        # print ("Average Score: " + str(average_score))
        #
        # list_of_differences = [item["differences"] for item in report_data]
        # print ("Differences: " + str(list_of_differences))
        #
        # list_of_delta = []
        # for idiff in list_of_differences:
        #     print ("idiff: " + str(idiff))
        #     # list_of_delta.append(list_of_differences[idiff])
        # print ("Deltas: " + str(list_of_delta))



        # list_of_delta_max = get_delta_max (list_of_differences)
        # print ("Delta Max: " + str(list_of_delta_max))


        # list_of_scores = [report_data[idx]["score"] for idx in range(1, len(report_data))]
        # print (list_of_scores)
        # for idata in report_data:
        #     print (idata)


    exit (0)
