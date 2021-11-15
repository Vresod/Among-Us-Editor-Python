import PySimpleGUI as sg
from extra import AUConfig
from os import environ
from data_indexes import hats, skins_dict, visors, nameplates_dict, pets_dict, color_indexes
import sys
import ctypes
from os import path


# Allows for IDs and in-game names of itmes to be swapped and vise versa
pets_dict2 = {y:x for x,y in pets_dict.items()}
nameplates_dict2 = {y:x for x,y in nameplates_dict.items()}
skins_dict2 = {y:x for x,y in skins_dict.items()}


def resource_path(relative_path): # stolen from https://stackoverflow.com/a/13790741
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = path.abspath(".")

	return path.join(base_path, relative_path)


__version__ = "1.0"

sg.theme('GrayGrayGray')   # Add a touch of color

menu_def = [["Help",["About"]]]

# All the stuff inside your window.
layout = [
	[sg.Menu(menu_def)],
	[sg.Text('Username:',key="username_display"),sg.Input(key="username")],
	[sg.Text('Color',key="color_display"),sg.Combo(values=color_indexes,key="color")],
	[sg.Text('Hat:',key="hat_display"),sg.Combo(values=hats,key="hat")],
	[sg.Text('Skin:',key="skin_display"),sg.Combo(values=tuple(skins_dict.values()),key="skin")],
	[sg.Text('Visor:',key="visor_display"),sg.Combo(values=visors,key="visor")],
	[sg.Text('Pet:',key="pet_display"),sg.Combo(values=tuple(pets_dict.values()),key="pet")],
 	[sg.Text('Nameplate:',key="nameplate_display"),sg.Combo(values=tuple(nameplates_dict.values()),key="nameplate")],
	[sg.HorizontalSeparator()],
	[sg.Input(key='file',visible=False,enable_events=True),sg.FileBrowse(button_text="Open",initial_folder=fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us"),sg.Submit('Save',key="save")]
]

# Process is given app user model id of 'a.b.c.d', differentiating itself from the Python processs
if sys.platform.startswith('win') and sys.argv[0].endswith('.exe') == False:
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(f'AUEPython.AUEPython.AUEPython.{__version__}') # string is arbitrary

# Create the Window
window = sg.Window(f'Among Us Editor (v{__version__}) - Remake - By Vresod',layout,icon=resource_path("images/logo.ico"))

def update_window(window:sg.Window,config:AUConfig):
	window['username_display'].update(value=f"Username: {config['lastPlayerName']}") 
	window['username'].update(value=config['lastPlayerName'])
	window['color_display'].update(value=f"Color: {color_indexes[int(config['colorConfig'])]}") 
	window['color'].update(value=color_indexes[int(config['colorConfig'])])
	window['hat_display'].update(value=f"Hat: {config['lastHat']}") 
	window['hat'].update(value=config['lastHat'])
	window['skin_display'].update(value=f"Skin: {skins_dict[config['lastSkin']]}") 
	window['skin'].update(value=skins_dict[config['lastSkin']])
	window['visor_display'].update(value=f"Visor: {config['lastVisor']}") 
	window['visor'].update(value=config['lastVisor'])
	window['pet_display'].update(value=f"Pet: {pets_dict[config['lastPet']]}")
	window['pet'].update(value=pets_dict[config['lastPet']])
	window['nameplate_display'].update(value=f"Nameplate: {nameplates_dict[config['lastNameplate']]}")
	window['nameplate'].update(value=nameplates_dict[config['lastNameplate']])
	window.finalize()

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		break
	print(f"{event=}\n{values=}")
	if event == "file":
		if values['file'] == '':
			continue
		config = AUConfig(values['file'])
		update_window(window,config)
	elif event == "save":
		config['lastPlayerName'] = values['username']
		config['colorConfig'] = color_indexes.index(values['color'])
		config['lastHat'] = values['hat']
		config['lastSkin'] = skins_dict2[values['skin']]
		config['lastVisor'] = values['visor']
		config['lastPet'] = pets_dict2[values['pet']]
		print(values['pet'])
		config['lastNameplate'] = nameplates_dict2[values['nameplate']]
		config.save()
		update_window(window,config)
		sg.popup("Config saved!")
	elif event == 'About':
		help_popup = sg.Window('About AUE',[
			[sg.T("Among Us Editor")],
			[sg.T(f"v{__version__}")],
			[sg.T("By Vresod (Vresod#3907) on Discord")],
			[sg.Button("Close")]
		]).read(close=True)

window.close()