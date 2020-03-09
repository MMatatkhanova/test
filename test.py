#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np
import ipinfo

access_token = '1d76007112805d'

handler = ipinfo.getHandler(access_token)

def city(ip):
    return handler.getDetails(ip).city

dfs = pd.read_excel('test.xlsx', sheet_name='test')

dfs['f_ip']=dfs['ips'].str.split(',',  expand=True)[0]

df=dfs[['device_id','login','bank','device_fingerprint','f_ip']]

df['city']=df['f_ip'].apply(lambda x:city(x))

lg=list(set(df[df.device_id=='91b12379-8098-457f-a2ad-a94d767797c2'].login.tolist()))

ip=list(set(df[df.device_id=='91b12379-8098-457f-a2ad-a94d767797c2'].f_ip.tolist()))

cities=list(set(df[df.device_id=='91b12379-8098-457f-a2ad-a94d767797c2'].city.tolist()))

dfp=list(set(df[df.device_id=='91b12379-8098-457f-a2ad-a94d767797c2'].device_fingerprint.tolist()))

df1=df[df.device_id=='91b12379-8098-457f-a2ad-a94d767797c2']

df2=df[(df.login.isin(lg))&(df.login!='-')]

df3=df[df.f_ip.isin(ip)]

df4=df[df.city.isin(cities)]

df5=df[(df.device_fingerprint.isin(dfp))&(df.device_fingerprint!='No data')]

union = pd.concat([df1, df2])

union = pd.concat([union, df3])

union = pd.concat([union, df5])

union.drop_duplicates(inplace=True)

dev=list(set(df[df.login=='0007f265568f1abc1da791e852877df2047b3af9'].device_id.tolist()))

dfp=list(set(df[df.login=='0007f265568f1abc1da791e852877df2047b3af9'].device_fingerprint.tolist()))

ip=list(set(df[df.login=='0007f265568f1abc1da791e852877df2047b3af9'].f_ip.tolist()))

cities=list(set(df[df.login=='0007f265568f1abc1da791e852877df2047b3af9'].city.tolist()))

df1=df[df.login=='0007f265568f1abc1da791e852877df2047b3af9']

df2=df[df.device_id.isin(dev)]

df3=df[df.device_fingerprint.isin(dfp)&(df.device_fingerprint!='No data')]

df4=df[df.f_ip.isin(ip)]

df5=df[df.city.isin(cities)]

union1 = pd.concat([df1, df2])

union1 = pd.concat([union1, df3])

union1 = pd.concat([union1, df4])

union1.drop_duplicates(inplace=True)

f1=union['login'].tolist()

f2=union1['login'].tolist()

fin=f1+f2

fin=list(set(fin))

fin.remove('-')

df = pd.DataFrame({'login':fin})

df.to_csv('out.csv')

print(df)




