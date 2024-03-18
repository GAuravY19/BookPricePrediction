import os
import shutil
from src.logger import logging


def MoveData(source_folder:str,
             destination_folder:str,
             file_to_move:str) -> None:

    """
    Move data from one location to another.

    Args:
        source_folder (str): The path to the source location of the data.
        destination_folder (str): The path to the destination location where the data will be moved.
        file_to_move (str): The name of the file to be moved.

    Raises:
        FileNotFoundError: If the specified source_folder or file_to_move does not exist.
    """
    logging.info("Files Moving started.")

    if not os.path.exists(source_folder):
        logging.info(f"The source path does not exists: {source_folder}")
        raise FileNotFoundError(f"The  source path {source_folder} does not exists.")

    if not os.path.exists(destination_folder):
        logging.info(f"The destination path does not exists. Creating it.")
        os.makedirs(destination_folder, exist_ok=True)

    files = os.listdir(source_folder)

    for file in files:
        if file == file_to_move:
            source_file = os.path.join(source_folder, file)
            destination_file = os.path.join(destination_folder, file)

            shutil.move(source_file, destination_file)

            logging.info("Files moving completed.")

    else:
        logging.info(f"{file_to_move} not found in specified location.")
        raise FileNotFoundError(f"{file_to_move} not found.")

