class Action(object):

    def __init__(self, numbers , level_operators, level_miltiplication_division, all_level_operators, list_bracket_open_and_numbers):

        #get lists
        self.numbers = numbers
        self.level_operators = level_operators
        self.level_miltiplication_division = level_miltiplication_division
        self.all_level_operators = all_level_operators
        self.list_bracket_open_and_numbers = list_bracket_open_and_numbers
        ##########

        self.first_operator = None
        self.num1 = None
        self.num2 = None
        self.list_results = []
        self.list_level_results = [[]]
        
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
    
    #first_operator_action
    def first_operator_action(self):
        operator = None
        while operator == None:
            if self.level_miltiplication_division[len(self.level_miltiplication_division)-1]:
                operator = self.level_miltiplication_division[len(self.level_miltiplication_division)-1].pop(0)
            elif self.level_operators[len(self.level_operators)-1]:
                operator = self.level_operators[len(self.level_operators)-1].pop(0)
            else:
                self.level_miltiplication_division.pop(len(self.level_miltiplication_division)-1)
                self.level_operators.pop(len(self.level_operators)-1)
            
        index_operator = self.all_level_operators[len(self.all_level_operators)-1].index(operator)
        self.all_level_operators[len(self.all_level_operators)-1].pop(index_operator)
        if not self.all_level_operators[len(self.all_level_operators)-1]:
            self.all_level_operators.pop(len(self.all_level_operators)-1)

        result = self.functyon(operator, self.numbers[len(self.numbers)-1].pop(index_operator), self.numbers[len(self.numbers)-1].pop(index_operator))
        self.list_results.append(result)
        if not self.numbers[len(self.numbers)-1] and len(self.numbers) != 1:
            self.numbers.pop(len(self.numbers)-1)
            self.numbers[len(self.numbers)-1].insert(len(self.numbers[len(self.numbers)-1])-1, result)
        else:
            self.numbers[len(self.numbers)-1].insert(len(self.numbers[len(self.numbers)-1])-1, result)
        
        print('result' , self.list_results)    
        print(operator)
        print(self.level_miltiplication_division)
        print(self.level_operators)
        print(self.all_level_operators)
        print('Number', self.numbers)

    # variant_two_first_action
    def two_first_action(self):
        operator = None
        while operator == None:
            if self.level_miltiplication_division[len(self.level_miltiplication_division)-1]:
                operator = self.level_miltiplication_division[len(self.level_miltiplication_division)-1].pop(0)
            elif self.level_operators[len(self.level_operators)-1]:
                operator = self.level_operators[len(self.level_operators)-1].pop(0)
            else:
                self.level_miltiplication_division.pop(len(self.level_miltiplication_division)-1)
                self.level_operators.pop(len(self.level_operators)-1)
            
        index_operator = self.all_level_operators[len(self.all_level_operators)-1].index(operator)
        self.all_level_operators[len(self.all_level_operators)-1].pop(index_operator)
        if not self.all_level_operators[len(self.all_level_operators)-1]:
            self.all_level_operators.pop(len(self.all_level_operators)-1)

        result = self.functyon(operator, self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].pop(index_operator), self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].pop(index_operator))
        
        if not self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1] and len(self.list_bracket_open_and_numbers) != 1:
            self.list_bracket_open_and_numbers.pop(len(self.list_bracket_open_and_numbers)-1)
            index_bracket_open = self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].index('(')
            self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].pop(index_bracket_open)
            self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].insert(index_bracket_open, result)
        else:
            if '(' in self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1]:
                index_bracket_open = self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].index('(')
                self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].pop(index_bracket_open)
                self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].insert(index_bracket_open, result)
            else:
                self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-1].insert(index_operator, result)

        print('All operators: ' , self.all_level_operators)
        print('Operators minus plus: ', self.level_operators)
        print('Miltiplication_division: ', self.level_miltiplication_division)
        print('list_bracket_open_and_numbers: ', self.list_bracket_open_and_numbers)
    

