import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def read_data():
    col_name = 'Team TimeStamp Temperture Humidity Pressure PM1_0 PM2_5 PM10 CO2'.split()
    df = pd.read_csv(r"Data_txt_raw/14-7-2023 (raw-1hour-open door).txt", names=col_name)
    return df
def filter(df, condition=None):
    data = df[(df[condition]>0)][condition].dropna()
    data = data[(data[condition[-1]]<2000)].dropna()
    data = data[(data[condition[3]]<4294967295)].dropna()
    data = data[(data[condition[4]]<4294967295)].dropna()
    data = data[(data[condition[5]]<4294967295)].dropna()
    data_cp = data.copy()
    return (data, data_cp)
def cal_error(df, condition):
    list_error = []
    T = pow(10,10)
    thres = [T, T, T, 4294967295, 4294967295, 4294967295, 2000]
    for i in range(len(condition)):
        error = len(df[(df[condition[i]]>0) & (df[condition[i]] < thres[i])])/len(df)
        list_error.append(1-error)
    return list_error
def save_data(data, condition):
    folder = 'Data_excel/1hour'
    type='-1hour-close door'
    for i in range(data.shape[1]):
        name = condition[i] + type + '.csv'
        path_file = os.path.join(folder, name)
        data[condition[i]].to_csv(path_file, index=False)
def show_info(data,df, condition, list_error):
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
    condition = 'Temperture Humidity Pressure PM1_0 PM2_5 PM10 CO2'.split()
    df = read_data()
    data, data_cp = filter(df, condition)

    list_error = cal_error(df, condition)
    show_info(data_cp, df, condition, list_error)

    graph(data)
main()