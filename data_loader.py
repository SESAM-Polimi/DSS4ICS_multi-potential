# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:57:54 2024

@author: giacomocrevani
"""

import pandas as pd

def load_module1(file_path):
    df = pd.read_excel(file_path, sheet_name='Module1')
    return df

def load_module2(file_path):
    df = pd.read_excel(file_path, sheet_name='Module2')
    return df