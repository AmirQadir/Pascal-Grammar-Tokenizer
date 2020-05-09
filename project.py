keywords = {"program", "var", "real", "integer", "if", "then", "else", "while", "repeat", "readln", "write", "writeln",
                "or", "div", "mod",
                "and", "true", "false", "not", "trunc", "do", "until","end", "begin"}
sym  = {";", ".", ":", ":=", "+", "-", "*", "/", "(", ")", "<", ">", "<=", ">=", "<>", "="}
dsym = { ":", "<", ">" }

import Processor

def status(buildup):
    if buildup.strip():
        if buildup in keywords:
            print("KEYWORD:", buildup)
        elif buildup in sym:
            print("SYM:", buildup)
        else:
            print("ID:", buildup)
            # ids.append(buildup)

def main():
    with open("etc.txt", "r", encoding='utf-8') as fileReader:
        for line_number, line in enumerate(fileReader):
            lp = Processor.LineProcessor(line_number, line)
            lp.process()


if __name__ == "__main__":
    main()
