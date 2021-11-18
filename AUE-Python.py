import lib.PySimpleGUI as sg
from lib.AUConfig import AUConfig, GameHostOptions
from __version__ import __version__
from os import environ
from lib.data_indexes import hats_dict, skins_dict, visors_dict, pets_dict, nameplates_dict, color_indexes
import sys
import ctypes
from os import path
from lib.dataclass import find_files
from decimal import Decimal, getcontext

getcontext().prec = 3

# Allows for IDs and in-game names of itmes to be swapped and vise versa
hats_dict2 = {y:x for x,y in hats_dict.items()}
skins_dict2 = {y:x for x,y in skins_dict.items()}
visors_dict2 = {y:x for x,y in visors_dict.items()}
pets_dict2 = {y:x for x,y in pets_dict.items()}
nameplates_dict2 = {y:x for x,y in nameplates_dict.items()}


def resource_path(relative_path): # stolen from https://stackoverflow.com/a/13790741
	""" Get absolute path to resource, works for dev and for PyInstaller """
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = path.abspath(".")

	return path.join(base_path, relative_path)

sg.theme('defaultnomorenagging')   # Add a touch of color

menu_def = [["Help",["About"]]]

# All the stuff inside your window.
playerPrefs_tab = [
	[sg.Text('Username:',key="username_display"),sg.Input(key="username")],
	[sg.Text('Color',key="color_display"),sg.Combo(values=color_indexes,key="color")],
	[sg.Text('Hat:',key="hat_display"),sg.Combo(values=tuple(hats_dict.values()),key="hat")],
	[sg.Text('Skin:',key="skin_display"),sg.Combo(values=tuple(skins_dict.values()),key="skin")],
	[sg.Text('Visor:',key="visor_display"),sg.Combo(values=tuple(visors_dict.values()),key="visor")],
	[sg.Text('Pet:',key="pet_display"),sg.Combo(values=tuple(pets_dict.values()),key="pet")],
 	[sg.Text('Nameplate:',key="nameplate_display"),sg.Combo(values=tuple(nameplates_dict.values()),key="nameplate")],
]

gameHostOptions_tab = [
	[sg.Text("Max players:",key="maxplayers_display"),sg.Input(key="maxplayers",size=(10,None))],
	[sg.Text("Player speed:",key="playerspeed_display"),sg.Input(key="playerspeed",size=(10,None))],
	[sg.Text("Crewmate vision:",key="crewmatevision_display"),sg.Input(key="crewmatevision",size=(10,None))],
	[sg.Text("Imposter vision",key="impostervision_display"),sg.Input(key="impostervision",size=(10,None))],
	[sg.Text("Kill cooldown:",key="killcooldown_display"),sg.Input(key="killcooldown",size=(10,None))],
	[sg.Text("Common tasks:",key="commontasks_display"),sg.Input(key="commontasks",size=(10,None))],
	[sg.Text("Short tasks:",key="shorttasks_display"),sg.Input(key="shorttasks",size=(10,None))],
	[sg.Text("Long tasks:",key="longtasks_display"),sg.Input(key="longtasks",size=(10,None))],
]

playerStats2_tab = [ [sg.T("WIP")] ]

