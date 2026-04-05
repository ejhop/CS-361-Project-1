#!/usr/bin/env python3
import numpy as np
import pandas as pd 
import mergesort as ms
import generateNumbers as gn
import sys
import time

#Load the file
def loader(filename):
    df = pd.read_csv(filename, sep=',')
    array = df.values.flatten()
    return array

def run_benchmarking(array):
    start_time = time.time()
    ms.threeWayMergeSort(array)
    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total_time run: {total_time}")

if __name__ == '__main__':
    if len(sys.argv) > 2:
        power = int(sys.argv[1])
        isfloat = bool(sys.argv[2])
    elif len(sys.argv) <= 2 and len(sys.argv) > 1:
        power = int(sys.argv[1])
        isfloat = False
    else:
        print("You need to supply at least the power argument")

    
    if isfloat==True:
        unsorted_numbers = f'random_data_2pow{power}_float.csv'
        sorted_numbers = f'sorted_data_2pow{power}_float.csv'
        gn.save_unique_randoms(unsorted_numbers, isfloat, power)
        array = loader(unsorted_numbers) 
        run_benchmarking(array)
        gn.save_to_file(array, sorted_numbers, batch_size=10000, total_numbers=pow(2,power))
    else:
        unsorted_numbers = f'random_data_2pow{power}.csv'
        sorted_numbers = f'sorted_data_2pow{power}.csv'
        gn.save_unique_randoms(unsorted_numbers, isfloat, power)
        array = loader(unsorted_numbers)
        run_benchmarking(array)
        gn.save_to_file(array, sorted_numbers, batch_size=10000, total_numbers=pow(2,power))
