# -*- coding: utf-8 -*-
"""
Created on Thu May  7 13:17:22 2020

@author: Qiu
"""

#install twint and nest_asyncio package first 
#pip install twint
#pip install nest_asyncio

import twint
import functools
import pandas as pd
from os.path import join
import os
import nest_asyncio

def run_tweet_scraping(output_file_path, username, callback, since = "2016-1-1 0:0:0"):
    c = twint.Config()
    c.Store_csv = True
    c.Debug = True
    #use the default format
    c.Since = since
    c.Hide_output = True
    c.Output = output_file_path
    c.Username = username
    twint.run.Search(c, callback=callback)

###callback function for error handling
def print_log(task, index, log_file_path):
    task_exception = task.exception()
    
    with open(log_file_path, "a") as log_file:
        if task_exception != None:
            log_file.write(f"Exception happend when running index {index}\nYou need restart from {index}\n")
            print(f"Exception happend when running index {index}\nYou need restart from index {index}", 
                  flush=True)
        else:
            log_file.write(f"Successfully Finished Index {index}\n")
            print(f"Successfully Finished Index {index}", flush=True)
        

def scrape_df(output_dir_path, output_log_path, df_path, start_index, end_index):
    df = pd.read_csv(df_path)
    names = df["full_name"]
    usernames = df["twitter"]
    nest_asyncio.apply()
    for i in range(start_index, end_index):
        print(f"running index {i}")
        file_name = f"{i} {names[i]}.csv"
        file_path = join(output_dir_path, file_name)
        if os.path.isfile(file_path):
            os.remove(file_path)
        run_tweet_scraping(file_path, usernames[i],
                              callback=functools.partial(print_log, index=i, log_file_path=output_log_path))
        

if __name__ == "__main__":
    ###TODO: fill in parameters######
    os.makedirs("test1")
    scrape_df("./test1", "./test1/log.txt", "scraping_list.csv", 587 , 687)
    print("###########Finished#################")
