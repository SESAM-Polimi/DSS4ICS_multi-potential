# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:59:08 2024

@author: giacomocrevani
"""
import pandas as pd

def get_countries_to_compare(available_countries):
    available_countries = [str(country) for country in available_countries]
    print("Available countries:", ', '.join(available_countries))
    countries = input("\nEnter the countries to compare, separated by commas: ").split(',')
    countries = [country.strip() for country in countries]
    unrecognized_countries = [country for country in countries if country not in available_countries]
    if unrecognized_countries:
        print(f"Warning: The following countries are not recognized: {', '.join(unrecognized_countries)}")
    return countries

def filter_data_by_countries(df, countries):
    return df[df['Country'].isin(countries)]

def merge_data(techno_economic_data, regulatory_social_data, selected_countries):
    selected_techno_economic_data = filter_data_by_countries(techno_economic_data, selected_countries)
    selected_regulatory_social_data = filter_data_by_countries(regulatory_social_data, selected_countries)
    merged_data = pd.merge(selected_techno_economic_data, selected_regulatory_social_data, on='Country')
    return merged_data