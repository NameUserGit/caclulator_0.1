import ravno_result
#import delete_last_ection as dle


class Collection_data():

    def __init__(self):

        ##########ERROR_INPUT###########
        self.list_for_error_input = []##
        ################################

        self.list_all_simvols = []
        
        self.list_nubmer_and_brackets_open = [[]]
        self.list_level_miltiplication_division = [[]]
        self.list_level_plus_minus = [[]]
        self.list_level_all_operators =  [[]]
        
        self.brackets_open = []
        self.brackets_close = []

        self.simvols = []
        
    def ask_level(self):
        return len(self.brackets_open)-len(self.brackets_close)

    def bracket_open(self):
        if self.error_input('('):
            self.list_all_simvols.append('(')
            #############ERROR_INPUT##############
            self.list_for_error_input.append('(')#
            ######################################
            if self.ask_level() == 0:
                self.list_nubmer_and_brackets_open[0].append('(')
            else:
                self.list_nubmer_and_brackets_open[self.ask_level()][len(self.list_nubmer_and_brackets_open[self.ask_level()])-1].append('(')
                
            self.brackets_open.append('(')    
            if len(self.list_nubmer_and_brackets_open) -1 < len(self.brackets_open) - len(self.brackets_close):
                self.list_nubmer_and_brackets_open.append([])
                self.list_level_miltiplication_division.append([])
                self.list_level_plus_minus.append([])
                self.list_level_all_operators.append([])
            
            self.list_nubmer_and_brackets_open[self.ask_level()].append([])             
            self.list_level_all_operators[self.ask_level()].append([])
            
    def bracket_close(self):
        if self.error_input(')'):
            self.int_num()
            self.brackets_close.append(')')
            self.list_all_simvols.append(')')
            self.list_for_error_input.append(')')

    def int_num(self):
        if self.simvols:
            snum = ''
            for s in self.simvols:
                snum += s
            if '.' in snum:
                self.list_for_error_input.append(float(snum))
                if self.ask_level():
                    self.list_nubmer_and_brackets_open[self.ask_level()][len(self.list_nubmer_and_brackets_open[self.ask_level()])-1].append(float(snum))
                else:
                    self.list_nubmer_and_brackets_open[self.ask_level()].append(float(snum))
            else:
                self.list_for_error_input.append(int(snum))
                if self.ask_level():
                    self.list_nubmer_and_brackets_open[self.ask_level()][len(self.list_nubmer_and_brackets_open[self.ask_level()])-1].append(int(snum))
                else:
                    self.list_nubmer_and_brackets_open[self.ask_level()].append(int(snum))
            self.simvols = []
            
######################################################################
#############################POLE NUMBERS#############################
    def one(self):
        if self.error_input('1'):
            self.simvols.append('1')
            self.list_all_simvols.append('1')

    def two(self):
        if self.error_input('2'):
            self.simvols.append('2')
            self.list_all_simvols.append('2')

    def three(self):
        if self.error_input('3'):
            self.simvols.append('3')
            self.list_all_simvols.append('3')

    def four(self):
        if self.error_input('4'):
            self.simvols.append('4')
            self.list_all_simvols.append('4')

    def five(self):
        if self.error_input('5'):
            self.simvols.append('5')
            self.list_all_simvols.append('5')

    def six(self):
        if self.error_input('6'):
            self.simvols.append('6')
            self.list_all_simvols.append('6')

    def seven(self):
        if self.error_input('7'):
            self.simvols.append('7')
            self.list_all_simvols.append('7')

    def eight(self):
        if self.error_input('8'):    
            self.simvols.append('8')
            self.list_all_simvols.append('8')

    def nine(self):
        if self.error_input('9'):
            self.simvols.append('9')
            self.list_all_simvols.append('9')

    def zero(self):
        if self.error_input('0'):
            self.simvols.append('0')
            self.list_all_simvols.append('0')
######################################################################
############################POLE OPERATORS############################
    def plus(self):
        if self.error_input('+'):
            self.list_all_simvols.append('+')
            self.list_level_plus_minus[self.ask_level()].append('+')
            if self.ask_level():
                self.list_level_all_operators[self.ask_level()][len(self.list_level_all_operators[self.ask_level()])-1].append('+')
            else:
                self.list_level_all_operators[self.ask_level()].append('+')
            self.int_num()
            self.list_for_error_input.append('+')

    def minus(self):
        if self.error_input('-'):
            self.list_all_simvols.append('-')
            self.list_level_plus_minus[self.ask_level()].append('-')
            if self.ask_level():
                self.list_level_all_operators[self.ask_level()][len(self.list_level_all_operators[self.ask_level()])-1].append('-')
            else:
                self.list_level_all_operators[self.ask_level()].append('-')
            self.int_num()
            self.list_for_error_input.append('-')

    def miltiplication(self):
        if self.error_input('*'):
            self.list_all_simvols.append('*')
            self.list_level_miltiplication_division[self.ask_level()].append('*')
            if self.ask_level():
                self.list_level_all_operators[self.ask_level()][len(self.list_level_all_operators[self.ask_level()])-1].append('*')
            else:
                self.list_level_all_operators[self.ask_level()].append('*')
            self.int_num()
            self.list_for_error_input.append('*')
        
    def division(self):
        if self.error_input('/'):
            self.list_all_simvols.append('/')
            self.list_level_miltiplication_division[self.ask_level()].append('/')
            if self.ask_level():
                self.list_level_all_operators[self.ask_level()][len(self.list_level_all_operators[self.ask_level()])-1].append('/')
            else:
                self.list_level_all_operators[self.ask_level()].append('/')
            self.int_num()
            self.list_for_error_input.append('/')

    def capcha(self):
        if self.error_input('.'):
            self.simvols.append('.')
            self.list_all_simvols.append('.')
