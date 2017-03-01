# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 18:23:01 2017

@author: bjr21

Pandas and Quandl test
"""
import quandl

quandl.ApiConfig.api_key = "cJy6sPx-LBTxR5-HN_zU"

a = quandl.get("FRED/GDPPOT", authtoken="cJy6sPx-LBTxR5-HN_zU")