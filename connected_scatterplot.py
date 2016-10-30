# coding: utf-8

import matplotlib.pyplot as plt
import numpy as np
import csv

f = open('./csv/kyoto_kisyotyo.csv', 'r')
reader = csv.reader(f)
header = next(reader)
for row in reader:
    print row
