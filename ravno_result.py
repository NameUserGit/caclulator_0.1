class Action():

    def __init__(self):

        #get list 
        self.list_nubmer_and_brackets_open = None
        self.list_level_miltiplication_division = None
        self.list_level_plus_minus = None
        self.list_level_all_operators = None
        #########

    def add_lists(self, list_nubmer_and_brackets_open, list_level_miltiplication_division, list_level_plus_minus, list_level_all_operators):
        #get list 
        self.list_nubmer_and_brackets_open = list_nubmer_and_brackets_open
        self.list_level_miltiplication_division = list_level_miltiplication_division
        self.list_level_plus_minus = list_level_plus_minus
        self.list_level_all_operators = list_level_all_operators
        #########
        
    def print_lists(self):
        print('#####################################')
        print(self.list_nubmer_and_brackets_open)
        print(self.list_level_miltiplication_division)
        print(self.list_level_plus_minus)
        print(self.list_level_all_operators)
        print('#####################################')
        
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

    def first_operatort(self):
        operator = None
        while operator == None:
            if self.list_level_miltiplication_division[len(self.list_level_miltiplication_division)-1]:
                operator = self.list_level_miltiplication_division[len(self.list_level_miltiplication_division)-1].pop(0)
            elif self.list_level_plus_minus[len(self.list_level_plus_minus)-1]:
                operator = self.list_level_plus_minus[len(self.list_level_plus_minus)-1].pop(0)
            elif len(self.list_level_miltiplication_division) != 1 and len(self.list_level_plus_minus) != 1:
                self.list_level_miltiplication_division.pop(len(self.list_level_miltiplication_division)-1)
                self.list_level_plus_minus.pop(len(self.list_level_plus_minus)-1)
                
        return operator
    
    def index_operator(self, operator):
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

        return index_operator, index_list

    def num1_num2_result(self, operator, index_operator, index_list):
        num1 = None
        num2 = None
        result = None
        
        if len(self.list_nubmer_and_brackets_open) == 1:
            num1 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_operator)
            num2 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_operator)
            result = self.functyon(operator, num1, num2)
            
        else:
            num1 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list].pop(index_operator)
            num2 = self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list].pop(index_operator)
            result = self.functyon(operator, num1, num2)

        print('num1: ' , num1)
        print('num2: ' , num2)
        
        return result 

    def position_result(self, index_operator, result , index_list):

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
            self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2].pop(index_main_open_bracket)
            self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2].insert(index_main_open_bracket, result)
                
        elif self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list]:
            self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list].insert(index_operator, result)
        elif not self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1][index_list]:
            self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1].pop(index_list)

            index_main_open_bracket = 0
            number_open_bracket = 0
            
            while number_open_bracket != index_list + 1:
                if self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_list][index_main_open_bracket] == '(':
                    number_open_bracket += 1
                    if number_open_bracket == index_list + 1:
                        break
                index_main_open_bracket += 1
            self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_list].pop(index_main_open_bracket)
            self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-2][index_list].insert(index_main_open_bracket, result)

        if not self.list_nubmer_and_brackets_open[len(self.list_nubmer_and_brackets_open)-1]:
            self.list_nubmer_and_brackets_open.pop(len(self.list_nubmer_and_brackets_open)-1)


    def action(self):

        while len(self.list_nubmer_and_brackets_open[0]) != 1:

            self.print_lists()
            
            operator = None
            index_operator = None
            index_list = None
            result = None
            
            
            operator = self.first_operatort()
            index_operator, index_list = self.index_operator(operator)
            result = self.num1_num2_result(operator, index_operator, index_list)
            self.position_result(index_operator, result , index_list)
            
            print('operator: ' , operator)
            
            print('result: ' , result)
            
        return_result = self.list_nubmer_and_brackets_open[0][0]
        
        self.print_lists()
        
        return  return_result
               
            

def formula(list_nubmer_and_brackets_open, list_level_miltiplication_division, list_level_plus_minus, list_level_all_operators):
    actions = Action()
    actions.add_lists(list_nubmer_and_brackets_open, list_level_miltiplication_division, list_level_plus_minus, list_level_all_operators)
    result = actions.action()

    return result
    

if __name__ == '__main__':
    print('You open modul ravno_result')
    input('Clicks Enter the end')
        

        
    
