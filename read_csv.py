#! /usr/bin/env python
# coding: utf-8

def check_time_diff(row_cnt, row):

    start_time = row[3]
    str_isofmt_time = datetime.datetime.fromisoformat(start_time)
    
    end_time = row[4]
    end_isofmt_time = datetime.datetime.fromisoformat(end_time)

    diff_time = end_isofmt_time - str_isofmt_time
    
    return diff_time

def update_time_diff(row_cnt, update_time, diff_time):

    if update_time < diff_time:

        return diff_time
    else:

        return update_time


import sys
import csv
import datetime

args = sys.argv
file_name = args[1]

row_cnt = 0
diff_time = 0
update_time = 0

with open('./' + file_name) as f:
    reader = csv.reader(f)
    for row in reader:
        if row_cnt == 0:
            pass
        else:
            diff_time = check_time_diff(row_cnt, row)
            if row_cnt == 1:
                update_time = diff_time
            
            update_time = update_time_diff (row_cnt, update_time, diff_time)

        row_cnt = row_cnt + 1
        
print (row_cnt)
