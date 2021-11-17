import lib.PySimpleGUI as sg
from lib.AUConfig import AUConfig
from __version__ import __version__
from os import environ
from lib.data_indexes import hats_dict, skins_dict, visors_dict, pets_dict, nameplates_dict, color_indexes
import sys
import ctypes
from os import path


# Allows for IDs and in-game names of itmes to be swapped and vise versa
hats_dict2 = {y:x for x,y in hats_dict.items()}; hats = list(hats_dict.values()); hats.sort()
skins_dict2 = {y:x for x,y in skins_dict.items()}; skins = list(skins_dict.values()); skins.sort()
visors_dict2 = {y:x for x,y in visors_dict.items()}; visors = list(visors_dict.values()); visors.sort()
pets_dict2 = {y:x for x,y in pets_dict.items()}; pets = list(pets_dict.values()); pets.sort()
nameplates_dict2 = {y:x for x,y in nameplates_dict.items()}; nameplates = list(nameplates_dict.values()); nameplates.sort()


def resource_path(relative_path): # stolen from https://stackoverflow.com/a/13790741
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = path.abspath(".")

	return path.join(base_path, relative_path)

sg.theme('GrayGrayGray')   # Add a touch of color

menu_def = [["Help",["About"]]]

# All the stuff inside your window.
playerPrefs_tab = [
	[sg.Text('Username:',key="username_display"),sg.Input(key="username")],
	[sg.Text('Color',key="color_display"),sg.Combo(values=color_indexes,key="color")],
	[sg.Text('Hat:',key="hat_display"),sg.Combo(values=hats,key="hat")],
	[sg.Text('Skin:',key="skin_display"),sg.Combo(values=skins,key="skin")],
	[sg.Text('Visor:',key="visor_display"),sg.Combo(values=visors,key="visor")],
	[sg.Text('Pet:',key="pet_display"),sg.Combo(values=pets,key="pet")],
 	[sg.Text('Nameplate:',key="nameplate_display"),sg.Combo(values=nameplates,key="nameplate")],
]

gameHostOptions_tab = [
	[sg.T("WIP")]
]

playerStats2_tab = [
	[sg.T("WIP")]
]

layout = [
	[sg.Menu(menu_def)],
	[sg.TabGroup([[
		sg.Tab('playerPrefs',playerPrefs_tab),sg.Tab('gameHostOptions',gameHostOptions_tab),sg.Tab('playerStats2',playerStats2_tab)
	]])],
	[sg.HorizontalSeparator()],
	[sg.Input(key='file',visible=False,enable_events=True),sg.FileBrowse(button_text="Open",initial_folder=fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us"),sg.Submit('Save',key="save")]
]

# Process is given app user model id of 'a.b.c.d', differentiating itself from the Python processs
if sys.platform == 'win32' and not sys.argv[0].endswith('.exe'):
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(f'AUEPython.AUEPython.AUEPython.{__version__}') # string is arbitrary

# Create the Window
window = sg.Window(f'Among Us Editor (v{__version__}) - Remake - By Vresod',layout,icon=resource_path("images/logo.ico"),finalize=True)

def update_window(window:sg.Window,config:AUConfig):
	window['username_display'].update(value=f"Username: {config['lastPlayerName']}") 
	window['username'].update(value=config['lastPlayerName'])
	window['color_display'].update(value=f"Color: {color_indexes[int(config['colorConfig'])]}") 
	window['color'].update(value=color_indexes[int(config['colorConfig'])])
	window['hat_display'].update(value=f"Hat: {hats_dict[config['lastHat']]}") 
	window['hat'].update(value=hats_dict[config['lastHat']])
	window['skin_display'].update(value=f"Skin: {skins_dict[config['lastSkin']]}") 
	window['skin'].update(value=skins_dict[config['lastSkin']])
	window['visor_display'].update(value=f"Visor: {visors_dict[config['lastVisor']]}") 
	window['visor'].update(value=visors_dict[config['lastVisor']])
	window['pet_display'].update(value=f"Pet: {pets_dict[config['lastPet']]}")
	window['pet'].update(value=pets_dict[config['lastPet']])
	window['nameplate_display'].update(value=f"Nameplate: {nameplates_dict[config['lastNameplate']]}")
	window['nameplate'].update(value=nameplates_dict[config['lastNameplate']])
	window.finalize()

if sys.platform == "win32":
	from glob import glob
	playerPrefsPath = glob(fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us\*playerPrefs")[0] # epic games compatible
	config = AUConfig(playerPrefsPath)
	update_window(window,config)

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
		config['lastPlayerName'] = values['username'][:10] # Max username character length
		config['colorConfig'] = color_indexes.index(values['color'])
		config['lastHat'] = hats_dict2[values['hat']]
		config['lastSkin'] = skins_dict2[values['skin']]
		config['lastVisor'] = visors_dict2[values['visor']]
		config['lastPet'] = pets_dict2[values['pet']]
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