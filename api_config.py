from nsetools import Nse
from pprint import pprint
import pandas as pd
nse = Nse()
infosys = nse.get_quote("INFY")
pprint(infosys)

