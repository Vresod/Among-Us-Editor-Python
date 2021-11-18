from collections import OrderedDict
from os import PathLike
from .data_indexes import prefs_indexes as _prefs_indexes
from .data_indexes import host_indexes as _host_indexes
import struct

from decimal import Decimal, getcontext

getcontext().prec = 3

class AUConfig():
	"""
	Used to store playerPrefs. Overwrite `open()` and `save()` methods and it'll work for everything else
	"""
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
		for i,index in enumerate(_prefs_indexes):
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

class GameHostOptions(AUConfig):
	def __init__(self,config_file:PathLike = None,autoinit = True):
		self.config_file = config_file
		self.raw_config = open(config_file,"rb")
		self.config = OrderedDict()
		if autoinit:
			self.open()
	
	def open(self):
		for i,index in enumerate(_host_indexes):
			if index.type == "byte": # one byte
				self.config[_host_indexes[i].name] = struct.unpack('B',self.raw_config.read(1))[0]
			elif index.type == "uint32": # unsigned int
				self.config[_host_indexes[i].name] = struct.unpack('I',self.raw_config.read(4))[0]
			elif index.type == "int32": # signed int
				self.config[_host_indexes[i].name] = struct.unpack('i',self.raw_config.read(4))[0]
			elif index.type == "boolean": # bool
				self.config[_host_indexes[i].name] = struct.unpack('?',self.raw_config.read(1))[0]
			elif index.type == "single": # float
				self.config[_host_indexes[i].name] = Decimal(struct.unpack('f',self.raw_config.read(4))[0]).normalize()
		self.raw_config.close()
	def save(self,config_file:str = None):
		config = b""
		for i,index in enumerate(_host_indexes):
			if index.type == "byte": # one byte
				config += struct.pack('B',self.config[index.name])
			elif index.type == "uint32": # unsigned int
				config += struct.pack('I',self.config[index.name])
			elif index.type == "int32": # signed int
				config += struct.pack('i',self.config[index.name])
			elif index.type == "boolean": # bool
				config += struct.pack('?',self.config[index.name])
			elif index.type == "single": # float
				config += struct.pack('f',self.config[index.name])
		if config_file is None:
			config_file = self.config_file
		with open(config_file,"wb") as config_filefile: # don't worry please
			config_filefile.write(config)