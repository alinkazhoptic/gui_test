# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas.core.frame

import gui_description
import print_somewords
import PySimpleGUI as sg

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np

# *************** Python examples for test *****************
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('user')

if __name__ == '__main__':
    print_somewords.print_somewords('Test of function in other files, which are in the same folder with main')
    print('Test passed')

gui_description.success_gui_test()
# ***********************************************************


def read_csv(csv_filepath):
    data = pandas.DataFrame()   # initialization for exception errors when filepath is empty
    if csv_filepath == '':
        print('[LOG] [Err] File reading error: Filepath is empty or unknown')
    else:
        # *** Чтение csv файла:
        data = pd.read_csv(csv_filepath, delimiter=';')
        print('[LOG] Input csv table:\n', data)
        # print('Input data type is ', type(data))
    return data

def read_txt(txt_filepath):
    data = pandas.DataFrame()  # initialization for exception errors when filepath is empty
    if txt_filepath == '':
        print('[LOG] [Err] File reading error: Filepath is empty or unknown')
    else:
        # *** Чтение txt файла:
        data = pd.read_csv(txt_filepath, delimiter = "\s+" )  #delimiter = " "
        print('[LOG] Input txt table:\n', data)
        # print('Input data type is ', type(data))
    return data


def group_by_AliceID(data):    # *** Группировка по ID Алис ***
    # grouped_data = []
    alice_id_list = []  #инициализация
    if 'Alice ID' not in data.keys():
        alice_id0 = '0x0'
        data.loc[:,'Alice ID'] = alice_id0
        print('There isn\'t Alice ID, so it named', alice_id0)

    grouped_data = data.groupby('Alice ID')
    alice_id_list = list(grouped_data.groups.keys())
    print('Alice ID list: \n', alice_id_list)
    # Тут че-то надо дописать,  сделать сгруппированный массив при одной Адисе
    return grouped_data, alice_id_list


def get_parameters_list(data_id_grouped, IDx):
    print('Alice ID: ', IDx)
    data_single_id = data_id_grouped.get_group(IDx)
    parameters_list = data_single_id.columns
    print('List of parameters for Alice', str(IDx), ': \n', parameters_list)
    return data_single_id, parameters_list

# def data_processing(data):
    # Эта функция бесполезна, надо сделать функцию, которая вытаскивает параметры для конкретной Алисы, входные данные - ID Алисы, выходные - список параметров, которые отображать в интерфейсе
    # data_proc = data
    # *** Группировка по ID Алис ***
    # if 'Alice ID' in data.keys():
    #     data_grouped_id, alice_ids = group_by_AliceID(data)
        # for idx in alice_ids:
        #     print('Alice ID: ', idx)
        #     data_id = data_grouped_id.get_group(idx)
        #     parameters_list = data_id.columns
        #     print('List of parameters for Alice', str(idx), ': \n', parameters_list)
    # else:
    #     alice_id0 = '0x0'
    #     alice_ids = [alice_id0]
        # print('There isn\'t Alice ID, so it named', alice_id0)
        # data_id0 = data
        # parameters_list = data_id0.columns
        # print('List of parameters for alone Alice', str(alice_id0), ': \n', parameters_list)

    # return data_proc, alice_ids, parameters_list

# def plotting_for_single_alice(data, id_num)
#     data_id = data.get_group(idx)



# Initialization
filepath = ''
# input_data = []
input_data = pandas.DataFrame()
alice_id_selected = ''
qkd_params = []
qkd_params_selected = []

main_window = gui_description.make_gui_window()

# Show window
while True:  # The Event Loop
    event, values = main_window.read()
    print('[LOG] Initialization:')
    print('Init input_data:\n', input_data)
    print('Type of init input data is ', type(input_data))

    print('event ', event, 'Values', values)     # debug
    # if event in (None, sg.WIN_CLOSED, 'Exit', 'Cancel'):
    #     break
    if event == sg.WIN_CLOSED:
        break
    if event in ('Exit', '-CANCEL-'):
        print('[LOG] EXIT or CANCEL Clicked')
        break
    else:
        print('_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_\n! Event = ', event, ' !')
        # print('--- Values Dictionary (key = value) ---')
        # for key in values:
        #     print(key, ' = ', values[key])

        if event == '-READ-':
            alice_ID_list = [] # очистка поля ID на всякий случай
            qkd_params = [] # очистка поля параметров на всякий случай
            filepath = values['-FILEPATH-']
            if filepath == '':
                print('[LOG] [Err] File reading error: Filepath is empty or unknown')
            elif 'csv' in filepath:
                input_data = read_csv(filepath)
            elif ('txt' in filepath) or ('dat' in filepath):
                input_data = read_txt(filepath)

            if input_data.empty:
                print('Input data is empty')
            else:
                data_proc, alice_ID_list = group_by_AliceID(input_data)
                # print(data_proc)
            main_window['-ALICE_ID_LIST-'].update(values=alice_ID_list)
            main_window['-PARAM_LIST-'].update(values=qkd_params)

        elif event == '-ID_SELECT-':
            alice_id_selected = values['-ALICE_ID_LIST-']
            alice_id_selected = alice_id_selected[0]
            print('Selected Alice ID ', alice_id_selected)
            print('Type is ', type(alice_id_selected))
            main_window['-SELECTED_ID-'].update(alice_id_selected)
            data_proc_selected_alice = data_proc.get_group(alice_id_selected)
            qkd_params = data_proc_selected_alice.columns
            main_window['-PARAM_LIST-'].update(values=qkd_params)

        elif event == '-PARAM_SELECT-':
            qkd_params_selected = values['-PARAM_LIST-']
            print('Selected parameters for graph: \n', qkd_params_selected )

        elif event == '-CLEAR-':
            input_data = pandas.DataFrame()
            print('Type of cleared input data is ', type(input_data))
            print('!!! Data cleared !!!')

        elif event == '-PLOT-':
            if qkd_params_selected == []:
                print('No selected parameters')
            else:
                # то можно строить график
                print('Trying to plot selected parameters..')
                for idx in alice_id_selected:
                    plotting_for_single_alice(data_proc, idx)










main_window.close()