class Collection_data(object):

    def __init__(self):

        self.numbers = []
        self.level_numbers = [[]]
        self.level_nembers_operators = [[]]
        self.brackets_open = []
        self.brackets_close = []
        self.all_level_operators = [[]]
        self.level_operators = [[]]
        self.level_miltiplication_division = [[]]
        self.list_bracket_open_and_numbers = [[]]

        self.simvols = []

        self.all_simvols = []

        self.action = None

    def add_operator(self, element):
        self.level_operators[self.ask_level()].append(element)
        self.all_level_operators[self.ask_level()].append(element)
        self.all_simvols.append(element)
        self.level_nembers_operators[self.ask_level()].append(element)
        
    def ask_level(self):
        return len(self.brackets_open)-len(self.brackets_close)

    def int_num(self):
        if self.simvols:
            snum = ''
            for s in self.simvols:
                snum += s

            if '.' in snum:
                self.level_numbers[self.ask_level()].append(float(snum))
                self.level_nembers_operators[self.ask_level()].append(float(snum))
                self.list_bracket_open_and_numbers[self.ask_level()].append(float(snum))
            else:
                self.level_numbers[self.ask_level()].append(int(snum))
                self.level_nembers_operators[self.ask_level()].append(int(snum))
                self.list_bracket_open_and_numbers[self.ask_level()].append(int(snum))
            self.simvols = []
        
    ################BRACKETS ( )##################    
    def bracket_open(self):
        self.brackets_open.append('(')
        self.all_simvols.append('(')
        if len(self.level_operators) - 1 < len(self.brackets_open) - len(self.brackets_close):
            self.level_numbers.append([])
            self.level_operators.append([])
            self.level_miltiplication_division.append([])
            self.all_level_operators.append([])
            self.level_nembers_operators.append([])
            self.list_bracket_open_and_numbers.append([])
        self.list_bracket_open_and_numbers[len(self.list_bracket_open_and_numbers)-2].append('(')

    def bracket_close(self):
        if self.simvols:
            self.int_num()
        self.all_simvols.append(')')
        self.brackets_close.append(')')
    ###############################################
    ################POLE NUMBER####################
    def one(self):
        self.simvols.append('1')
        self.all_simvols.append('1')

    def two(self):
        self.simvols.append('2')
        self.all_simvols.append('2')
        
    def three(self):
        self.simvols.append('3')
        self.all_simvols.append('3')

    def four(self):
        self.simvols.append('4')
        self.all_simvols.append('4')

    def five(self):
        self.simvols.append('5')
        self.all_simvols.append('5')

    def six(self):
        self.simvols.append('6')
        self.all_simvols.append('6')

    def seven(self):
        self.simvols.append('7')
        self.all_simvols.append('7')

    def eight(self):
        self.simvols.append('8')
        self.all_simvols.append('8')

    def nine(self):
        self.simvols.append('9')
        self.all_simvols.append('9')

    def zero(self):
        self.simvols.append('0')
        self.all_simvols.append('0')
    ###############################################
    def capcha(self):
        self.simvols.append('.')
        self.all_simvols.append('.')
        
    ################POLE OPERATOR##################
    def plus(self):
        if self.simvols:
            self.int_num()
        self.add_operator('+')
        

    def minus(self):
        if self.simvols:
            self.int_num()
        self.add_operator('-')
        
        

    def multiplication(self):
        if self.simvols:
            self.int_num()
        self.level_miltiplication_division[self.ask_level()].append('*')
        self.all_level_operators[self.ask_level()].append('*')
        self.level_nembers_operators[self.ask_level()].append('*')
        self.all_simvols.append('*')
        

    def division(self):
        if self.simvols:
            self.int_num()
        self.level_miltiplication_division[self.ask_level()].append('/')
        self.all_level_operators[self.ask_level()].append('/')
        self.level_nembers_operators[self.ask_level()].append('/')
        self.all_simvols.append('/')
           
    ###############################################
    def ravno(self):
        self.int_num()
        if self.action == None:
            print(':D')
            self.action = Action(self.level_numbers, self.level_operators, self.level_miltiplication_division,self.all_level_operators, self.list_bracket_open_and_numbers)
            
        self.action.two_first_action()

    def print_simvols(self):
        simvols = ''
        for s in self.all_simvols:
            simvols += s
        print('level_nun' , self.level_numbers)
        print('brackets_o' , self.brackets_open)
        print('brackets_c' , self.brackets_close)
        print('level operators' , self.level_operators)
        print('all operators' , self.all_level_operators)
        print('level m d', self.level_miltiplication_division)
        print('all num and operators', self.level_nembers_operators)
        print('number and open_brackets!', self.list_bracket_open_and_numbers)
        print('#####################################################')
        return simvols
        
        
        

    
        