######################################################################        
        

    def ravno(self):
        if self.error_input('='):
            self.int_num()
            result = ravno_result.formula(self.list_nubmer_and_brackets_open , self.list_level_miltiplication_division, self.list_level_plus_minus, self.list_level_all_operators)
            result_str = str(result)
            print('ravno ' , result)

            self.list_all_simvols.append(' = ')
            self.list_all_simvols.append(result_str)

            self.clear_ravno()

            
            
######################################################################
##########################CLEAR#######################################
    def clear(self):

        ##########ERROR_INPUT###########
        self.list_for_error_input = []##
        ################################
        
        self.list_all_simvols = []
        
        self.list_nubmer_and_brackets_open = [[]]
        self.list_level_miltiplication_division = [[]]
        self.list_level_plus_minus = [[]]
        self.list_level_all_operators =  [[]]
        
        self.brackets_open = []
        self.brackets_close = []

        self.simvols = []

    def clear_ravno(self):
        
        ##########ERROR_INPUT###########
        self.list_for_error_input = []##
        ################################
 
        self.list_nubmer_and_brackets_open = [[]]
        self.list_level_miltiplication_division = [[]]
        self.list_level_plus_minus = [[]]
        self.list_level_all_operators =  [[]]
        
        self.brackets_open = []
        self.brackets_close = []

        self.simvols = []

    def clear_list_all_simvols(self):
        if self.list_all_simvols:
                if self.list_all_simvols[len(self.list_all_simvols) - 2] == ' = ':
                    self.list_all_simvols = []
        


########################END CLEAR#####################################
######################################################################
####################DELETE_LAST_ECTION################################
    def delete_last_ection(self):
        self.list_all_simvols , self.list_nubmer_and_brackets_open = dle.oredelation_action(self.list_all_simvols,self.list_nubmer_and_brackets_open)
        print(self.list_nubmer_and_brackets_open)
        ##########ERROR_INPUT###########
        #self.list_for_error_input = []##
        ################################

        #self.list_all_simvols = []
        
        #self.list_nubmer_and_brackets_open = [[]]
        #self.list_level_miltiplication_division = [[]]
        #self.list_level_plus_minus = [[]]
        #self.list_level_all_operators =  [[]]
        
        #self.brackets_open = []
        #self.brackets_close = []

        #self.simvols = []
        
#################END_DELETE_LAST_ECTION###############################
######################################################################


    def print_simvols(self):
        simvols = ''
        for i in self.list_all_simvols:
            simvols += i
        print('simvols' , self.list_all_simvols)
        return simvols

    
    def error_input(self, element):

        resolution = False
            
        print('self.list_for_error_input' , self.list_for_error_input)
        
        if element in '0 1 2 3 4 5 6 7 8 9':

            self.clear_list_all_simvols()
                
            if not len(self.list_for_error_input):
                resolution = True
            elif self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /':
                resolution = True
            elif self.list_for_error_input[len(self.list_for_error_input)-1] == '(':
                resolution = True
             
    
        elif element == '(':
            
            self.clear_list_all_simvols()
            
            if not len(self.list_for_error_input) and not self.simvols:
                resolution = True
            if self.list_for_error_input:
                if self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /' and not self.simvols:
                    resolution = True
                
                elif self.list_for_error_input[len(self.list_for_error_input)-1] == '(':
                    resolution = True

        elif element == ')':
            
            self.clear_list_all_simvols()
            
            if len(self.list_for_error_input):
                if len(self.brackets_open) - len(self.brackets_close) != 0 and self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /' and self.simvols:
                    if self.simvols[0] == '.' and len(self.simvols) > 1:
                        resolution = True
                    elif self.simvols[0] != '.':
                        resolution = True
                        
                elif self.list_for_error_input[len(self.list_for_error_input)-1] == ')' and len(self.brackets_open) - len(self.brackets_close) != 0:
                    resolution = True
                
        elif element in  '+ - * /':
            
            self.clear_list_all_simvols()
            
            if not len(self.list_for_error_input) and self.simvols:
                if self.simvols[0] == '.' and len(self.simvols) > 1:
                    resolution = True
                elif self.simvols[0] != '.':
                    resolution = True
            
            elif len(self.list_for_error_input):
                if self.list_for_error_input[len(self.list_for_error_input)-1] == ')':
                    resolution = True
                elif self.simvols:
                    resolution = True
        elif element == '.':
            
            self.clear_list_all_simvols()
            
            if '.' not in self.simvols:
                resolution = True

        elif element == '=':
            
            self.clear_list_all_simvols()
            
            if self.list_for_error_input:
                if self.list_for_error_input[len(self.list_for_error_input)-1] == ')'  and len(self.brackets_open) - len(self.brackets_close) == 0:
                    resolution = True
                elif self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /' and self.simvols:
                    if self.simvols[0] == '.' and len(self.simvols) > 1:
                        resolution = True
                    elif self.simvols[0] != '.':
                        resolution = True
                    
        return resolution 

if __name__ == '__main__':
    print('You open modul back')
    input('Clicks Enter the end')
        
        
            
        
    


    

            
            
            

        
        