layout = [
	[sg.Menu(menu_def)],
	[sg.TabGroup([[
		sg.Tab('playerPrefs',playerPrefs_tab),sg.Tab('gameHostOptions',gameHostOptions_tab),sg.Tab('playerStats2',playerStats2_tab)
	]])],
	[sg.Input(key='file',visible=False,enable_events=True),sg.FolderBrowse(button_text="Open",initial_folder=fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us"),sg.Submit('Save',key="save")]
]

# Process is given app user model id of 'a.b.c.d', differentiating itself from the Python processs
if sys.platform == 'win32' and not sys.argv[0].endswith('.exe'):
	ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(f'AUEPython.AUEPython.AUEPython.{__version__}') # string is arbitrary

# Create the Window
window = sg.Window(f'Among Us Editor (v{__version__}) - Remake - By Vresod',layout,icon=resource_path("images/logo.ico"),finalize=True)

def update_window(window:sg.Window,prefsConfig:AUConfig,hostConfig:GameHostOptions):
	"""
	Undoubtedly one of the most bloated functions in the entire codebase. lmao
	"""
	window['username_display'].update(value=f"Username: {prefsConfig['lastPlayerName']}") 
	window['username'].update(value=prefsConfig['lastPlayerName'])
	window['color_display'].update(value=f"Color: {color_indexes[int(prefsConfig['colorConfig'])]}") 
	window['color'].update(value=color_indexes[int(prefsConfig['colorConfig'])])
	window['hat_display'].update(value=f"Hat: {hats_dict[prefsConfig['lastHat']]}") 
	window['hat'].update(value=hats_dict[prefsConfig['lastHat']])
	window['skin_display'].update(value=f"Skin: {skins_dict[prefsConfig['lastSkin']]}") 
	window['skin'].update(value=skins_dict[prefsConfig['lastSkin']])
	window['visor_display'].update(value=f"Visor: {visors_dict[prefsConfig['lastVisor']]}") 
	window['visor'].update(value=visors_dict[prefsConfig['lastVisor']])
	window['pet_display'].update(value=f"Pet: {pets_dict[prefsConfig['lastPet']]}")
	window['pet'].update(value=pets_dict[prefsConfig['lastPet']])
	window['nameplate_display'].update(value=f"Nameplate: {nameplates_dict[prefsConfig['lastNameplate']]}")
	window['nameplate'].update(value=nameplates_dict[prefsConfig['lastNameplate']])
	# maxplayers playerspeed crewmatevision impostervision killcooldown
	window['maxplayers_display'].update(value=f"Max players: {hostConfig['MaxPlayers']}")
	window['maxplayers'].update(value=hostConfig['MaxPlayers'])
	window['playerspeed_display'].update(value=f"Player speed: {hostConfig['PlayerSpeedMod']}")
	window['playerspeed'].update(value=hostConfig['PlayerSpeedMod'])
	window['crewmatevision_display'].update(value=f"Crewmate vision: {hostConfig['CrewLightMod']}")
	window['crewmatevision'].update(value=hostConfig['CrewLightMod'])
	window['impostervision_display'].update(value=f"Imposter vision: {hostConfig['ImposterLightMod']}")
	window['impostervision'].update(value=hostConfig['ImposterLightMod'])
	window['killcooldown_display'].update(value=f"Kill cooldown: {hostConfig['KillCooldown']}")
	window['killcooldown'].update(value=hostConfig['KillCooldown'])
	window['commontasks_display'].update(value=f"Common tasks: {hostConfig['NumCommonTasks']}")
	window['commontasks'].update(value=hostConfig['NumCommonTasks'])
	window['shorttasks_display'].update(value=f"Short tasks: {hostConfig['NumShortTasks']}")
	window['shorttasks'].update(value=hostConfig['NumShortTasks'])
	window['longtasks_display'].update(value=f"Long tasks: {hostConfig['NumLongTasks']}")
	window['longtasks'].update(value=hostConfig['NumLongTasks'])
	window.finalize()

if sys.platform == "win32":
	files = find_files(fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us") # epic games compatible
	prefsConfig = AUConfig(files.playerPrefs)
	hostConfig = GameHostOptions(files.gameHostOptions)
	update_window(window,prefsConfig,hostConfig)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		break
	print(f"{event=}\n{values=}")
	if event == "file":
		if values['file'] == '':
			continue
		files = find_files(values['file'])
		prefsConfig = AUConfig(files)
		hostConfig = GameHostOptions(files)
		update_window(window,prefsConfig,hostConfig)
	elif event == "save":
		prefsConfig['lastPlayerName'] = values['username'][:10] # Max username character length
		prefsConfig['colorConfig'] = color_indexes.index(values['color'])
		prefsConfig['lastHat'] = hats_dict2[values['hat']]
		prefsConfig['lastSkin'] = skins_dict2[values['skin']]
		prefsConfig['lastVisor'] = visors_dict2[values['visor']]
		prefsConfig['lastPet'] = pets_dict2[values['pet']]
		prefsConfig['lastNameplate'] = nameplates_dict2[values['nameplate']]
		prefsConfig.save()
		hostConfig['MaxPlayers'] = int(values['maxplayers'])
		hostConfig['PlayerSpeedMod'] = Decimal(values['playerspeed']).normalize()
		hostConfig['CrewLightMod'] = Decimal(values['crewmatevision']).normalize()
		hostConfig['ImposterLightMod'] = Decimal(values['impostervision']).normalize()
		hostConfig['KillCooldown'] = Decimal(values['killcooldown']).normalize()
		hostConfig['NumCommonTasks'] = int(values['commontasks'])
		hostConfig['NumShortTasks'] = int(values['shorttasks'])
		hostConfig['NumLongTasks'] = int(values['longtasks'])
		hostConfig.save()
		update_window(window,prefsConfig,hostConfig)
		sg.popup("Config saved!")
	elif event == 'About':
		help_popup = sg.Window('About AUE',[
			[sg.T("Among Us Editor")],
			[sg.T(f"v{__version__}")],
			[sg.Text("By Vresod (Vresod#3907) on Discord")],
			[sg.Button("Close")]
		]).read(close=True)

window.close()