import this

import pyttsx4
import PyPDF2


class BookReader:
    def __init__ (self, file: str = "") -> None:
        this.file = file
        this.total_pages = 0

    def scan_book(self, file_name: str = "./input/Indistractible(Nir Eyal).pdf") -> None:
        with open(file_name, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            this.total_pages = len(pdf_reader.pages)
            speaker = pyttsx4.init()
            page = pdf_reader.pages[20]
            text = page.extract_text()
            speaker.say(text)
            speaker.runAndWait()

    def set_file(self, file_name: str) -> None:
        this.file = file_name


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    nir_eyal = BookReader()
    nir_eyal.scan_book()