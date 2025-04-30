import os


class FolderManager:
    """Handles folder creation and deletion operations."""

    @staticmethod
    def create_output_folder(output_folder):
        """Create the output folder. If it exists, delete all files inside it."""
        if os.path.exists(output_folder):
            FolderManager.delete_files_in_folder(output_folder)
        else:
            os.makedirs(output_folder)

    @staticmethod
    def delete_files_in_folder(folder):
        """Delete all files in the specified folder."""
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.remove(file_path)
