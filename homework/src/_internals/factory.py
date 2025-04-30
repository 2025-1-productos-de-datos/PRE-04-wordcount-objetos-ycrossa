from .word_count_process import WordCountProcess


class WordCountProcessFactory:
    """Factory class to create and configure a WordCountProcess instance."""

    @staticmethod
    def create(input_folder, output_folder):
        """Create and return a WordCountProcess instance."""
        return WordCountProcess(input_folder=input_folder, output_folder=output_folder)
