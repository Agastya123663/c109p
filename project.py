import statistics
import pandas as pd
import csv

df = pd.read_csv("project.csv")
read_list = df["reading score"].to_list()


mean = statistics.mean(read_list)
median = statistics.median(read_list)
mode = statistics.mode(read_list)

print("Mean : ",mean)
print("Median : ",median)
print("Mode : ",mode)

standard_deviation = statistics.stdev(read_list)


first_standard_deviation_start, first_standard_deviation_end = mean - standard_deviation, mean + standard_deviation
second_standard_deviation_start, second_standard_deviation_end = mean - (2*standard_deviation), mean+(2*standard_deviation)
third_standard_deviation_start, third_standard_deviation_end   = mean - (3*standard_deviation), mean+(3*standard_deviation)

list_of_data_within_first_standard_deviation = [result for result in read_list if result> first_standard_deviation_start and result< first_standard_deviation_end]
list_of_data_within_second_standard_deviation = [result for result in read_list if result> second_standard_deviation_start and result< second_standard_deviation_end]
list_of_data_within_third_standard_deviation = [result for result in read_list if result> third_standard_deviation_start and result< third_standard_deviation_end]

print("{}% Of Data Lies Within 1 Deviation".format(len(list_of_data_within_first_standard_deviation)*100/len(read_list)))
print("{}% Of Data Lies Within 2 Deviation".format(len(list_of_data_within_second_standard_deviation)*100/len(read_list)))
print("{}% Of Data Lies Within 3 Deviation".format(len(list_of_data_within_third_standard_deviation)*100/len(read_list)))