from os import PathLike
from typing import OrderedDict
from data_indexes import prefs_indexes

class AUConfig():
	def __init__(self,config_file:PathLike = None,autoinit = True):
		self.config_file = config_file
		self.raw_config = open(config_file).read()
		self.config = OrderedDict()
		if autoinit:
			self.open()
	def __getitem__(self,attr):
		return self.config[attr]
	def __setitem__(self,attr,value):
		self.config[attr] = value
	def __iter__(self): # guaranteed to be in correct order because OrderedDict
		for i in self.config:
			yield i
	def open(self):
		"""
		Manually open the config set in self.config_file
		"""
		temp_config = self.raw_config.split(",")
		for i,index in enumerate(prefs_indexes):
			self.config[index] = temp_config[i]
	def save(self,config_file:str = None):
		"""
		Save the config to the file it was opened from
		"""
		config = ""
		for i,value in enumerate(self.config):
			config += str(self.config[value])
			if i < len(self.config):
				config += ","
		if config_file is None:
			config_file = self.config_file
		with open(config_file,"w") as config_filefile: # horrible variable name, don't worry about it
			config_filefile.write(config)

if __name__ == "__main__":
	c = AUConfig(r"C:\Users\lukeb\AppData\LocalLow\Innersloth\Among Us\playerPrefs")
	c.save()
