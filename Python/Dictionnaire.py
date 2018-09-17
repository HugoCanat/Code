class Dixion:
	def __init__(self, **data):
		self._keys = []
		self._values = []

		for k, v in data.items():
			self._keys.append(k)
			self._values.append(v)

	def __getitem__(self, index):
		if index in self._keys:
			indice = self._keys.index(index)
			return self._values[indice]
		else:
			self.__getattr__()
	def __setitem__(self, index, value):
		if index in self._keys:
			indice = self._keys.index(index)
			self._values[indice] = value
		else:
			self._keys.append(index)
			self._values.append(value)
	def __getattr__(self):
		raise IndexError
	def __delitem__(self, index):
		
		if index in self._keys:
			indice = self._keys.index(index)
			del self._values[indice]
			del self._keys[indice]
		else:
			self.__getattr__()

	def __contains__(self, k):
		if k in self._keys:
			return True
		else:
			return False
	def __len__(self):
		return len(self._keys)

	def __repr__(self):
		chaine = '{'
		ft = True
		for k, v in self.items():
			if ft:
				ft = False
			else:
				chaine += ', '

			if type(k) == int:
				k = str(k)
			else:
				k = "'" + k + "'"
			chaine += "" + k + ": " + str(v)
		chaine += '}'
		return chaine

	def __str__(self):
		return repr(self)

	def __iadd__(self, obj):
		if obj.__class__.__name__ != 'Dixion' and obj.__class__.__name__ != 'dict':
			raise TypeError("unsupported operand type(s): only 'dict' and 'Dixion' type(s) supported.")
		else:
			for k, v in obj.items():
				self[k] = v
		return self
	def __radd__(self, obj):
		print('bojnour')
		return self
	def __add__(self, obj):
		if obj.__class__.__name__ != 'Dixion' and obj.__class__.__name__ != 'dict':
			raise TypeError("unsupported operand type(s): only 'dict' and 'Dixion' type(s) supported.")
		else:
			for k, v in obj.items():
				self[k] = v
		return self

	def __iter__(self):
		return iter(self._keys)

	def keys(self):
		return self._keys
	def values(self):
		return self._values
	def items(self):
		#items = list()
		#i = 0
		#while i < len(self._keys):
		#	a = (self._keys[i], self._values[i])
		#	items.append(a)
		#	i += 1
		#return items
		for i, cle in enumerate(self._keys):
			valeur = self._values[i]
			yield (cle, valeur)

	def sort(self):
		SortedKeys = sorted(self._keys)
		values = self._values
		a = 0
		for i in SortedKeys:
			self._values[a] = values[self._keys.index(i)]
			a+= 1
		self._keys = SortedKeys

	def reverse(self):
		revKey = list()
		revVal = list()

		i=len(self._keys)-1
		while i >= 0:
			revKey.append(self._keys[i])
			revVal.append(self._values[i])
			i -= 1
		self._keys = revKey
		self._values = revVal