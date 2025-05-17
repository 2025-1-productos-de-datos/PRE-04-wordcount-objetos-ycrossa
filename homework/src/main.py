# import argparse

# from ._internals.file_reader import FileReader
# from ._internals.text_processor import TextProcessor


# class ArgumentParser:
#     def __init__(self):
#         self.input = None
#         self.output = None

#     def run(self):

#         parser = argparse.ArgumentParser(description="Count words in files.")

#         parser.add_argument(
#             "input",
#             type=str,
#             help="Path to the input folder containing files to process",
#         )
#         parser.add_argument(
#             "output",
#             type=str,
#             help="Path to the output folder for results",
#         )

#         parsed_args = parser.parse_args()

#         self.input = parsed_args.input
#         self.output = parsed_args.output


# def main():

#     parser = ArgumentParser()
#     parser.run()
#     print(f"Input folder: {parser.input}")
#     print(f"Output folder: {parser.output}")

#     file_reader = FileReader(parser.input)
#     lines = file_reader.read_all_lines()
#     print(f"Read {len(lines)} lines from files in {parser.input}")

#     text_processor = TextProcessor()
#     processed_lines = text_processor.preprocess_lines(lines)
#     words = text_processor.split_into_words(processed_lines)
#     print(f"Extracted {len(words)} words from lines")


from homework.src._internals.CountWordsMixin import CountWordsMixin
from homework.src._internals.ParseArgsMixin import ParseArgsMixin
from homework.src._internals.PreprocessLinesMixin import PreprocessLinesMixin
from homework.src._internals.ReadAllLinesMixin import ReadAllLinesMixin
from homework.src._internals.SplitIntoWordsMixin import SplitIntoWordsMixin
from homework.src._internals.WriteWordCountsMixin import WriteWordCountsMixin


class WordCountApp(
    ParseArgsMixin,
    ReadAllLinesMixin,
    PreprocessLinesMixin,
    SplitIntoWordsMixin,
    CountWordsMixin,
    WriteWordCountsMixin,
):
    def __init__(self):
        self.input_folder = None
        self.output_folder = None
        self.lines = None
        self.preprocessed_lines = None
        self.words = None
        self.word_counts = None

    def run(self):

        self.parse_args()
        self.read_all_lines()
        self.preprocess_lines()
        self.split_into_words()
        self.count_words()
        self.write_word_counts()


if __name__ == "__main__":
    WordCountApp().run()
