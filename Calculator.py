from PythonCard import model

Formula = ''

class MainWindow(model.Background):
    def on_Button1_mouseClick(self, event):
        global Formula
        Formula = Formula + '1'
        self.components.Text.text = str(Formula)
    def on_Button2_mouseClick(self, event):
        global Formula
        Formula = Formula + '2'
        self.components.Text.text = str(Formula)
    def on_Button3_mouseClick(self, event):
        global Formula
        Formula = Formula + '3'
        self.components.Text.text = str(Formula)
    def on_Button4_mouseClick(self, event):
        global Formula
        Formula = Formula + '4'
        self.components.Text.text = str(Formula)
    def on_Button5_mouseClick(self, event):
        global Formula
        Formula = Formula + '5'
        self.components.Text.text = str(Formula)
    def on_Button6_mouseClick(self, event):
        global Formula
        Formula = Formula + '6'
        self.components.Text.text = str(Formula)
    def on_Button7_mouseClick(self, event):
        global Formula
        Formula = Formula + '7'
        self.components.Text.text = str(Formula)
    def on_Button8_mouseClick(self, event):
        global Formula
        Formula = Formula + '8'
        self.components.Text.text = str(Formula)
    def on_Button9_mouseClick(self, event):
        global Formula
        Formula = Formula + '9'
        self.components.Text.text = str(Formula)
    def on_Button0_mouseClick(self, event):
        global Formula
        Formula = Formula + '0'
        self.components.Text.text = str(Formula)
    def on_ButtonP_mouseClick(self, event):
        global Formula
        global Formula
        Formula = Formula + '+'
        self.components.Text.text = str(Formula)
    def on_ButtonM_mouseClick(self, event):
        global Formula
        Formula = Formula + '-'
        self.components.Text.text = str(Formula)
    def on_ButtonX_mouseClick(self, event):
        global Formula
        Formula = Formula + '*'
        self.components.Text.text = str(Formula)
    def on_ButtonE_mouseClick(self, event):
        global Formula
        Formula = Formula + '/'
        self.components.Text.text = str(Formula)
    def on_ButtonA_mouseClick(self, event):
        global Formula
        self.components.Text.text = str(eval(Formula))
        Formula = ''
app = model.Application(MainWindow)
app.MainLoop()
