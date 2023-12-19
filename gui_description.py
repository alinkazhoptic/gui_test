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
text_font_small = 'SegoeUI 9'  # for not so valuable things
text_font_big = 'SegoeUI 12'  # for headers

# Sizes definitions
checkbox_size = (15)
listbox_size = (15,4)
menu_def = [['&File', ['Something']], ['&Help', ['&About']]]  # Menu string format
pad_size = (16,4)
button_big_size = (10,1)
multiline_size = (15, 8)

# Colors definitions
c_red = [0.8, 0, 0]
c_blue = [0, 0.3, 0.5]
c_green = [0, 0.5, 0]
but_green = [0, 0.8, 0]


table_data = []
table_headings = []

# Window description
def make_gui_window():
    layout = [
        [ sg.Menu(menu_def, key='-MENU LINE-') ],

        [ sg.Text(text='STEP 1 - Open log file', justification='center', font=text_font_big)],

        [ sg.Text('Log file (csv/dat):', font=text_font),
          sg.InputText(key='-FILEPATH-', font=text_font_small, size=(50,10), expand_x=True),
          sg.FileBrowse(file_types=[("*.dat", "*.dat*"), ("*.csv", "*.csv*")], font=text_font, auto_size_button=True) ],

        [ sg.Button(key='-READ-', button_text='Read', font=text_font, pad=pad_size) ],

        [ sg.HorizontalSeparator(color='grey') ],

        # *** Alice ID ***
        [sg.Text(text='STEP 2 - Choose Alice ID', justification='center', font=text_font_big)],

        [ sg.Text('Alice IDs in log:')],
        # [ sg.Listbox(key='-ALICE_ID_LIST-', values=[],font=text_font_small, size=listbox_size, expand_x=False, expand_y=True, select_mode='single', change_submits=False),
        [ sg.Combo(key='-ALICE_ID_COMBO-', values=[], default_value='Select ...', readonly=False, size=(10, 2)),
          sg.Button(key='-ID_SELECT-', button_text='>> Select Alice ID >>', font=text_font, disabled=True, pad=pad_size),
          sg.InputText(key='-SELECTED_ID-', default_text='No selected ID', font=text_font_small, size=(10, 2), expand_x=False, disabled=True, use_readonly_for_disable=True),
          ],
        [sg.Frame(title='',
                  layout=[[sg.Button(key='-CLEAR-', button_text='Clear', font=text_font, pad=pad_size, button_color='coral', size=button_big_size)]],
                  border_width=0,
                  expand_x=True,
                  element_justification='right')
         ],

        [sg.HorizontalSeparator(color='grey')],

        # *** Parameters ***
        [sg.Text(text='STEP 3 - Choose parameters', justification='center', font=text_font_big)],

        [ sg.Text('Parameters for plotting:') ],
        [ sg.Listbox(key='-PARAM_LIST-', values=[],font=text_font_small, size=listbox_size, expand_x=True, expand_y=True, select_mode='multiple', change_submits=False),
          sg.Button(key='-PARAM_SELECT-', button_text='>> Select parameters >>', font=text_font, disabled=True),
          sg.Multiline(key='-PARAM_SELECTED_LIST-', default_text='', font=text_font_small, size=multiline_size, expand_x=True, disabled=True),
          ],


        [sg.HorizontalSeparator(color='grey')],

        # *** PLOT ***
        [sg.Text(text='STEP 4 - Plot', justification='center', font=text_font_big)],
        [sg.Frame(title='',
                  layout=[[sg.Button(key='-PLOT-', button_text='PLOT', font=text_font, button_color='darkcyan', disabled=True, size=button_big_size)]],
                  border_width=0,
                  expand_x=True,
                  element_justification='center')],
        # [sg.Button(key='-PLOT-', button_text='PLOT', font=text_font, button_color='green', disabled=True, size=(10,2), target=(5,5))],


        [sg.HorizontalSeparator(color='grey')],

        # *** LOG Actions ***
        [sg.Text(text='Actions', justification='center', font=text_font_big)],
        [ sg.Text('Actions log:', expand_x=True)],
        [ sg.Multiline(size=multiline_size, font='Courier 7', expand_x=True, expand_y=True, write_only=True, reroute_stdout=True,
                       reroute_stderr=True, reroute_cprint=True, echo_stdout_stderr=True, autoscroll=True, auto_refresh=True)],




        [ sg.Cancel(key='-CANCEL-', button_text='EXIT', font=text_font, button_color='indianred', size=button_big_size) ]
    ]
    layout[-1].append(sg.Sizegrip())

    gui_window = sg.Window('CSV reader', layout, grab_anywhere=True, resizable=True)

    return gui_window

