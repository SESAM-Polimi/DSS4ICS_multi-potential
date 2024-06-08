# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 15:47:13 2024

@author: giacomocrevani
"""

import pandas as pd
import numpy as np
from data_loader import *
from data_processor import *
from module3 import *

# Data loading
file_path = 'default_data.xlsx'
module1_data = load_module1(file_path)
module2_data = load_module2(file_path)
available_countries = module1_data['Country'].unique()

# User input for country selection
selected_countries = get_countries_to_compare(available_countries)

# Merge data based on selected countries
merged_potentials = merge_data(module1_data, module2_data, selected_countries)[['Country', 'fNRB [-]2', 'ER normalized', 'Social potential (lack of access to clean cooking)', 'Regulatory potential (RISE)']]
merged_potentials.columns = ['Country', 'Environmental potential', 'Techno-economic potential', 'Social potential', 'Regulatory potential']
potentials = ['Environmental potential', 'Techno-economic potential', 'Social potential', 'Regulatory potential']

# AHP weighting process
pairwise_matrix = np.zeros((len(potentials), len(potentials)))

for i in range(len(potentials)):
    for j in range(i + 1, len(potentials)):
        while True:
            weight = float(input(f"Enter the weight of {potentials[i]} compared to {potentials[j]}, on a 0 to 4 scale. Place 1 for all the comparisons if you consider the potentials to weight equally: "))
            pairwise_matrix[i, j] = weight
            pairwise_matrix[j, i] = 1 / weight
            break

np.fill_diagonal(pairwise_matrix, 1)
priority_vector, ci, cr = ahp(pairwise_matrix)

if cr < 0.1:
    print("Consistency Ratio (CR) is acceptable.")
else:
    print("Consistency Ratio (CR) is not acceptable. Please re-evaluate the pairwise comparisons.")

# Weights the potentials
weighted_potentials = merged_potentials.copy()  # Make a copy of the merged potentials
weight_vector = priority_vector/priority_vector.max()
weighted_potentials[potentials] *= weight_vector  # Weight the potentials using the priority vector
weighted_potentials['Country'] = merged_potentials['Country']
max_value = weighted_potentials[potentials].values.max()


# Prepare data for radar chart
data_dict = {}
for index, row in weighted_potentials.iterrows():
    values = row[potentials].values.tolist()
    print(f"Country: {row['Country']}, Values: {values}")  # Debugging line
    data_dict[row['Country']] = values

# Create and save the radar chart
create_radar_chart(potentials, data_dict, 'Country Comparison Radar Chart', max_value)
