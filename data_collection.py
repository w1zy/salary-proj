# -*- coding: utf-8 -*-
"""
Created on Sun May 28 18:25:37 2023

@author: Shruti
"""

import glassdoor_scraper as gs
import pandas as pd


df = gs.get_jobs('data scientist', 15, False)
df
