import pyttsx4
import PyPDF2
import os

from PyPDF2 import PdfReader


class BookReader:
    def __init__ (self, file: str = "") -> None:
        self.file = file
        self.total_pages = 0

    def get_file(self) -> str:
        return self.file

    def set_file(self, file_name: str) -> None:
        self.file = file_name

    def clear_file(self) -> None:
        self.file = ""

    def setup(self) -> bool:
        try:
            with open(self.file, "rb") as book:
                pdf_reader = PdfReader(book)
                self.total_pages = len(pdf_reader.pages)
                print("Setup successful!")

        except FileNotFoundError:
            print("Error: The specified PDF file was not found.")
            return False

        except Exception as e:
            print(f"An error occurred: {e}")
            return False

        return True

    def read(self, start_page: int, end_page: int):
        if start_page < 0 or end_page > self.total_pages:
            print("Invalid pages!")
            return
        try:
            with open(self.file, "rb") as book:
                pdf_reader = PyPDF2.PdfReader(book)
                extracted_text = ""
                for page_num in range(start_page, end_page):
                    page = pdf_reader.pages[page_num]
                    extracted_text += page.extract_text()

                speaker = pyttsx4.init()
                speaker.say(extracted_text)
                speaker.runAndWait()

        except FileNotFoundError:
            print("Error: The specified PDF file was not found.")

        except Exception as e:
            print(f"An error occurred: {e}")