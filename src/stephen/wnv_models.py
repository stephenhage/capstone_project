import csv
import pathlib
import numpy as np
from sklearn import metrics
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.utils import np_utils

parentpath = pathlib.Path('../data/processed').resolve().parents[1]
dat_path = pathlib.Path('data/processed')
dat_path = parentpath / dat_path
noaa = pathlib.Path('noaa.weather.stations.csv')
wnv.trap = pathlib.Path('wnv.trap.csv')

noaa_dat = dat_path / noaa


class logistic_model(df, target):

    def __init__(self, data, y):
        self.data = data
        self.y = y

    def
