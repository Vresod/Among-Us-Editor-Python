import lib.PySimpleGUI as sg
from lib.AUConfig import AUConfig, GameHostOptions, PlayerStats
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

sg.theme('defaultnomorenagging')   # Add a touch of color

menu_def = [["Help",["About"]]]

# All the stuff inside your window.
playerPrefs_tab = [
	[sg.Text('Username:',key="username_display"),sg.Push(),sg.Input(key="username",size=(20,None))],
	[sg.Text('Color',key="color_display"),sg.Push(),sg.Combo(values=color_indexes,key="color")],
	[sg.Text('Hat:',key="hat_display"),sg.Push(),sg.Combo(values=hats,key="hat")],
	[sg.Text('Skin:',key="skin_display"),sg.Push(),sg.Combo(values=skins,key="skin")],
	[sg.Text('Visor:',key="visor_display"),sg.Push(),sg.Combo(values=visors,key="visor")],
	[sg.Text('Pet:',key="pet_display"),sg.Push(),sg.Combo(values=pets,key="pet")],
	[sg.Text('Nameplate:',key="nameplate_display"),sg.Push(),sg.Combo(values=nameplates,key="nameplate")],
]

gameHostOptions_tab = [
	[sg.Text("Max players:",key="maxplayers_display"),sg.Push(),sg.Input(key="maxplayers",size=(10,None))],
	[sg.Text("Player speed:",key="playerspeed_display"),sg.Push(),sg.Input(key="playerspeed",size=(10,None))],
	[sg.Text("Crewmate vision:",key="crewmatevision_display"),sg.Push(),sg.Input(key="crewmatevision",size=(10,None))],
	[sg.Text("Imposter vision",key="impostervision_display"),sg.Push(),sg.Input(key="impostervision",size=(10,None))],
	[sg.Text("Kill cooldown:",key="killcooldown_display"),sg.Push(),sg.Input(key="killcooldown",size=(10,None))],
	[sg.Text("Common tasks:",key="commontasks_display"),sg.Push(),sg.Input(key="commontasks",size=(10,None))],
	[sg.Text("Short tasks:",key="shorttasks_display"),sg.Push(),sg.Input(key="shorttasks",size=(10,None))],
	[sg.Text("Long tasks:",key="longtasks_display"),sg.Push(),sg.Input(key="longtasks",size=(10,None))],
]

playerStats2_column = [
	[sg.Text('Bodies reported:',key="bodiesreported_display"),sg.Push(),sg.Input(key="bodiesreported",size=(10,None))],
	[sg.Text('Emergencies called:',key="emergenciescalled_display"),sg.Push(),sg.Input(key="emergenciescalled",size=(10,None))],
	[sg.Text('Tasks completed:',key="taskscompleted_display"),sg.Push(),sg.Input(key="taskscompleted",size=(10,None))],
	[sg.Text('All tasks completed:',key="alltaskscompleted_display"),sg.Push(),sg.Input(key="alltaskscompleted",size=(10,None))],
	[sg.Text('Sabotages fixed:',key="sabotagesfixed_display"),sg.Push(),sg.Input(key="sabotagesfixed",size=(10,None))],
	[sg.Text('Imposter kills:',key="imposterkills_display"),sg.Push(),sg.Input(key="imposterkills",size=(10,None))],
	[sg.Text('Times murdered:',key="timesmurdered_display"),sg.Push(),sg.Input(key="timesmurdered",size=(10,None))],
	[sg.Text('Times ejected:',key="timesejected_display"),sg.Push(),sg.Input(key="timesejected",size=(10,None))],
	[sg.Text('Crewmate streak:',key="crewmatestreak_display"),sg.Push(),sg.Input(key="crewmatestreak",size=(10,None))],
	[sg.Text('Times imposter:',key="timesimposter_display"),sg.Push(),sg.Input(key="timesimposter",size=(10,None))],
	[sg.Text('Times crewmate:',key="timescrewmate_display"),sg.Push(),sg.Input(key="timescrewmate",size=(10,None))],
	[sg.Text('Games started:',key="gamesstarted_display"),sg.Push(),sg.Input(key="gamesstarted",size=(10,None))],
	[sg.Text('Games finished:',key="gamesfinished_display"),sg.Push(),sg.Input(key="gamesfinished",size=(10,None))],
	[sg.Text('Imposter vote wins:',key="impostervotewins_display"),sg.Push(),sg.Input(key="impostervotewins",size=(10,None))],
	[sg.Text('Imposter kill wins:',key="imposterkillwins_display"),sg.Push(),sg.Input(key="imposterkillwins",size=(10,None))],
	[sg.Text('Imposter sabotage wins:',key="impostersabotagewins_display"),sg.Push(),sg.Input(key="impostersabotagewins",size=(10,None))],
	[sg.Text('Crewmate vote wins:',key="crewmatevotewins_display"),sg.Push(),sg.Input(key="crewmatevotewins",size=(10,None))],
	[sg.Text('Crewmate task wins:',key="crewmatetaskwins_display"),sg.Push(),sg.Input(key="crewmatetaskwins",size=(10,None))],
]

playerStats2_tab = [[sg.Column(playerStats2_column,scrollable=True,expand_x=True,size=(None,200),vertical_scroll_only=True)]]

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

