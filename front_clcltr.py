import three_back_clcltr
from tkinter import *


class Application(Frame):
    
    def __init__(self):
        self.tk = Tk()
        self.tk.title('GUI clcltr L')
        self.tk.geometry('223x182')
        super(Application, self).__init__(self.tk)
        self.bc = three_back_clcltr.Collection_data()
        self.grid()
        self.element_grafic_interface()
        
    def element_grafic_interface(self):

        ########TEXT APPLICATION######
        self.text_application = Text(self, width=27, height=3, wrap = WORD)
        self.text_application.grid(column=0, columnspan=55)
        
        #########POLE NUMBER##########
        Button(self,
               text=' 1 ',
               command = lambda:[self.bc.one(), self.mapper_text()]
               ).grid(row=1,
                      column=0)
        Button(self,
               text=' 2 ',
               command = lambda:[self.bc.two(), self.mapper_text()]
               ).grid(row=1,
                      column=1)
        Button(self,
               text=' 3 ',
               command = lambda:[self.bc.three(), self.mapper_text()]
               ).grid(row=1,
                      column=2)
        
        Button(self,
               text=' 4 ',
               command = lambda:[self.bc.four(), self.mapper_text()]
               ).grid(row=2,
                      column=0)
        Button(self,
               text=' 5 ',
               command = lambda:[self.bc.five(), self.mapper_text()]
               ).grid(row=2,
                      column=1)
        Button(self,
               text=' 6 ',
               command = lambda:[self.bc.six(), self.mapper_text()]
               ).grid(row=2,
                      column=2)

        Button(self,
               text=' 7 ',
               command = lambda:[self.bc.seven(), self.mapper_text()]
               ).grid(row=3,
                      column=0)
        Button(self,
               text=' 8 ',
               command = lambda:[self.bc.eight(), self.mapper_text()]
               ).grid(row=3,
                      column=1)
        Button(self,
               text=' 9 ',
               command = lambda:[self.bc.nine(), self.mapper_text()]
               ).grid(row=3,
                      column=2)
        Button(self,
               text=' 0 ',
               command = lambda:[self.bc.zero(), self.mapper_text()],
               ).grid(row=4,
                      column=1)
        
        #########POLE BRACKETS##########
        Button(self,
               text=' ( ',
               command = lambda:[self.bc.bracket_open(), self.mapper_text()],
               ).grid(row=4,
                      column=0)
        Button(self,
               text=' ) ',
               command = lambda:[self.bc.bracket_close(), self.mapper_text()],
               ).grid(row=4,
                      column=2)
        
        #########POLE OPERATORS##########
        Button(self,
               text=' + ',
               command = lambda:[self.bc.plus(), self.mapper_text()],
               width=2
               ).grid(row=1,
                      column=3)
        Button(self,
               text=' - ',
               command = lambda:[self.bc.minus(), self.mapper_text()],
               width=2
               ).grid(row=1,
                      column=4)
        Button(self,
               text=' / ',
               command = lambda:[self.bc.division(), self.mapper_text()],
               width=2
               ).grid(row=2,
                      column=3)
        
        Button(self,
               text=' * ',
               command = lambda:[self.bc.miltiplication(), self.mapper_text()],
               width=2
               ).grid(row=2,
                      column=4)
        Button(self,
               text=' = ',
               command = lambda:[self.bc.ravno(), self.mapper_text()],
               width=2
               ).grid(row=3,
                      column=3)
        ######### . ##########
        Button(self,
               text=' . ',
               width=2,
               command = lambda:[self.bc.capcha(), self.mapper_text()],
               ).grid(row=3,
                      column=4)
        ######### <- ##########
        Button(self,
               text=' <- ',
               command = lambda:[self.bc.delete_last_ection(), self.mapper_text()],
               width=2
               ).grid(row=4,
                      column=3)
         ######### C ##########
        Button(self,
               text=' C ',
               command = lambda:[self.bc.clear(), self.mapper_text()],
               width=2
               ).grid(row=4,
                      column=4)

    def mapper_text(self):
        self.text_application.delete(0.0 , END)
        self.text_application.insert(0.0 , self.bc.print_simvols())
        
        
        

app = Application()
    
