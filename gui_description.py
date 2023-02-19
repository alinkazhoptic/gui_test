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
sg.theme('SystemDefaultForReal')   # Add a little color to windows
# also good themes: 'DarkAmber', 'DarkGreen2', 'DarkGrey13', 'DarkGrey8', 'DarkTeal6', 'Default', 'Default1', 'GrayGrayGray', 'SystemDefaultForReal'
text_font = 'SegoeUI 10' # also checked 'Arial', 'Calibri', 'Isocpeur', 'Menlo',  number is a text size
text_font_small = 'SegoeUI 9' # for not so valuable things
checkbox_size = (15)
menu_def = [['&File', ['Something']], ['&Help', ['&About']]]  # Menu string format


# Window description
def make_gui_window():
    layout = [
        [ sg.Menu(menu_def, key='-MENU LINE-') ],

        [ sg.Text('Log file (.csv):', font=text_font),
          sg.InputText(font=text_font_small, size=(50,10), expand_x=True, key='-FILEPATH-'),
          sg.FileBrowse(file_types=(('*.csv', '*.csv*'),), font=text_font, auto_size_button=True) ],

        [ sg.Button('Read', font=text_font, key='-READ-') ],
        # какой-то график непонятный пока
        # [ sg.Graph(canvas_size=(50,50), graph_bottom_left=(10,50), graph_top_right=(50,10), expand_x=True, expand_y=True, background_color='Black') ],
        [ sg.HorizontalSeparator(color='grey') ],
        # [ sg.Listbox(values=[1,2,3,4]) ],
        [ sg.Text('Parameters for plotting:') ],
        [ sg.Checkbox('QBER', font=text_font, size=checkbox_size, key='-QBER-', default=True)],
        [ sg.Checkbox('Piezo voltage', font=text_font, size=checkbox_size, key='-PIEZO-'), sg.Checkbox('Efficiency', font=text_font, size=checkbox_size, key='-EFFICIENCY-') ],
        [ sg.Checkbox('Visibility', font=text_font, size=checkbox_size, key='-VISIBILITY-'), sg.Checkbox('Secret key length', font=text_font, size=checkbox_size, key='-SECRET KEY-') ],
        [ sg.Text('List of parameters for plotting:') ],
        [ sg.Listbox(values=[],font=text_font_small, size=(30,10), expand_x=False, expand_y=True, select_mode='multiple', change_submits=False, key='-PARAM_LIST-') ],
        [ sg.Button('Select', font=text_font, key='-PARAM_SELECT-') ],

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

