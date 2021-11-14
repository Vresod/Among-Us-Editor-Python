import PySimpleGUI as sg
from extra import AUConfig
from os import environ
from data_indexes import hats, skins, visors, color_indexes

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
	[sg.Text('Pet:',key="pet_display")],
	[sg.HorizontalSeparator()],
	[sg.Input(key='file',visible=False,enable_events=True),sg.FileBrowse(button_text="Open",initial_folder=fr"{environ['AppData']}\..\LocalLow\Innersloth\Among Us"),sg.Submit('Save',key="save")]
]


# Create the Window
window = sg.Window('Among Us Editor (v0.1 prerelease) - Remake - By Vresod',layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
	event, values = window.read()
	if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
		break
	print(f"{event=}\n{values=}")
	if event == "file":
		config = AUConfig(values['file'])
		window['username_display'].update(value=f"Username: {config['lastPlayerName']}") 
		window['hat_display'].update(value=f"Hat: {config['lastHat']}") 
		window['skin_display'].update(value=f"Skin: {config['lastSkin']}") 
		window['pet_display'].update(value=f"Pet: {config['lastPet']}")
		window.finalize()
	elif event == "save":
		config['lastPlayerName'] == window['username']
		config.save()
	elif event == 'About':
		help_popup = sg.Window('About AUE',[
			[sg.T("Among Us Editor")],
			[sg.T("v0.1 prerelease")],
			[sg.T("By Vresod (Vresod#3907) on Discord")],
			[sg.Button("Close")]
		]).read(close=True)

window.close()