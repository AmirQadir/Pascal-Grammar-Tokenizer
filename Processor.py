keywords = {"program", "var", "real", "integer", "if", "then", "else", "while", "repeat", "readln", "write", "writeln",
                "or", "div", "mod",
                "and", "true", "false", "not", "trunc", "do", "until","end", "begin"}
sym  = {";", ".", ":", ":=", "+", "-", "*", "/", "(", ")", "<", ">", "<=", ">=", "<>", "="}
dsym = { ":", "<", ">" }

class AbstractProcessor:

    def __init__(self, line):
        self.line = line

    
    def process(self):
        pass


class StringProcessor(AbstractProcessor):

    def __init__(self, line):
        self.line = line
    
    
    def process(self):
        idx = 0
        string = ""

        while self.line[idx] != '"':
            string += self.line[idx]
            idx += 1
        
        print("STRING:", string)

        return idx + 2


class WordProcessor(AbstractProcessor):

    def __init__(self, line):
        self.line = line
    
    
    def process(self):
        # Terminating Conditions: Symbol, Whitespace
        idx = 0
        word = ""
        
        while self.line[idx] not in sym and not self.line[idx].isspace():
            word += self.line[idx]
            idx += 1
        
        if word in keywords:
            print("KEYWORD:", word)
        else:
            print("ID:", word)
        
        return idx


class NumberProcessor(AbstractProcessor):

    def __init__(self, line):
        self.line = line
    
    
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
        
        print("NUMBER:", number)

        return idx


class SymbolProcessor(AbstractProcessor):

    def __init__(self, line):
        self.line = line
    
    
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
        
        return idx


class LineProcessor(AbstractProcessor):

    def __init__(self, line_number, line):
        self.line = line
        self.line_number = line_number

    
    def process(self):
        idx = 0
        while idx < len(self.line):
            if self.line[idx] == '"':
                processor = StringProcessor(self.line[idx + 1:])

            elif self.line[idx].isdigit():
                processor = NumberProcessor(self.line[idx:])

            elif self.line[idx] in sym:
                processor = SymbolProcessor(self.line[idx:])

            elif self.line[idx].isspace():
                idx += 1
                continue
            
            else:
                processor = WordProcessor(self.line[idx:])

            x = processor.process()

            if x:
                idx += x
            else:
                idx += 1
