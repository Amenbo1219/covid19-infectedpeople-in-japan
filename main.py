import urllib.request
import datetime,os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def get_data(file,url):
    #該当URLからデータを取得する
    urllib.request.urlretrieve(url,file)
    # print("success!")
def make_dataframe(file):
    #入手したデータからデータフレームの作成
    df= pd.read_csv(file,header=0,index_col=0)
    return df
def pick_dataframe(df):
    # データフレームからデータシリーズを作成し、必要なデータを取り出す
    new_ds = df[df.Prefecture=='ALL']
    new_ds = new_ds['Newly confirmed cases']
    return new_ds
def pick_dataframe_minus(df):
    # データフレームからデータシリーズを作成し、必要なデータを取り出す
    # 累積データなので、一個前のデータを消すことを繰り返す
    # しかし、データがおかしいため実行不能
    new_ds = df[df.Prefecture=='ALL']
    new_ds = new_ds['Newly confirmed cases'].astype(int)
    # print(new_ds)
    new_ds[1::1] -= new_ds[1:-1:1]
    
    # print(new_ds)
    return new_ds
def wirte_dataframe(ds,file):
    # データをcsvで書き出す
    df = pd.DataFrame(ds)
    df.to_csv(path_or_buf=file)

def make_processdata(ds):
    # データから日時とデータに分ける
    date = ds.index
    values=ds.values
    # print(date[1])
    # print(values[1])
    return date,values
def make_graph(x,y,file=''):
    # グラフの生成
    date,value = make_processdata(ds)
    fig,ax = plt.subplots()
    ax.plot(x,y,label='infected')
    ax.set_xlim(0,len(x))
    ax.set_ylim(0,)
    ax.set_title('Covid-19 in Japan ')
    ax.set_xlabel('date')
    ax.set_ylabel('people')
    y = date[::30]
    step = (len(date)) // 5
    ax.set_xticks(date[0:len(date)+1:step])
    ax.legend()
    today = datetime.datetime.now()
    today = today.strftime('%Y-%m-%d')
    file = file + today + ".png"
    plt.savefig(file)

    # plt.show()

if __name__ == '__main__':

    url = 'https://covid19.mhlw.go.jp/public/opendata/newly_confirmed_cases_daily.csv'
    basefile = '/Users/intelmac/covid19/Numberofinfectedpeople/data/indectedpoeple.csv'
    temp = '/Users/intelmac/covid19/Numberofinfectedpeople/data/temp.csv'
    get_data(basefile,url)
    df=make_dataframe(basefile)
    ds = pick_dataframe(df)
    wirte_dataframe(ds,temp)
    date,value = make_processdata(ds)
    result = '/Users/intelmac/covid19/Numberofinfectedpeople/result/infected'
    make_graph(date,value,result)

    ##ソースのデータがおかしいのでこれで処理終わりにする。
    # url1 = 'https://covid19.mhlw.go.jp/public/opendata/deaths_cumulative_daily.csv'
    # file1 ='/Users/m1mac/MyFavorite/Python/covid19/Numberofinfectedpeople/data/death.csv'
    # get_data(file1,url)
    # df=make_dataframe(file1)
    # ds = pick_dataframe_minus(df)
    # file2 = '/Users/m1mac/MyFavorite/Python/covid19/Numberofinfectedpeople/data/temp2.csv'
    # wirte_dataframe(ds,file2)


    

