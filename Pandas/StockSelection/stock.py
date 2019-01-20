#!/usr/bin/env python
# -*- coding: utf-8 -*-
__version__ = '1.0.0.0'

import pandas as pd
import numpy as np
import os

df_all = []

def handle(file_name):
    df = pd.read_csv(file_name, encoding="gbk", usecols=[0, 1, 2, 3, 4, 5])
    if df.empty:
        return
    # df = df[df['成交量'] * df['成交价'] >= 1000000]
    df['成交量'] = df['成交量'].abs()
    df['金额(万元)'] = df['成交价'] * df['成交量']
    df1 = df.groupby(['委买ID', '委买量'], as_index = False)["金额(万元)"].sum()
    df1 = df1[df1['金额(万元)'] >= 1000000]
    print(df1.head(5))
    df_temp = df.drop_duplicates(['委买ID', '委买量'],  keep='first')[['委买ID',  '委买价', '委买量', '成交价', '时间']]
    print(df_temp.head(5))
    df3 = df.groupby(['委买ID', '委买量'], as_index = False)["成交量"].sum()
    print(df3.head(5))
    df = pd.merge(df_temp, df3,on=['委买ID', '委买量'])
    print(df.head(5))
    df = pd.merge(df, df1,on=['委买ID', '委买量'])
    print(df.head(5))
    if not df.empty:
        df["股票"] = "%s" % file_name.split(".")[0]
        df['金额(万元)'] = np.around(df['金额(万元)']/10000)
        df.sort_values('时间', ascending = True)
        print(df.head(5))
        columns = ['股票', '时间', '委买ID', '成交价', '委买价', '委买量', '成交量', '金额(万元)']
        #df_new = df.append([{"股票": file_name.split(".")[0]}], ignore_index=True)
        #df_new = df.append(pd.Series([np.nan]), ignore_index = True)
        df_new = df.append(pd.Series(), ignore_index = True)
        print(df_new.head(5))
        df_all.append(df_new)
        df.to_csv("result/R_" + file_name, encoding="gbk", index = False, columns=columns)


if __name__ == '__main__':
    # handle("300236.L2.csv")
    dirs = os.listdir(os.path.realpath(os.path.dirname(__file__)))
    result_dir = os.path.join(os.path.realpath(os.path.dirname(__file__)), "result")
    if not os.path.exists(result_dir):
        os.mkdir(result_dir)
    print(dirs)
    for item in dirs:
        if item.find("R_") == -1 and item.find("L2.csv") !=-1:
            handle(item)
    print(df_all[0])
    df_all_all = df_all[0]
    for item in df_all[1:]:
        df_all_all = df_all_all.append(item)
    columns = ['股票', '时间', '委买ID', '成交价', '委买价', '委买量', '成交量', '金额(万元)']
    df_all_all.to_csv("result/result.csv", encoding="gbk", index = False, columns=columns)
    #df_all_all = df_all_all[df_all_all['金额(万元)'] >= 300]
    df_all_all = df_all_all.fillna(-1)
    df_all_all = df_all_all[(df_all_all['金额(万元)'] >= 300)|(df_all_all['金额(万元)']==-1)]
    print(df_all_all.head(20))
    df_all_all['时间'] = df_all_all['时间'].astype('int')
    df_all_all.replace(-1, np.nan, inplace=True)
    print(df_all_all.head(20))
    df_all_all.to_csv("result/300.csv", encoding="gbk", index = False, columns=columns)

