import PySimpleGUI as sg
from extra import AUConfig
from os import environ
from data_indexes import hats, skins, visors, pets_indexes, color_indexes

__version__ = "1.0"

sg.theme('GrayGrayGray')   # Add a touch of color

menu_def = [["Help",["About"]]]

# All the stuff inside your window.
layout = [
	[sg.Menu(menu_def)],
	[sg.Text('Username:',key="username_display"),sg.Input(key="username")],
	[sg.Text('Color',key="color_display"),sg.Combo(values=color_indexes,key="color")],
	[sg.Text('Hat:',key="hat_display"),sg.Combo(values=hats,key="hat")],
	[sg.Text('Skin:',key="skin_display"),sg.Combo(values=skins,key="skin")],
	[sg.Text('Visor:',key="visor_display"),sg.Combo(values=visors,key="visor")],
	[sg.Text('Pet:',key="pet_display"),sg.Combo(values=pets_indexes,key="pet")],
	[sg.HorizontalSeparator()],
	[sg.Input(key='file',visible=False,enable_events=True),sg.FileBrowse(button_text="Open",initial_folder=fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us"),sg.Submit('Save',key="save")]
]


# Create the Window
window = sg.Window(f'Among Us Editor (v{__version__}) - Remake - By Vresod',layout)

def update_window(window:sg.Window,config:AUConfig):
	window['username_display'].update(value=f"Username: {config['lastPlayerName']}") 
	window['username'].update(value=config['lastPlayerName'])
	window['color_display'].update(value=f"Color: {color_indexes[int(config['colorConfig'])]}") 
	window['color'].update(value=color_indexes[int(config['colorConfig'])])
	window['hat_display'].update(value=f"Hat: {config['lastHat']}") 
	window['hat'].update(value=config['lastHat'])
	window['skin_display'].update(value=f"Skin: {config['lastSkin']}") 
	window['skin'].update(value=config['lastSkin'])
	window['visor_display'].update(value=f"Visor: {config['lastVisor']}") 
	window['visor'].update(value=config['lastVisor'])
	window['pet_display'].update(value=f"Pet: {config['lastPet']}")
	window['pet'].update(value=config['lastPet'])
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
		config['lastSkin'] = values['skin']
		config['lastVisor'] = values['visor']
		config['lastPet'] = values['pet']
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