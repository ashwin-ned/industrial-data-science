# Code to explore the data
import os
import json
from matplotlib import pyplot as plt

def screw_data_loader(path):
    # Create two lists to hold all measurements (we focus on torque and time)
    all_torque_values = []
    all_time_values = []

    # Use the os module to get a list of all files in your path
    all_file_names_as_str = os.listdir(path)

    # Iterate all file names and use enumerate() to create an additional index
    for i, file_name in enumerate(all_file_names_as_str):

        # For every file name, load the file from json as dictionary
        with open(f"{path}/{file_name}") as file:
            # Use the json module to load the file
            json_as_dict = json.load(file)

            # Create two new empty lists to store individual screw runs [only a list]
            torque_values_of_step = []
            time_values_of_step = []

        # Iterate every step in the result list to get the "tightening steps"
        for step in json_as_dict["tightening steps"]:
            # Add these to our
            torque_values_of_step.extend(step["graph"]["torque values"])
            time_values_of_step.extend(step["graph"]["time values"])

        # Add the unpacked lists from the current screw step to our result lists
        all_torque_values.append(torque_values_of_step)
        all_time_values.append(time_values_of_step)

    return all_torque_values, all_time_values   