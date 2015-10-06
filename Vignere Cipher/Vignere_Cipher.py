from copy import deepcopy
from pprint import pprint

class Vignere_Cipher():
    def __init__(self):
            self.alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
            self.cipher = "TSMVM MPPCW CZUGX HPECP RFAUE IOBQW PPIMS FXIPC TSQPK SZNUL OPACR DDPKT SLVFW ELTKR GHIZS FNIDF ARMUE NOSKR GDIPH WSGVL EDMCM SMWKP IYOJS TLVFA HPBJI RAQIW HLDGA IYOUX"
            #self.cipher = "ADQYS MIUSB OXKKT MIBHK IZOOO EQOOG IFBAG KAUMF VVTAA CIDTW
            #MOCIO EQOOG BMBFV ZGGWP CIEKQ HSNEW VECNE DLAAV RWKXS VNSVP HCEUT QOIOF
            #MEGJS WTPCH AJMOC HIUIX"
            #self.cipher = "ABCDEFABC"
            #self.cipher = "THERE ARETW OWAYS OFCON STRUC TINGA SOFTW AREDE SIGNO NEWAY
            #ISTOM AKEIT SOSIM PLETH ATTHE REARE OBVIO USLYN ODEFI CIENC IESAN DTHEO
            #THERW AYIST OMAKE ITSOC OMPLI CATED THATT HEREA RENOO BVIOU SDEFI CIENC
            #IESTH EFIRS TMETH ODISF ARMOR EDIFF ICULT"
            self.period = None

    def index_of_coincidence(self, c):
            cd = {}
            cipher = c.split()
            cipher_length = 0
            chars = (list(c))
            #print chars
            for i in chars:
                    if(i != " "):
                            cipher_length += 1
            #print(cipher_length, chars)

            if cipher_length == 0:
                return 0
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
            #print "Index of coincidence: ", result
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
                            string1 = ''.join(chars[j:i + j])

                            if(not chars_dict.has_key(string1)):
                                    chars_dict[string1] = []

                            # go through all chars
                            for k in range(len(chars) - 1):
                                    string2 = ''.join(chars[k:i + k])

                                    if(string1 == string2):
                                            if(not chars_dict[string1].count(k) > 0):
                                                    chars_dict[string1].append(k)

            return chars_dict

    def print_similarities(self, dict):
        result = []
        # untabify worked
        for keys, values in dict.iteritems():
            if(len(values) > 1 and len(values) == 2):
                    result.append((keys, values, [values[1] - values[0]]))
            elif(len(values) > 1 and len(values) == 3):
                    result.append((keys, values, [values[1] - values[0], values[2] - values[1]]))
        return result

    def seg_alphabets(self, no_of_alphabets, ciphertext):
        count = 0
        t_count = 0
        string = ""
        string_list = []
        # convert ciphertext into strings
        ciphertext = list("".join(ciphertext.split()))
        
        # create a list of 11 charactere strings
        while(t_count < len(ciphertext)):
            if(count == 11):
                string_list.append(string)
                count = 0
                string = ""
            else:
                string += ciphertext[t_count]
                t_count += 1
                count += 1
        string_list.append(string)
        return string_list

    def find_ic_unknown_alphabets(self, length, cipher_list):
        coincidences = []
        dict_alphabets = {}
        # column
        for i in range(length):
            string = ""
            # row
            for items in cipher_list:
                if(i < len(items)):
                    string += items[i]
            coincidences.append(string)
        
        for x in range(len(coincidences)):
            dict_alphabets[x] = round(self.index_of_coincidence(coincidences[x]), 5)

        pprint(dict_alphabets)

# Main
if __name__ == '__main__':
    V = Vignere_Cipher()
    V.index_of_coincidence(V.cipher)
    dict = V.find_matches()
    sim = V.print_similarities(dict)
    pprint(sim)
    seg = V.seg_alphabets(11, V.cipher)
    #pprint(seg)
    V.find_ic_unknown_alphabets(11, seg)
