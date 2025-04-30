from .folder_manager import FolderManager
from .result_saver import ResultSaver
from .word_counter import WordCounter


class WordCountProcess:
    """Encapsulates the word count process."""

    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.folder_manager = FolderManager()
        self.word_counter = WordCounter()
        self.result_saver = ResultSaver()

    def run(self):
        """Run the word count process."""
        # Count words in the input folder
        counter = self.word_counter.count_words_in_folder(self.input_folder)

        # Create the output folder
        self.folder_manager.create_output_folder(self.output_folder)

        # Save the results
        self.result_saver.save_counting_results(counter, self.output_folder)
