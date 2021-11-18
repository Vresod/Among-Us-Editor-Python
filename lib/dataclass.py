from dataclasses import dataclass
from glob import glob

@dataclass
class host_index:
	name: str
	type: str
	length: int

@dataclass
class find_files:
	__slots__ = ['playerPrefs','gameHostOptions','playerStats2']
	def __init__(self,config_folder:str) -> None:
		self.playerPrefs = glob(f"{config_folder}/*playerPrefs")[0]
		self.gameHostOptions = glob(f"{config_folder}/*gameHostOptions")[0]
		self.playerStats2 = glob(f"{config_folder}/*playerStats2")[0]

if __name__ == "__main__":
	from os import environ
	d = find_files(f"{environ['AppData']}\..\LocalLow\Innersloth\Among Us")
	print(d.playerPrefs)
	print(d.playerStats2)
	print(d.gameHostOptions)