from book_reader import BookReader
import os
import time

def check_selection() -> None:
    directory_path = "input"
    if os.path.isdir(directory_path):
        print(f"Directory '/{directory_path}' exists!")

    else:
        print(f"Directory '/{directory_path}' does not exist!")
        print("Creating now...")
        os.mkdir("input")
    print("")

def print_selection(selection: list[str]):
    if len(selection) == 0:
        print("No files to read.")
        return

    print("Current Options: ")
    for index, item in enumerate(selection):
        print(f"{index + 1}. {item}")
    print("")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    active: bool = True

    check_selection()
    while active:
        book_selection = [item for index, item in enumerate(os.listdir("input"))]
        print_selection(book_selection)

        selected = input(f"What would you like to read? Choose the number: ")
        if selected.isnumeric() and int(selected) < len(book_selection) + 1:
            current_book = BookReader()
            current_book.set_file(os.getcwd() + "/input/" + book_selection[int(selected) - 1])
            print("/input/" + book_selection[int(selected) - 1])
            current_book.setup()
            print(f"Selected {book_selection[int(selected) -1]} ({current_book.total_pages} pages)")

            try_pages: bool = True

            page_start = int(input(f"Input the starting page: "))
            page_end = int(input(f"Input the ending page: "))
            current_book.read(page_start, page_end)

        elif selected == "break":
            break

        else:
            print("_________________________")
            print("Invalid input. Try again.")
            print("_________________________ \n")
        print("\n \n \n")
        time.sleep(1)
