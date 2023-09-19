import os
import cv2
import imutils
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import random
import pickle

from skimage.feature import hog
from sklearn.utils import shuffle
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
