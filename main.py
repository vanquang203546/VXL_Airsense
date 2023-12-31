import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data(path_file, col_name):
    return pd.read_csv(path_file, names=col_name)
def filter(df, params):
    data = df[(df[params]>0)][params].dropna()
    data = data[(data[params[3]]<4294967295) & (data[params[4]]<4294967295) & (data[params[5]]<4294967295) & (data[params[-1]]<2000)].dropna()
    return (data, data.copy())
def cal_error(df, params):
    list_error = []
    T = pow(10,10)
    thres = [T, T, T, 4294967295, 4294967295, 4294967295, 2000]
    for i in range(len(params)):
        error = len(df[(df[params[i]]>0) & (df[params[i]] < thres[i])])/len(df)
        list_error.append(1-error)
    return list_error
def save_data(data, params, time, type, index=False):
    folder = 'Data_excel/{}'.format(time)
    type='-{}-{}'.format(time, type)
    for i in range(data.shape[1]):
        name_file = params[i] + type + '.csv'
        path_file = os.path.join(folder, name_file)
        data[params[i]].to_csv(path_file, index=index)
def show_info(data, df, params, list_error):
    data = data.values
    name_arg = 'Nhiệt độ,Độ ẩm,Áp suất,PM1_0,PM2_5,PM10,CO2'.split(',')
    for i in range(len(name_arg)):
        print('{:<10} trung bình: {:12.3f}'.format(name_arg[i], data[:,i].mean()))
    for i in range(len(name_arg)):
        print('{:<10} lỗi: {:12.2f} %'.format(name_arg[i], list_error[i]*100))
    print('Xác xuất lỗi trung bình: {:4.2f}%'.format(100 - len(data)/len(df)*100))
#Graph
def graph(data):
    data = data.values
    plt.figure()
    #temperture
    plt.subplot(2,3,1)
    plt.plot(data[:,0])
    plt.title('Temperture')
    plt.ylim(31, 34) 
    # plt.xlabel("Average Pulse")
    # plt.ylabel("Calorie Burnage")
    #humidity
    plt.subplot(2,3,2)
    plt.plot(data[:,1])
    plt.title('Humidity')
    plt.ylim(69, 74) 
    # plt.xlabel("Average Pulse")
    # plt.ylabel("n")
    # Pressure
    plt.subplot(2,3,3)
    plt.plot(data[:,-5])
    plt.title('Pressure')
    plt.ylim(99600, 99750)
    # plt.xlabel("Average Pulse")
    # plt.ylabel("Calorie Burnage") 
    # PM1_0
    plt.subplot(2,3,4)
    plt.title('PM')
    plt.plot(data[:,-4], label = 'PM 1.0')
    # PM2_5
    plt.plot(data[:,-3], label = 'PM 2.5')
    # PM10
    plt.plot(data[:,-2], label = 'PM 10')
    plt.ylim(10, 80)
    plt.legend()
    # CO2
    plt.subplot(2,3,5)
    plt.plot(data[:,-1])
    plt.title('CO2')
    # plt.xlabel("Average Pulse")
    # plt.ylabel("Calorie Burnage")

    #show
    plt.suptitle("AIR SENSE")
    plt.show()
def main():
    col_name = 'Team TimeStamp Temperture Humidity Pressure PM1_0 PM2_5 PM10 CO2'.split()
    params = 'Temperture Humidity Pressure PM1_0 PM2_5 PM10 CO2'.split()
    path_file = "Data_txt_raw/14-7-2023 (raw-1hour-open door).txt" #change path_file
    time = '1hour' #7days
    type = 'open door' #close door

    df = read_data(path_file, col_name)
    data, data_cp = filter(df, params)

    list_error = cal_error(df, params)
    # show_info(data_cp, df, params, list_error)

    # save_data(data_cp, params, time, type)
    # graph(data)
main()
#df: dataframe before use filters
#data: dataframe after use filters