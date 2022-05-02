import random
# озвращает список цифр которым соответствует буква юникода.
#для генерации ключа заданного размера - введите 1 аргумент любую строку, а второй длинну
def keyGen  (Message, typer=0):
	lenMessage = 0
	if typer == 0:
		lenMessage = len(Message)
	elif typer >= 1:
		lenMessage = typer
	for i in range(lenMessage):
	listRandInteger = [random.randint(1, 1500) for i in range(lenMessage)]
	listRandInteger.insert(0, 0)
	print("KEY: {0}".format(listRandInteger))
	return listRandInteger
# возвращает список дексов юникода, принимает строку сообщение
def msg2ver(Message):
	for i in Message:
		listMessage = list(Message)
	listNumMessage = [int(ord(i)) for i in listMessage]
	return listNumMessage
# возвращает строку сообщение, принимает список дексов юникода
def ver2msg(listNumMessage):
	listMessage = [chr(int(i)) for i in listNumMessage]
	Message = "".join(listMessage)
	return Message
# принимает строку - возвращает ее списком чисел
def str2list(text):
	strListText = text.split(".")
	listNumText = [int(i) for i in strListText if i.isdecimal()]
	return listNumText
# принимает список чисел - возвращает его строкой
def list2str(listText):
	strList = [str(i) for i in listText]
	strText = ".".join(strList)
	return strText

x = keyGen("", 5)
