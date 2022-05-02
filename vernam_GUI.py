import tkinter as tk
from vernam_def import *
from tkinter import filedialog as fd
#-----------------------------------------------------------------------
def decrypting(listCrypt, key):
	msgNum = [a ^ b for a,b in zip(listCrypt, key)]
	msgString = numList2msg(msgNum)
	return msgString
#-----------------------------------------------------------------------
def keyGenBut():
	ent_key_size.insert(tk.END,"\r")
	try:
		file_name = fd.asksaveasfilename(
			filetypes=(("VSK files", "*.VSK"),
				("All files", "*.*"))
				)
		f = open(file_name, 'w')
		sizeKeyStr = ent_key_size.get()
		ent_key_size.delete(0, tk.END)
		sizeKey = "".join(c for c in sizeKeyStr if  c.isdecimal())
		sizeKey = int(sizeKey)
		strText = list2str(keyGen(0,sizeKey))
		f.write(strText)
		f.close()
	except TypeError:
		return 1
	except FileNotFoundError:
		return 2
	except ValueError:
		return 3
		
def inputMsg():
	try:
		file_name = fd.askopenfilename(
					filetypes=(("VSM files", "*.VSM"),
						("TXT files", "*.TXT"),
						("All files", "*.*"))
						)
		f = open(file_name)
		s = f.read()
		txt_msg.delete(1.0, tk.END)
		txt_msg.insert(1.0, s)
		f.close()
	except FileNotFoundError:
		return 1
	except TypeError :
		return 2
		
def outputMsg():
	try:
		file_name = fd.asksaveasfilename(
				filetypes=(("VSM files", "*.VSM"),
					("All files", "*.*"))
					)
		f = open(file_name, 'w')
		Msg = txt_msg.get("1.0", tk.END)
		f.write(Msg)
		f.close()
	except FileNotFoundError:
		return 1
	except TypeError :
		return 2
		
def inputVer():
	file_name = fd.askopenfilename(
				filetypes=(("VSV files", "*.VSV"),
					("All files", "*.*"))
					)
	f = open(file_name)
	s = f.read()
	ent_ver.delete(0, tk.END)
	ent_ver.insert(0, s)
	f.close()
	
def outputVer():
	file_name = fd.asksaveasfilename(
		filetypes=(("VSV files", "*.VSV"),
			("All files", "*.*"))
			)
	f = open(file_name, 'w')
	Msg = ent_ver.get()
	f.write(Msg)
	f.close()

def inputKey():
	file_name = fd.askopenfilename(
				filetypes=(("VSK files", "*.VSK"),
					("All files", "*.*"))
					)
	f = open(file_name)
	s = f.read()
	ent_key.delete(0, tk.END)
	ent_key.insert(0, s)
	f.close()

def outputKey():
	file_name = fd.asksaveasfilename(
		filetypes=(("VSK files", "*.VSK"),
			("All files", "*.*"))
			)
	f = open(file_name, 'w')
	Msg = ent_key.get()
	f.write(Msg)
	f.close()

def crypting():
	ent_ver.delete(0, tk.END)
	MsgNum = msg2ver(txt_msg.get(1.0, tk.END))
	keyNum = str2list(ent_key.get())
	if len(keyNum) == 0:
		keyNum = keyGen("", (len(MsgNum)-1))
		keyNum.pop(0)
	listCrypt = [a ^ b for a,b in zip(MsgNum, keyNum)]
	strCrypt = list2str(listCrypt)
	ent_ver.insert(0, strCrypt)
	
window = tk.Tk()
window.title("Vernam Encrypt")
window.geometry('400x600')
window.minsize(420,500)
window.maxsize(420,500)

lbl_msg = tk.Label(window, text="Message", font=(20)).grid(row=0, column=0,stick="w", padx=5,pady=5)
btn_in_msg = tk.Button(window, text="import", command=inputMsg).grid(row=0, column=1, padx=5,pady=5) 
btn_out_msg = tk.Button(window, text="output",command=outputMsg).grid(row=0, column=2, padx=5,pady=5)
txt_msg = tk.Text(window, width=50, height=7)
txt_msg.grid(row=1, column=0, columnspan=3, stick="we", padx=5)

lbl_spaser = tk.Label(window, text="	").grid(row=2, column=0, columnspan=3, stick="we", padx=5, pady=5)

lbl_ver = tk.Label(window, text="Chiphrogram", font=(20)).grid(row=3, column=0,stick="w", padx=5)
btn_in_ver = tk.Button(window, text="import", command=inputVer).grid(row=3, column=1) 
btn_out_ver = tk.Button(window, text="output",command=outputVer).grid(row=3, column=2)
ent_ver = tk.Entry(window)
ent_ver.grid(row=4, column=0, columnspan=3, stick="we", padx=5, pady=5)

lbl_spaser = tk.Label(window, text="	").grid(row=5, column=0, columnspan=3, stick="we", padx=5, pady=5)

lbl_key = tk.Label(window, text="Key", font=(20)).grid(row=6, column=0, stick="w", padx=5)
btn_in_key = tk.Button(window, text="import", command=inputKey).grid(row=6, column=1) 
btn_out_key = tk.Button(window, text="output", command=outputKey).grid(row=6, column=2)
ent_key = tk.Entry(window)
ent_key.grid(row=7, column=0, columnspan=3, stick="we", padx=5, pady=5)

btn_crypt = tk.Button(window, text="Crypt", relief=tk.RAISED, borderwidth=5,width=10, height=1, command=crypting).grid(row=8, column=1, padx=10, pady=5)
btn_decrypt = tk.Button(window, text="Decrypt", relief=tk.RAISED, borderwidth=5,width=10, height=1).grid(row=8, column=2, padx=10, pady=5)

lbl_spaser = tk.Label(window, text="	", font=(20)).grid(row=9, column=0, columnspan=3, stick="we")

lbl_key = tk.Label(window, text="Key size", font=(5)).grid(row=10, column=0, stick="we", padx=5)
ent_key_size = tk.Entry(window,width=15)
ent_key_size.grid(row=10, column=1, padx=5)
btn_keygen = tk.Button(window, text="Key Gen", command=keyGenBut).grid(row=10, column=2,padx=5)

#-----------------------------------------------------------------------
print(str2list("123.123.44.xer.r34.56"))
window.mainloop()
