# Pascal-Grammar-Tokenizer

Pascal Grammar Tokenizer is a simple python program that reads a pascal file and generate two files. 
1. token_list.csv
2. symboltable.csv

## Usage
```
1. python3 project.py (Run project.py)

Note: ensure all python files and .pas file are in the same directory
```

### Code Explanation
```python
def main():
    with open("pascalCode.pas", "r", encoding='utf-8') as fileReader:
        for line_number, line in enumerate(fileReader):
            lp = Processor.LineProcessor(line_number + 1, line)
            lp.process()
    print("token_list.csv File Generated")
    print("symboltable.csv File Genearated")
```

1. project.py reads the pascal file
    1. for each line it creates an object of LineProcessor
    2. and then calls its process method.
2. LineProcessor process method does the following
```
    def process(self):
        idx = 0
        position = 0
        while idx < len(self.line):
            position += 1
            if self.line[idx] == '"':
                processor = StringProcessor(self.line[idx + 1:], self.line_number, idx + 1)

            elif self.line[idx].isdigit():
                processor = NumberProcessor(self.line[idx:], self.line_number, idx + 1)

            elif self.line[idx] in sym:
                processor = SymbolProcessor(self.line[idx:], self.line_number, idx + 1)

            elif self.line[idx].isspace():
                idx += 1
                continue

            else:
                processor = WordProcessor(self.line[idx:], self.line_number, idx + 1)

            x = processor.process()

            if x:
                idx += x
            else:
                idx += 1
```
