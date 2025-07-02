class simple_model:
    # import libraries
    import pandas as pd
    import matplotlib.pyplot as plt
    import yfinance as yf
    import numpy as np
    import mplfinance as mpf
    import ta
    import datetime

    
    def __init__(self,avg_pe=18,L=1,k=1):
        print("Initialize...")
        self.avg_pe = avg_pe
        self.L = L
        self.k =k

    def get_value_signal(self,pe):
        return 1-2*self.L/(1+np.exp(-self.k*(pe-self.avg_pe)))


        
    
