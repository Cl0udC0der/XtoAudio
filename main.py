from book_reader import BookReader
import os
from dotenv import load_dotenv
from voice_player import VoicePlayer

def check_input() -> None:
    directory_path = "input"
    if os.path.isdir(directory_path):
        print(f"Directory '/{directory_path}' exists!")

    else:
        print(f"Directory '/{directory_path}' does not exist!")
        print("Creating now...")
        os.mkdir("input")
    print("")

def check_output() -> None:
    directory_path = "audio"
    if os.path.isdir(directory_path):
        print(f"Directory '/{directory_path}' exists!")

    else:
        print(f"Directory '/{directory_path}' does not exist!")
        print("Creating now...")
        os.mkdir("audio")
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
    check_input()
    check_output()
    load_dotenv()

    while active:
        print("1. Read from a PDF file.")
        print("2. Browse audio files.")
        print("3. Make dummy audio.")
        print("4. Exit")
        print("")
        action_choice = input("What would you like to do? Choose number: ")
        print("")


        match action_choice:
            # Read a PDf
            case '1':
                book_selection = [item for index, item in enumerate(os.listdir("input"))]
                print_selection(book_selection)
                selected = input(f"What would you like to read? Choose the number: ")

                if selected.isnumeric() and int(selected) < len(book_selection) + 1:
                    current_book = BookReader()
                    current_book.set_file(os.getcwd() + "/input/" + book_selection[int(selected) - 1])
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

            # Listen to Audio
            case '2':
                make_sound = True
                while make_sound:
                    audio_selection = [item for index, item in enumerate(os.listdir("audio"))]
                    print_selection(audio_selection)
                    selected = input(f"What would you like to read? Choose the number: ")


                    if selected.isnumeric() and int(selected) < len(audio_selection) + 1:
                        print(f"Selected {audio_selection[int(selected) - 1]}")
                        speaker = VoicePlayer(os.getenv("ELEVENLABS_API_KEY"))
                        speaker.play_recorded(f"{os.getcwd()}/input/{audio_selection[int(selected) - 1]}.mp3")

                    elif selected == "break":
                        break

                    else:
                        print("_________________________")
                        print("Invalid input. Try again.")
                        print("_________________________ \n")
                    print("\n \n \n")

            # Make dummy audio
            case '3':
                content = input("What do you want to turn to audio?\n ")
                speaker = VoicePlayer(os.getenv("ELEVENLABS_API_KEY"))
                audio = speaker.make_audio(content)
                path = speaker.save_audio(audio)
                speaker.play_recorded(path)
                print(f"Dummy made at {path}")

            #exit
            case _:
                break