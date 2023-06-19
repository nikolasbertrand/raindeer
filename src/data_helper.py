# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 15:02:04 2023

@author: timow
"""

import requests
import pandas as pd

download = False
merge = True

def download_txt_files(url_template, destination_folder, months):
    for number in months:
        url = url_template.format(number)
        response = requests.get(url)
        if response.status_code == 200:
            content = response.text
            filename = url.split("/")[-1]
            destination_path = f"{destination_folder}/{filename}"
            with open(destination_path, "w") as file:
                file.write(content)
            print(f"Downloaded '{filename}' to '{destination_path}'.")
        else:
            print(f"Failed to download the file for URL: {url}.")


# Example usage, please replace later when used as a helper:
url_template = "https://opendata.dwd.de/climate_environment/CDC/regional_averages_DE/monthly/air_temperature_mean/regional_averages_tm_{}.txt"  # Replace with the URL template containing '{}' as a placeholder for the number
destination_folder = "../data"  # Replace with the desired destination folder on your system
months = {'01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'}

if download == True:
    download_txt_files(url_template, destination_folder, months)

def generate_txt_names(base_name, iterator):
    txt_names = set()
    for i in iterator:
        txt_name = f"{base_name}{i}.txt"
        txt_names.add(txt_name)
    return txt_names


def merge_files_to_dataframe(filenames, skip_rows):
    data = []
    for filename in filenames:
        with open(filename, 'r') as file:
            for _ in range(skip_rows):
                next(file)  # Skip the specified number of rows
            for line in file:
                line = line.strip()  # Remove leading/trailing whitespace
                if line:
                    data.append(line.split())  # Split line into columns and append to data

    # Create DataFrame from the collected data
    df = pd.DataFrame(data)
    df.columns = [row_headers]
    
    return df


# Example usage:
txt_files = generate_txt_names('../data/regional_averages_tm_', months) #['../data/regional_averages_tm_01.txt', '../data/regional_averages_tm_02.txt', '../data/regional_averages_tm_03.txt']  # Replace with the paths to your TXT files
row_headers = ['Jahr', 'Monat', 'Brandenburg/Berlin', 'Brandenburg,Baden-Wuerttemberg', 'Bayern' , 'Hessen', 'Mecklenburg-Vorpommern', 'Niedersachsen', 'Niedersachsen/Hamburg/Bremen', 'Nordrhein-Westfalen', 'Rheinland-Pfalz', 'Schleswig-Holstein', 'Saarland', 'Sachsen', 'Sachsen-Anhalt', 'Thueringen/Sachsen-Anhalt', 'Thueringen', 'Deutschland']  # Replace with your desired header    

if merge == True:
    skip_rows = 3
    df = merge_files_to_dataframe(txt_files, skip_rows)
    print(df)
    df.to_csv("../data/regional_averages_tm_all.csv")

