import pandas as pd
import numpy as np
import qgrid
from IPython.display import Markdown
from tabulate import tabulate

table = pd.read_excel("https://mysnu-my.sharepoint.com/:x:/g/personal/kyeongsunkim_seoul_ac_kr/Ef3iWrinVHxCnDBumcnJsDEBzBBxGJNQDdcj8vNdf--g8Q?e=lqXCcM")

Markdown(tabulate(table))

qgrid.show_grid(table)