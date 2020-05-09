class AbstractProcessor:

    def process(self):
        pass


class StringProcessor(AbstractProcessor):

    def process(self):
        pass


class WordProcessor(AbstractProcessor):

    def process(self):
        pass


class NumberProcessor(AbstractProcessor):

    def process(self):
        pass


class SymbolProcessor(AbstractProcessor):

    def process(self):
        pass


class LineProcessor(AbstractProcessor):

    def process(self, line):
        idx = 0
        while idx < len(line):
            if line[idx] == '"':
                processor = StringProcessor(line[idx + 1:])

            elif line[idx].isdigit():
                processor = NumberProcessor(line[idx:])

            elif line[idx] in sym:
                processor = SymbolProcessor(line[idx:])

            else:
                processor = WordProcessor(line[idx:])

            idx = processor.process()
