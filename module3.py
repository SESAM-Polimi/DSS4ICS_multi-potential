# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:59:47 2024

@author: giacomocrevani
"""

import plotly.graph_objects as go
import numpy as np
import plotly.io as pio
import os

# Set default renderer
pio.renderers.default = 'browser'

# Calculate the normalized pairwise comparison matrix
def normalize_matrix(matrix):
    column_sums = np.sum(matrix, axis=0)
    normalized_matrix = matrix / column_sums
    return normalized_matrix

# Calculate the priority vector
def calculate_priority_vector(normalized_matrix):
    priority_vector = np.mean(normalized_matrix, axis=1)
    return priority_vector

# Calculate the consistency index (CI)
def calculate_consistency_index(matrix, priority_vector):
    lambda_max = np.mean(np.sum(matrix * priority_vector, axis=1) / priority_vector)
    n = matrix.shape[0]
    ci = (lambda_max - n) / (n - 1)
    return ci

# Calculate the consistency ratio (CR)
def calculate_consistency_ratio(ci, n):
    ri_values = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    ri = ri_values[n]
    cr = ci / ri
    return cr

# AHP process
def ahp(pairwise_matrix):
    normalized_matrix = normalize_matrix(pairwise_matrix)
    priority_vector = calculate_priority_vector(normalized_matrix)
    ci = calculate_consistency_index(pairwise_matrix, priority_vector)
    cr = calculate_consistency_ratio(ci, pairwise_matrix.shape[0])
    return priority_vector, ci, cr

def create_radar_chart(categories, data_dict, title, max_scale):
    fig = go.Figure()

    for country, values in data_dict.items():
        values_wrapped = values + values[:1]  # Closing the radar chart loop
        categories_wrapped = categories + categories[:1]  # Closing the radar chart loop
        
        fig.add_trace(go.Scatterpolar(
            r=values_wrapped,
            theta=categories_wrapped,
            fill='toself',
            name=country
        ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max_scale]  # Ensure the same scale for all countries
            )
        ),
        showlegend=True,
        title=title
    )

    # Create the "Results-comparison" folder if it doesn't exist
    results_folder = "Results-comparison"
    if not os.path.exists(results_folder):
        os.makedirs(results_folder)

    # Save plot as an HTML file in the "Results-comparison" folder
    plot_file = os.path.join(results_folder, f"{title.replace(' ', '_')}_radar_chart.html")
    fig.write_html(plot_file)
    print(f"Plot saved as {plot_file}")

    # Show plot
    fig.show()
