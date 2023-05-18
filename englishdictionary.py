import bs4
import requests
import PySimpleGUI as gui

layout =[[gui.Text("以下に英単語を入力(空白で区切る)",font=("Gothic",15))],
		 [gui.Input("")],
		 [gui.Button("決定"),gui.Button("終了")]]
window = gui.Window("ケンブリッジ辞書自動検索", layout)
while True:
	event, values = window.read()
	pplayout = []

	print(event)
	if event == "決定":

		url = "https://dictionary.cambridge.org/ja/dictionary/english/"
		headers_dic = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}

		word = values[0] ##input("Enter an English word>>>")
		words = word.split() ##空欄で単語を区切る
		kekka = ""
		for word in words:
			wurl = url + word
			print(word)
			site = requests.get(wurl,headers=headers_dic,timeout=(7.0,7.5))

			soup = bs4.BeautifulSoup(site.content, "html.parser")
			tests = soup.find("div",class_="def ddef_d db")

			if tests is None :
				print("こんな単語ない")
				pplayout.append([gui.Text(word,font =("Gothic",15))])
				pplayout.append([gui.Text("こんな単語ない")])
				continue
			print(tests.text)
			print("")
			pplayout.append([gui.Text(word,font =("Gothic",15))])
			pplayout.append([gui.Text("意味："),gui.Text(tests.text)])
			kekka = kekka + word +"\n"+ tests.text + "\n"
			print(pplayout)
	else :
		break
	print("miteruyo")
	ppup = gui.Window("ケンブリッジ辞書より",pplayout)
	batu = ppup.read()
window.close()
		

	
