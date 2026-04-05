import numpy as np
import pandas as pd
import os

def save_unique_randoms(filename, isfloat=False, powers=20):
    power = powers
    batch_size = 10000
    total_numbers = pow(2,power)
    high = pow(2,power)*2
    low = 0
    seed=42
    precision = 2
    filename = filename
    isfloat = isfloat


    rng = np.random.default_rng(seed)
     
    if isfloat == True:
        # Generate all unique float numnbers 
        scale_factor = 10**precision
        float_low = low * scale_factor
        float_high = high * scale_factor
        unique_integers = rng.choice(np.arange(float_low, float_high), size=total_numbers, replace=False)
        all_randoms = unique_integers.astype(float) / scale_factor
    else:
        #  Generate all unique numbers first to ensure global uniqueness
        all_randoms = rng.choice(np.arange(low, high), size=total_numbers, replace=False)
    save_to_file(all_randoms, filename, batch_size, total_numbers)

def save_to_file(all_randoms, filename, batch_size, total_numbers):
    batch_size = batch_size
    total_numbers = total_numbers
    for i in range(0, total_numbers, batch_size):
        batch = all_randoms[i:i + batch_size]
        df = pd.DataFrame(batch, columns=['unique_number'])
        
        # header=True only for the first batch
        if i == 0:
            df.to_csv(filename, mode='w', index=False, header=False)
        else:
            df.to_csv(filename, mode='a', index=False, header=False)

# Parameters
#filename = 'random_data_2pow20_float.csv'
#save_unique_randoms(
#    filename=filename,
#    total_numbers=pow(2,20),
#    batch_size=100000,
#    low=0,
#    high=pow(2,20)*2,
#    seed=42,
#    isfloat=True,
#    precision=2
#)
