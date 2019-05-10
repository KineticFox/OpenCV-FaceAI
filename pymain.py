import tkinter
import random


class Window(tkinter.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.pack()
		self.createWidgets()

	def createWidgets(self):
		self.nameEntry = tkinter.Entry(self)
		self.nameEntry.pack()
		self.textB = tkinter.StringVar()
		self.textB.set(" ")
		self.nameEntry["textvariable"] = self.textB
		self.calc = tkinter.Button(self)
		self.calc["text"] = "Calc"
		self.calc["command"] = self.rand
		self.calc.pack(side="left")

	def rand(self):
		self.textB.set(random.randint(1,21)) #just for testing tkinter

root = tkinter.Tk()
app = Window(root)
app.mainloop()