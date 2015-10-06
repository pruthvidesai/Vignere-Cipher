import pprint
from copy import deepcopy

class Vignere_Cipher():
	def __init__(self):
		self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
		self.cipher = "TSMVM MPPCW CZUGX HPECP RFAUE IOBQW PPIMS FXIPC TSQPK SZNUL OPACR DDPKT SLVFW ELTKR GHIZS FNIDF ARMUE NOSKR GDIPH WSGVL EDMCM SMWKP IYOJS TLVFA HPBJI RAQIW HLDGA IYOUX"
		#self.cipher = "ADQYS MIUSB OXKKT MIBHK IZOOO EQOOG IFBAG KAUMF VVTAA CIDTW MOCIO EQOOG BMBFV ZGGWP CIEKQ HSNEW VECNE DLAAV RWKXS VNSVP HCEUT QOIOF MEGJS WTPCH AJMOC HIUIX"
		#self.cipher = "ABCDEFABC"
		#self.cipher = "THERE ARETW OWAYS OFCON STRUC TINGA SOFTW AREDE SIGNO NEWAY ISTOM AKEIT SOSIM PLETH ATTHE REARE OBVIO USLYN ODEFI CIENC IESAN DTHEO THERW AYIST OMAKE ITSOC OMPLI CATED THATT HEREA RENOO BVIOU SDEFI CIENC IESTH EFIRS TMETH ODISF ARMOR EDIFF ICULT"
		self.period = None

	def index_of_coincidence(self, c):
		cd = {}
		cipher = c.split()
		cipher_length = 0
		chars = (list(c))
		for i in chars:
			if(i != " "):
				cipher_length += 1
		print(cipher_length)
		result = float(1) / (cipher_length * (cipher_length - 1))
		sum = 0

		# from a to z
		for i in range(0, 26):
			cd[self.alphabets[i]] = 0
			for j in cipher:
				for k in j:
					if(self.alphabets[i] == k.lower()):
						cd[self.alphabets[i]] += 1
			if(cd[self.alphabets[i]] > 0):
				sum += (cd[self.alphabets[i]] * (cd[self.alphabets[i]] - 1))
		result *= sum
		return result

	def find_matches(self):
		# from 2 to 15 find if there are any matches
		chars = list(self.cipher)
		chars_dict = {}
		temp = []
		count = 0

		# remove spaces
		for x in chars:
			if(x != ' '):
				temp.append(x)
		chars = deepcopy(temp)

		# string lengths
		for i in range(2, 15):
			for j in range(len(chars)):
				string1 = ''.join(chars[j:i+j])

				if(not chars_dict.has_key(string1)):
					chars_dict[string1] = []

				# go through all chars
				for k in range(len(chars) - 1):
					string2 = ''.join(chars[k:i+k])

					if(string1 == string2):
						if(not chars_dict[string1].count(k) > 0):
							chars_dict[string1].append(k)

		return chars_dict

	def print_similarities(self, dict):
		for keys, values in dict.iteritems():
			if(len(values) > 1):
				print(keys, values)

# Main
V = Vignere_Cipher()
V.index_of_coincidence(V.cipher)
d = V.find_matches()
V.print_similarities(d)