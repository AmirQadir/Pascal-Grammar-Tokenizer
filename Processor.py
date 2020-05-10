import csv
keywords = {"program", "var", "if", "then", "else", "while", "repeat", "readln", "write", "writeln",
                "or", "div", "mod",
                "and", "true", "false", "not", "trunc", "do", "until","end", "begin"}
sym  = {";", ".", ":", ":=", "+", "-", "*", "/", "(", ")", "<", ">", "<=", ">=", "<>", "="}
dsym = { ":", "<", ">" }
type = {"integer", "real"}
stringConst = []
intConst = []

file = open("token_list.csv", "w", newline = '')
fileWriter = csv.writer(file)


class AbstractProcessor:

    def __init__(self,line, line_number, position):
        self.line = line
        self.line_number = line_number
        self.position = position

    
    def process(self):
        pass


class StringProcessor(AbstractProcessor):

    def __init__(self, line, line_number, position):
        self.line = line
        self.line_number = line_number
        self.position = position
    
    
    def process(self):
        idx = 0
        string = ""

        while self.line[idx] != '"':
            string += self.line[idx]
            idx += 1
        stringConst.append(string)
        fileWriter.writerow(["stringConst", string, self.line_number, self.position])

        print("STRING:", string)

        return idx + 2


class WordProcessor(AbstractProcessor):

    def __init__(self, line, line_number, position):
        self.line = line
        self.line_number = line_number
        self.position = position
    
    
    def process(self):
        # Terminating Conditions: Symbol, Whitespace
        idx = 0
        word = ""
        
        while self.line[idx] not in sym and not self.line[idx].isspace():
            word += self.line[idx]
            idx += 1
        
        if word in keywords:
            fileWriter.writerow(["keyword", word, self.line_number, self.position])

            print("KEYWORD:", word)
        elif word in type:
            fileWriter.writerow(["keyword", word, self.line_number, self.position])

            print("TYPE:", word)
        else:
            fileWriter.writerow(["id", word, self.line_number, self.position])
            print("ID:", word)
        
        return idx


class NumberProcessor(AbstractProcessor):

    def __init__(self, line, line_number, position):
        self.line = line
        self.line_number = line_number
        self.position = position
    
    
    def process(self):
        # Terminating Conditions: Symbol, Whitespace
        idx = 0
        number = ""

        while self.line[idx].isdigit():
            number += self.line[idx]
            idx += 1
        
        if self.line[idx] == ".":
            idx += 1
            number += "."
            while self.line[idx].isdigit():
                number += self.line[idx]
                idx += 1
        intConst.append(number)
        print("NUMBER:", number)
        fileWriter.writerow(["intConst", number, self.line_number, self.position])


        return idx


class SymbolProcessor(AbstractProcessor):

    def __init__(self, line, line_number, position):
        self.line = line
        self.line_number = line_number
        self.position = position
    
    
    def process(self):
        # Terminating Conditions: Whitespace, number, alphabet
        idx = 0
        symbol = ""

        if self.line[idx] in dsym:
            symbol += self.line[idx]
            idx += 1

            backup = symbol
            symbol += self.line[idx]

            if symbol in sym:
                idx += 1
            else:
                symbol = backup

        else:
            symbol += self.line[idx]
            idx += 1
        
        print("SYM:", symbol)
        fileWriter.writerow(["sym", symbol, self.line_number, self.position])
        return idx


class LineProcessor(AbstractProcessor):

    def __init__(self, line_number, line):
        self.line = line
        self.line_number = line_number

    
    def process(self):
        idx = 0
        position = 0
        while idx < len(self.line):
            position+=1
            if self.line[idx] == '"':
                processor = StringProcessor(self.line[idx + 1:], self.line_number, position)

            elif self.line[idx].isdigit():
                processor = NumberProcessor(self.line[idx:], self.line_number, position)

            elif self.line[idx] in sym:
                processor = SymbolProcessor(self.line[idx:], self.line_number, position)

            elif self.line[idx].isspace():
                idx += 1
                continue
            
            else:
                processor = WordProcessor(self.line[idx:], self.line_number, position)

            x = processor.process()

            if x:
                idx += x
            else:
                idx += 1
