from ._internals.argument_parser import ArgumentParser
from ._internals.factory import WordCountProcessFactory


def main():
    """Main function to parse arguments and run the word count process."""
    args = ArgumentParser.parse_arguments()
    process = WordCountProcessFactory.create(
        input_folder=args.input_folder, output_folder=args.output_folder
    )
    process.run()


if __name__ == "__main__":
    main()
