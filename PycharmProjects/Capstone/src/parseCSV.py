# import csv, json, xlrd
import pandas as pd
import numpy


def csvParse():
    df = pd.read_csv('schedule.csv', index_col=0)
    return df.to_json(orient='records')
