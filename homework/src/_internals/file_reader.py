import os


class FileReader:
    def __init__(self, input_folder):
        self.input_folder = input_folder

    def read_all_lines(self):

        lines = []
        for filename in os.listdir(self.input_folder):
            file_path = os.path.join(self.input_folder, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                lines.extend(f.readlines())
        return lines
