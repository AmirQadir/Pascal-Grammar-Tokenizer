import Processor


def main():
    with open("pascalCode.pas", "r", encoding='utf-8') as fileReader:
        for line_number, line in enumerate(fileReader):
            lp = Processor.LineProcessor(line_number + 1, line)
            lp.process()
    print("token_list.csv File Generated")
    print("symboltable.csv File Genearated")


if __name__ == "__main__":
    main()
