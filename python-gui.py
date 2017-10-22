import easygui as g
import sys
while 1:
	g.msgbox('嗨，欢迎进入第一个界面小游戏')
	msg = '请问你想在我这里学到什么知识呢？'
	title = '小游戏互动'
	choices =['相声','编程','ooxx','琴棋书画']
	choice = g.choicebox(msg,title,choices)
	#note that we convert choice to string, in case
	#the user cancelled the choice, and we got None
	g.msgbox('你的选择是:'+str(choice),'结果')
	msg = '你希望重新开始小游戏吗？'
	title = '请选择'
	if g.ccbox(msg,title):#show a Continue/Cancel dialog
		pass #user chose Continue
	else:
		sys.exit(0)#user chose Cancel
