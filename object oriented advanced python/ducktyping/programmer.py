class Pycharm:
    def compile(self):
        print("compile using pycharm ")
    def execute(self):
        print("execute using pycharm")
class Vscode:
    def compile(self):
        print("compile using Vscode ")
    def execute(self):
        print("execute using Vscode")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
p=Programmer()
pyc=Pycharm()
p.coding(pyc)

