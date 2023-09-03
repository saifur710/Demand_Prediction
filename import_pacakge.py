import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import re
import numpy as np
from plotnine import ggplot, aes, geom_line
import plotly.graph_objects as go
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima_model import ARIMA
from statsmodels.graphics.tsaplots import plot_pacf
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.tsa.arima_process import ArmaProcess
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import pacf
from statsmodels.tsa.stattools import acf
import os
import datetime as dt
from pandas.core.frame import DataFrame
