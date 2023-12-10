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
        data = pd.read_csv(txt_filepath, delimiter = "\s+" )
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


def plotting_for_single_alice(data, params):
    num_of_params = len(params)
    print('num_of_params = ', num_of_params)

    # Colors definitions
    c_red = [0.8, 0, 0]
    c_blue = [0, 0.3, 0.5]
    c_green = [0, 0.5, 0]

    # Line parameters
    line_width = 1
    grid_width = 0.5
    # Marker parameters
    marker_size = 10
    marker_size_on_line = 4

    # Labels
    x_name = 'Time points'

    text_for_graphs = ''

    fig1 = plt.figure(figsize=[8, 6])

    plt.subplots_adjust(wspace=0.4, hspace=0.4)
    plt.rcParams['font.size'] = '8'
    plt.rcParams['font.family'] = 'Arial'

    fig1.suptitle('QKD output parameters', fontsize=10)
    num_of_axs = num_of_params + 1
    print('num_of_axs = ', num_of_axs)

    for i in range(num_of_params):

        # Расчет средних значенийи СКО:
        p = params[i]
        data_p = data[p].to_numpy(na_value=0)
        print('param = ', p)
        print( '\ndata(p) = \n', data_p )
        mean_p = np.mean( data_p )
        SKO_p = np.std( data_p )
        text_for_graphs = text_for_graphs + p + ': \nmean = ' + str("%.2f" % mean_p) + '\nstandard deviation = ' + str("%.2f" % SKO_p) + '\n\n'

        print('i = ', i)
        ax = plt.subplot(num_of_axs, 1, i+1)
        ax.plot( data_p, color=c_blue, linestyle='--', linewidth=line_width)
        ax.set(ylabel=params[i])
        ax.grid(True, linestyle=':', linewidth=grid_width)
        ax.legend(['data'], loc='upper right')

    ax_Text = plt.subplot(num_of_axs, 1, num_of_axs)
    ax_Text.axis('off')
    ax_Text.text(0.1, 0.2, text_for_graphs, fontsize=10)


    return fig1










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

            data_proc_selected_alice = data_proc.get_group(alice_id_selected)  # Parameters for only one Alice if there are many ones
            qkd_params = data_proc_selected_alice.columns  # ALL the parameters of QKD in log
            main_window['-PARAM_LIST-'].update(values=qkd_params)

        elif event == '-PARAM_SELECT-':
            qkd_params_selected = values['-PARAM_LIST-']
            main_window['-PARAM_SELECTED_LIST-'].update(qkd_params_selected)
            print('Selected parameters for graph: \n', qkd_params_selected )

        # # Таблица с параметрами не работает
        # elif event == '-TO_TABLE-':
        #     print('Writing selected data to table')
        #     for i in range(len(qkd_params_selected)):
        #         main_window['-TABLE-'].update(values=data_proc_selected_alice[qkd_params_selected[i]])
        #     print('Table was filled with data')


        elif event == '-CLEAR-':
            input_data = pandas.DataFrame()

            alice_ID_list = []
            main_window['-ALICE_ID_LIST-'].update(values=alice_ID_list)

            alice_id_selected = ''
            main_window['-SELECTED_ID-'].update(alice_id_selected)

            qkd_params = []
            main_window['-PARAM_LIST-'].update(qkd_params)

            qkd_params_selected = []
            main_window['-PARAM_SELECTED_LIST-'].update(qkd_params_selected)

            print('Type of cleared input data is ', type(input_data))
            print('!!! Data cleared !!!')

        elif event == '-PLOT-':
            if qkd_params_selected == []:
                print('No selected parameters')
            else:
                # то можно строить график
                print('Selecting and processing to numpy ')

                print('Trying to plot selected parameters..')
                fig_graph = plotting_for_single_alice(data_proc_selected_alice, qkd_params_selected)
                plt.show()  # Отображаем графики











main_window.close()