def update_window(window:sg.Window,prefsConfig:AUConfig,hostConfig:GameHostOptions,statsConfig:PlayerStats):
	"""
	Undoubtedly one of the most bloated functions in the entire codebase. lmao
	""" # Now it's even more bloated thanks to playerStats2 ;)
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
	# playerStats2
	window['bodiesreported_display'].update(value=f"Bodies reported: {statsConfig['BodiesReported']}")
	window['bodiesreported'].update(value=statsConfig['BodiesReported'])
	window['emergenciescalled_display'].update(value=f"Emergencies called: {statsConfig['EmergenciesCalled']}")
	window['emergenciescalled'].update(value=statsConfig['EmergenciesCalled'])
	window['taskscompleted_display'].update(value=f"Tasks completed: {statsConfig['TasksCompleted']}")
	window['taskscompleted'].update(value=statsConfig['TasksCompleted'])
	window['alltaskscompleted_display'].update(value=f"All tasks completed: {statsConfig['AllTasksCompleted']}")
	window['alltaskscompleted'].update(value=statsConfig['AllTasksCompleted'])
	window['sabotagesfixed_display'].update(value=f"Sabotages fixed: {statsConfig['SabotagesFixed']}")
	window['sabotagesfixed'].update(value=statsConfig['SabotagesFixed'])
	window['imposterkills_display'].update(value=f"Imposter kills: {statsConfig['ImposterKills']}")
	window['imposterkills'].update(value=statsConfig['ImposterKills'])
	window['timesmurdered_display'].update(value=f"Times murdered: {statsConfig['TimesMurdered']}")
	window['timesmurdered'].update(value=statsConfig['TimesMurdered'])
	window['timesejected_display'].update(value=f"Times ejected: {statsConfig['TimesEjected']}")
	window['timesejected'].update(value=statsConfig['TimesEjected'])
	window['crewmatestreak_display'].update(value=f"Crewmate streak: {statsConfig['CrewmateStreak']}")
	window['crewmatestreak'].update(value=statsConfig['CrewmateStreak'])
	window['timesimposter_display'].update(value=f"Times imposter: {statsConfig['TimesImposter']}")
	window['timesimposter'].update(value=statsConfig['TimesImposter'])
	window['timescrewmate_display'].update(value=f"Times crewmate: {statsConfig['TimesCrewmate']}")
	window['timescrewmate'].update(value=statsConfig['TimesCrewmate'])
	window['gamesstarted_display'].update(value=f"Games started: {statsConfig['GamesStarted']}")
	window['gamesstarted'].update(value=statsConfig['GamesStarted'])
	window['gamesfinished_display'].update(value=f"Games finished: {statsConfig['GamesFinished']}")
	window['gamesfinished'].update(value=statsConfig['GamesFinished'])
	window['impostervotewins_display'].update(value=f"Imposter vote wins: {statsConfig['ImposterVoteWins']}")
	window['impostervotewins'].update(value=statsConfig['ImposterVoteWins'])
	window['imposterkillwins_display'].update(value=f"Imposter kill wins: {statsConfig['ImposterKillWins']}")
	window['imposterkillwins'].update(value=statsConfig['ImposterKillWins'])
	window['impostersabotagewins_display'].update(value=f"Imposter sabotage wins: {statsConfig['ImposterSabotageWins']}")
	window['impostersabotagewins'].update(value=statsConfig['ImposterSabotageWins'])
	window['crewmatevotewins_display'].update(value=f"Crewmate vote wins: {statsConfig['CrewmateVoteWins']}")
	window['crewmatevotewins'].update(value=statsConfig['CrewmateVoteWins'])
	window['crewmatetaskwins_display'].update(value=f"Crewmate task wins: {statsConfig['CrewmateTaskWins']}")
	window['crewmatetaskwins'].update(value=statsConfig['CrewmateTaskWins'])
	window.finalize()

if sys.platform == "win32":
	files = find_files(fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us") # epic games compatible
	prefsConfig = AUConfig(files.playerPrefs)
	hostConfig = GameHostOptions(files.gameHostOptions)
	statsConfig = PlayerStats(files.playerStats2)
	update_window(window,prefsConfig,hostConfig,statsConfig)

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
		statsConfig = PlayerStats(files)
		update_window(window,prefsConfig,hostConfig,statsConfig)
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
		statsConfig['BodiesReported'] = int(values['bodiesreported'])
		statsConfig['EmergenciesCalled'] = int(values['emergenciescalled'])
		statsConfig['TasksCompleted'] = int(values['taskscompleted'])
		statsConfig['AllTasksCompleted'] = int(values['alltaskscompleted'])
		statsConfig['SabotagesFixed'] = int(values['sabotagesfixed'])
		statsConfig['ImposterKills'] = int(values['imposterkills'])
		statsConfig['TimesMurdered'] = int(values['timesmurdered'])
		statsConfig['TimesEjected'] = int(values['timesejected'])
		statsConfig['CrewmateStreak'] = int(values['crewmatestreak'])
		statsConfig['TimesImposter'] = int(values['timesimposter'])
		statsConfig['TimesCrewmate'] = int(values['timescrewmate'])
		statsConfig['GamesStarted'] = int(values['gamesstarted'])
		statsConfig['GamesFinished'] = int(values['gamesfinished'])
		statsConfig['ImposterVoteWins'] = int(values['impostervotewins'])
		statsConfig['ImposterKillWins'] = int(values['imposterkillwins'])
		statsConfig['ImposterSabotageWins'] = int(values['impostersabotagewins'])
		statsConfig['CrewmateVoteWins'] = int(values['crewmatevotewins'])
		statsConfig['CrewmateTaskWins'] = int(values['crewmatetaskwins'])
		statsConfig.save()
		update_window(window,prefsConfig,hostConfig,statsConfig)
		sg.popup("Config saved!")
	elif event == 'About':
		help_popup = sg.Window('About AUE',[
			[sg.T("Among Us Editor")],
			[sg.T(f"v{__version__}")],
			[sg.Text("By Vresod (Vresod#3907) on Discord")],
			[sg.Button("Close")]
		]).read(close=True)

window.close()