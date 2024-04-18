from Tkinter import *
import tkMessageBox
import Tkinter, Tkconstants, tkFileDialog
import re, string
import unicodedata
import Tkinter, Tkconstants, tkFileDialog
import f

def abrir():
	filename = tkFileDialog.askopenfilename(initialdir = "",title = "Select file",filetypes = (("all files","*.*"), ("all files","*.*") ))
	archivo = open (filename, 'r')
	contenido = archivo.read()
	T.insert(END, contenido)
	#tkMessageBox.showinfo( "Este es el nombre del archivo", contenido)
def remove_punctuation( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

def elimina_tildes(cadena):
    s = ''.join((c for c in unicodedata.normalize('NFD',unicode(cadena)) if unicodedata.category(c) != 'Mn'))
    return s.decode()



def crypt():
	plainText=T.get('1.0', 'end')
	try:	
		al = int(alfa.get())
		if f.hasInverse(al, 26) and plainText.strip():
			tkMessageBox.showinfo("Message", 'Alpha en betha are right values')
			plainText=elimina_tildes(plainText)
			plainText=plainText.upper()
			plainText=remove_punctuation(plainText)
        		plainText=f.remove_space(plainText)
        		print plainText
			cryptText=encryptText(plainText)
			cipherT.insert(END, cryptText)
		else:
			tkMessageBox.showinfo('Error :c', 'There isnt plain text or alpha and Betha are wrong values ')
		
	except ValueError:
		tkMessageBox.showinfo('Error :c', 'No ibsertaste numeros validos or There isnt plain text')
	

def encryptText(plaintext):
	

	alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
	'O','P','Q','R','S','T','U','V','W','X','Y','Z']
	list2=[]
	for i in plaintext:
		
		if i=='\n':
			list2.append('\n')

		else:
			actualPosition=alfabeto.index(i)
			
			al=int(alfa.get())
			be=int(beta.get())
			aux=(al*actualPosition)+be
			newPosition=aux%26
			list2.append(alfabeto[newPosition])
		
	salida=''.join(list2)
		
	
		
	return salida

def decrypt():
	
	crypT=cipherT.get('1.0', 'end')
	if crypT.strip():
		
		clearPlainText()
		plainText=decryptText(crypT)
		T.insert(END, plainText)			
	else:
		tkMessageBox.showinfo( "Alert !", "There isn't cypher text")
	
def decryptText(encryptedText):
	inverse=int(f.inverse( int(alfa.get()),26 )) 
	be=int(beta.get())


	alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
	'O','P','Q','R','S','T','U','V','W','X','Y','Z']
	list2=[]
	for i in encryptedText:
		if i=='\n':
			list2.append('\n')
		else:
    			position=alfabeto.index(i)
    			aux=inverse*(position-be)
    			newPosition=aux%26      
	        	list2.append(alfabeto[newPosition])

	#list2.pop()
	salida=''.join(list2)
	return salida
	



def clearText():
	T.delete('1.0', END)
	cipherT.delete('1.0', END)
def clearPlainText():
	T.delete('1.0', END)




		



		


def exit():
	root.quit()
def mensaje():
	tkMessageBox.showinfo( "Mensaje", selectedNumber.get())
	#print(option.get())

def suma():
	#suma=int(entrada1.get()) + int(entrada2.get())
	try:	
		al = int(alfa.get())
		if f.hasInverse(al, 26):
			tkMessageBox.showinfo("Message", 'okis')
		else:
			tkMessageBox.showinfo("Message", 'not okis')
	except ValueError:
		tkMessageBox.showinfo('Error :c', 'No ibsertaste numeros validos')
	




root = Tk()
root.geometry("700x580")
root.title("Affine cipher")
root.configure(bg="#99ffcc")
T = Text(root, height=15, width=40)
cipherT = Text(root, height=15, width=40)



lbPt= Label(text="Plain text").place(x=10, y=12)
lbPt= Label(text="Cypher text").place(x=10, y=280)


alfa=StringVar()
beta=StringVar()

lbCx = Label (text="C(x)=").place(x=340, y=270)
tfAlfa=Entry(root, textvariable=alfa, width=5).place(x=385, y=270)
lbCx = Label (text=" x + ").place(x=435, y=270)
tfBeta=Entry(root, textvariable=beta, width=5).place(x=470, y=270)
lbCx = Label (text="mod 26").place(x=520, y=270)
 




btnExaminar =  Button (text="Add plain text", command=abrir).place(x=550, y=50)
btnC = Button(root, text="Crypt", command=crypt).place(x=550, y=100)
btnD = Button (root, text="Decrypt", command=decrypt).place(x=550, y=150) 
btnClear = Button (text="New Crypt", command=clearText).place(x=550, y=200)
btnClear = Button (text="Close",font=("Verdana",12), command=exit).place(x=600, y=480)

btnClearPlain = Button (text="Clear plain text", command=clearPlainText).place(x=550, y=300)


btnClearPlain = Button (text="prueba", command=suma).place(x=450, y=400)






T.place(x=10, y=30)
cipherT.place(x=10, y=300)



mainloop()
