keywords = {"program", "var", "real", "integer", "if", "then", "else", "while", "repeat", "readln", "write", "writeln",
                "or", "div", "mod",
                "and", "true", "false", "not", "trunc", "do", "until","end", "begin"}
sym = {";", ".", ":", ":=", "+", "-", "*", "/", "(", ")", "<", ">", "<=", ">=", "<>", "="}

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
        ids_by_line = []
        for line in fileReader:
            line = line.strip()
            if not line:
                continue
            
            buildup = ""

            # ids = []

            looking_for_more_sym = False

            # TODO: Specialized logic for stringConst
            for char in line:
                if char not in sym and char != " ":
                    if looking_for_more_sym:
                        looking_for_more_sym = False
                        status(buildup)
                        if (char in [">", "="]):
                            buildup += char
                        else:
                            status(buildup)
                            buildup = char
                    else:
                        buildup += char
                elif char in sym:
                    if looking_for_more_sym:
                        looking_for_more_sym = False
                        if (char in [">", "="]):
                            buildup += char
                        else:
                            status(buildup)
                            buildup = char

                        status(buildup)
                        buildup = ""
                    else:
                        status(buildup)
                        looking_for_more_sym = True
                        buildup = char
                else:
                    status(buildup)
                    buildup = ""
            
            status(buildup)
            buildup = ""

            # ids_by_line.append(id)


if __name__ == "__main__":
    main()
