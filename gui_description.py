# This is a sample Python script.
import PySimpleGUI as sg
import ctypes
import platform

# Проверка что библиотека грузится
def success_gui_test():
    print('Successful PySimpleGUI import')

# Функция изменение разрешения (масштабирование в зависимости от разрешения экрана)
def make_dpi_aware():
    if int(platform.release()) >= 8:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)

# Применение учета разрешения экрана при масштабировании
make_dpi_aware()

# Style settings
sg.theme('GrayGrayGray')   # Add a little color to windows
# also good themes: 'DarkAmber', 'DarkGreen2', 'DarkGrey13', 'DarkGrey8', 'DarkTeal6', 'Default', 'Default1', 'GrayGrayGray', 'SystemDefaultForReal'
text_font = 'SegoeUI 10' # also checked 'Arial', 'Calibri', 'Isocpeur', 'Menlo',  number is a text size
text_font_small = 'SegoeUI 9' # for not so valuable things
checkbox_size = (15)
listbox_size = (15,4)
menu_def = [['&File', ['Something']], ['&Help', ['&About']]]  # Menu string format


# Window description
def make_gui_window():
    layout = [
        [ sg.Menu(menu_def, key='-MENU LINE-') ],

        [ sg.Text('Log file (csv/dat/txt):', font=text_font),
          sg.InputText(font=text_font_small, size=(50,10), expand_x=True, key='-FILEPATH-'),
          sg.FileBrowse(file_types=[("*.csv", "*.csv*"), ("*.txt", "*.txt*"), ("*.dat", "*.dat*")], font=text_font, auto_size_button=True) ],  #, '*.dat', '*.dat*'

        [ sg.Button('Read', font=text_font, key='-READ-') ],
        # какой-то график непонятный пока
        # [ sg.Graph(canvas_size=(50,50), graph_bottom_left=(10,50), graph_top_right=(50,10), expand_x=True, expand_y=True, background_color='Black') ],
        [ sg.HorizontalSeparator(color='grey') ],
        # [ sg.Listbox(values=[1,2,3,4]) ],

        [ sg.Text('Alice IDs in log:')],
        [ sg.Listbox(values=[],font=text_font_small, size=listbox_size, expand_x=False, expand_y=True, select_mode='single', change_submits=False, key='-ALICE_ID_LIST-'),
          sg.Button('Select Alice ID >>>', font=text_font, key='-ID_SELECT-'),
          # sg.Text('>>>', font=text_font),
          sg.InputText(default_text='', font=text_font_small, size=(15, 10), expand_x=False, disabled=True, use_readonly_for_disable=True, key='-SELECTED_ID-')],

        [ sg.Text('Parameters for plotting:') ],
        [ sg.Listbox(values=[],font=text_font_small, size=listbox_size, expand_x=False, expand_y=True, select_mode='multiple', change_submits=False, key='-PARAM_LIST-')],
        [ sg.Button('Select parameters', font=text_font, key='-PARAM_SELECT-') ],

        [ sg.Text('Actions log:', expand_x=True)],
        [ sg.Multiline(size=(80,10), font='Courier 8', expand_x=True, expand_y=True, write_only=True, reroute_stdout=True,
                       reroute_stderr=True, reroute_cprint=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],

        [ sg.Button('Plot', font=text_font, key='-PLOT-') ],
        [ sg.Button('Clear', font=text_font, key='-CLEAR-') ],

        [ sg.Submit(font=text_font, key='-SUBMIT-'),
          sg.Cancel(font=text_font, key='-CANCEL-') ]
    ]
    layout[-1].append(sg.Sizegrip())

    gui_window = sg.Window('CSV reader', layout, grab_anywhere=True, resizable=True)

    return gui_window

