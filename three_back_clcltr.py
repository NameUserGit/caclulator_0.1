class Action():

    def __init__(self, list_nubmer_and_brackets_open, list_level_miltiplication_division, list_level_plus_minus, list_level_all_operators):

        #get list 
        self.list_nubmer_and_brackets_open = list_nubmer_and_brackets_open
        self.list_level_miltiplication_division = list_level_miltiplication_division
        self.list_level_plus_minus = list_level_plus_minus
        self.list_level_all_operators = list_level_all_operators
        #########

    def functyon(self, operator, num1, num2):
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            result = num1 / num2

        return result

    def first_action(self):

        if len(self.list_nubmer_and_brackets_open) == 1 and len(self.list_nubmer_and_brackets_open[0]) == 1:
            print('stop!')
        else:
            operator = None
            
            while operator == None:
                if self.list_level_miltiplication_division[len(self.list_level_miltiplication_division)-1]:
                    operator = self.list_level_miltiplication_division[len(self.list_level_miltiplication_division)-1].pop(0)
                elif self.list_level_plus_minus[len(self.list_level_plus_minus)-1]:
                    operator = self.list_level_plus_minus[len(self.list_level_plus_minus)-1].pop(0)
                elif len(self.list_level_miltiplication_division) != 1 and len(self.list_level_plus_minus) != 1:
                    self.list_level_miltiplication_division.pop(len(self.list_level_miltiplication_division)-1)
                    self.list_level_plus_minus.pop(len(self.list_level_plus_minus)-1)
                    
                    

            index_operator = None
            index_list = 0
                
            if len(self.list_level_all_operators) == 1:
                index_operator = self.list_level_all_operators[len(self.list_level_all_operators)-1].index(operator)
                self.list_level_all_operators[len(self.list_level_all_operators)-1].pop(index_operator)
                                
            else:
                while index_operator == None:
                
                    if operator in self.list_level_all_operators[len(self.list_level_all_operators)-1][index_list]:
                        index_operator = self.list_level_all_operators[len(self.list_level_all_operators)-1][index_list].index(operator)
                        break
                    
                    index_list += 1
                    
                self.list_level_all_operators[len(self.list_level_all_operators)-1][index_list].pop(index_operator)
                if not self.list_level_all_operators[len(self.list_level_all_operators)-1][index_list]:
                    self.list_level_all_operators[len(self.list_level_all_operators)-1].pop(index_list)
                    
                if not self.list_level_all_operators[len(self.list_level_all_operators)-1]:
                    self.list_level_all_operators.pop(len(self.list_level_all_operators)-1)
                
                    
            print('index_list', index_list)            
            print('index_operator',index_operator)
            
            num1 = None
            num2 = None

            if len(self.list_nubmer_and_brackets_open) == 1:
                num1 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_operator)
                num2 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_operator)

            else:
                num1 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list].pop(index_operator)
                num2 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list].pop(index_operator)

            print('operator' , operator)
            print('num1' , num1)
            print('num2' , num2)
            result = self.functyon(operator, num1, num2)
            print('result' , result)


            if len(self.list_nubmer_and_brackets_open) == 1:
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].insert(index_operator, result)
                
            elif len(self.list_nubmer_and_brackets_open) == 2 and not self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list]:
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_list)
                index_main_open_bracket = 0
                number_open_bracket = 0
                while number_open_bracket != index_list + 1:
                    if self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_main_open_bracket] == '(':
                        number_open_bracket += 1
                    if number_open_bracket == index_list + 1:
                        break
                    index_main_open_bracket += 1
                print(index_main_open_bracket)
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2].pop(index_main_open_bracket)
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2].insert(index_main_open_bracket, result)
                
            elif self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list]:
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list].insert(index_operator, result)
            elif not self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list]:
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_list)
                
                index_main_open_bracket = 0
                number_open_bracket = 0
                
                while number_open_bracket != index_list + 1:
                    print('~~~~~~~~~~~~~~~~~~~')
                    if self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_list][index_main_open_bracket] == '(':
                        number_open_bracket += 1
                        if number_open_bracket == index_list + 1:
                            break
                    index_main_open_bracket += 1
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_list].pop(index_main_open_bracket)
                self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_list].insert(index_main_open_bracket, result)

            if not self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1]:
                self.list_nubmer_and_brackets_open.pop(len(self.list_nubmer_and_brackets_open)-1)            
        
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

        self.action = None
        
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
        self.int_num()
        print('\n')
        print('num bracket' , self.list_nubmer_and_brackets_open)
        print('m d ' , self.list_level_miltiplication_division)
        print('p m ' , self.list_level_plus_minus)
        print('all o', self.list_level_all_operators)

        if not self.action:
            self.action = Action(self.list_nubmer_and_brackets_open, self.list_level_miltiplication_division, self.list_level_plus_minus, self.list_level_all_operators)

        self.action.first_action()
                
    def print_simvols(self):
        simvols = ''
        for i in self.list_all_simvols:
            simvols += i
        print('simvols' , self.list_all_simvols)
        return simvols

    def error_input(self, element):

        resolution = False
        
        if element in '0 1 2 3 4 5 6 7 8 9':
            if not len(self.list_for_error_input):
                resolution = True
            elif self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /':
                resolution = True
            elif self.list_for_error_input[len(self.list_for_error_input)-1] == '(':
                resolution = True

        elif element == '(':
            if not len(self.list_for_error_input):
                resolution = True

            elif self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /':
                resolution = True
            
            elif self.list_for_error_input[len(self.list_for_error_input)-1] == '(':
                resolution = True

        elif element == ')':
            if len(self.list_for_error_input):
                if len(self.brackets_open) - len(self.brackets_close) != 0 and self.list_for_error_input[len(self.list_for_error_input)-1] in '+ - * /' and self.simvols:
                    resolution = True
                elif self.list_for_error_input[len(self.list_for_error_input)-1] == ')' and len(self.brackets_open) - len(self.brackets_close) != 0:
                    resolution = True
                
        elif element in  '+ - * /':
            if not len(self.list_for_error_input) and self.simvols:
                    resolution = True
            
            elif len(self.list_for_error_input):
                if self.list_for_error_input[len(self.list_for_error_input)-1] == ')':
                    resolution = True
                elif self.simvols:
                    resolution = True
        elif element == '.':
            if '.' not in self.simvols:
                resolution = True
                
        return resolution 

if __name__ == '__main__':
    print('You open modul back')
    input('Clicks Enter the end')
        
        
            
        
    


    

            
            
            

        
        
