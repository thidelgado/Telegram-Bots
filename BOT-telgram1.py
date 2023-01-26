import telebot

#i = 0
bot = telebot.TeleBot("5464936434:AAG0WK1WtTJxfGtOykX9_2zS92lWre5eEno")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Salve guerreiro!")

@bot.message_handler(func=lambda message: True)
def echo_all(message, i=0):
	if(message.text == "Hi"):
		list = []
		list.append(message.date)
		print(list)
		i += 1
		print(i)
		dtstr = str(message.date)
		f = open("demofile2.txt", "a")
		f.write(dtstr)
		f.close()
  		#date = ("d"+str[i])
		#print(date)
  		#d = "date"+ i
		d = message.date
		print(d)
		#bot.reply_to(message, message.text)
		a=1
		f = open("demofile2.txt", "r")
		print("TEST: ", f.read(10))
		myStr = f.read(-10)
		ln = len(myStr)
		print(ln)
		print("--------------------")
		print("myString", myStr)
		print("--------------------")
		ivmyString = myStr[::-1]
		print("INVERTED:", ivmyString)
		print("xxxxxxxxxxxxxxxxxxxx")
		print("1- lastChar_INV: ", ivmyString[0])
		print("2- lastChar_INV: ", ivmyString[1])
		print("3- lastChar_INV: ", ivmyString[2])
		print("4- lastChar_INV: ", ivmyString[3])
		print("5- lastChar_INV: ", ivmyString[4])
		print("6- lastChar_INV: ", ivmyString[5])
		print("7- lastChar_INV: ", ivmyString[6])
		print("8- lastChar_INV: ", ivmyString[7])
		print("9- lastChar_INV: ", ivmyString[8])
		print("10- lastChar_INV: ", ivmyString[9])
		print("--------------------")
		lastVar = ivmyString[9]+ivmyString[8]+ivmyString[7]+ivmyString[6]+ivmyString[5]+ivmyString[4]+ivmyString[3]+ivmyString[2]+ivmyString[1]+ivmyString[0]
		print(lastVar)
		print(type(lastVar))
		numLV = int(lastVar)
		print("Last DATE NUM: ",numLV)
		print(type(numLV))
		print("xxxxxxxxxxxxxxxxxxxx")
		print("11- lastChar_INV: ", ivmyString[10])
		print("12- lastChar_INV: ", ivmyString[11])
		print("13- lastChar_INV: ", ivmyString[12])
		print("14- lastChar_INV: ", ivmyString[13])
		print("15- lastChar_INV: ", ivmyString[14])
		print("16- lastChar_INV: ", ivmyString[15])
		print("17- lastChar_INV: ", ivmyString[16])
		print("18- lastChar_INV: ", ivmyString[17])
		print("19- lastChar_INV: ", ivmyString[18])
		print("20- lastChar_INV: ", ivmyString[19])
		print("---------------------")
		penuVar = ivmyString[19]+ivmyString[18]+ivmyString[17]+ivmyString[16]+ivmyString[15]+ivmyString[14]+ivmyString[13]+ivmyString[12]+ivmyString[11]+ivmyString[10]
		print(penuVar)
		print(type(penuVar))
		numLVP = int(penuVar)
		print("Penultimo DATE NUM: ",numLVP)
		print(type(numLVP))
		print("----------------------------------")
		print("==== CALCULATION AND CONDITION ===")
		print("----------------------------------")
		tm = 1 #TIME TO WAIT IN MINUTES
		maxdif = tm * 60
		print("Seconds: ", maxdif)
		resultAmB = numLV - numLVP
		print("Result: ",resultAmB)
  		
  		#res = ivmyString.Substring(0, 10);
		#print(type(ivmyString))
		#print(f.read())
		
		#f = open("invert1.txt", "a")
		#f.write(f.read(10))
		#f.close()  		
		#txt1 = f.read()
		#print("------")
		#print(txt1())
		if(message.text == "Hi" and resultAmB>maxdif):
			print("Dont Send")
		elif(message.text == "Hi" and resultAmB<maxdif):
			msgTXT = "ALERTA Mensagem enviada novamente em " + str(resultAmB) + " segundos"
			bot.send_message(2052052310 , msgTXT)
			print(message.date)
		
bot.infinity_polling()
echo_all()
