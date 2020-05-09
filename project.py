def main():
    keywords = {"program", "real", "integer", "if", "then", "else", "while", "repeat", "readln", "write", "writeln",
                "or", "div", "mod",
                "and", "true", "false", "not", "trunc", "do", "until","end", "begin"}
    sym = {";", ".", ":", ":=", "+", "-", "*", "/", "(", ")", "<", ">", "<=", ">=", "<>", "="}

    with open("etc.txt", "r", encoding='utf-8') as fileReader:
        for line in fileReader:
            line = line.strip()
            if line:







if __name__ == "__main__":
    main()
