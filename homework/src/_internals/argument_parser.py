import argparse


class ArgumentParser:
    """Handles parsing command-line arguments."""

    @staticmethod
    def parse_arguments():
        """Parse command-line arguments."""
        parser = argparse.ArgumentParser(
            description="Word count utility for processing text files."
        )
        parser.add_argument("input_folder", type=str, help="Path to the input folder")
        parser.add_argument("output_folder", type=str, help="Path to the output folder")
        return parser.parse_args()
