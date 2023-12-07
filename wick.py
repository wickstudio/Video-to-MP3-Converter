import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import pyfiglet
from colorama import init, Fore, Style
import os

init(autoreset=True)

def show_banner():
    banner = pyfiglet.figlet_format("WICK STUDIO")
    print(Fore.CYAN + Style.BRIGHT + banner)

def select_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def convert_to_mp3(video_file):
    video_clip = VideoFileClip(video_file)
    audio_clip = video_clip.audio
    output_file = os.path.splitext(video_file)[0] + ".mp3"
    audio_clip.write_audiofile(output_file)
    print(Fore.GREEN + f"MP3 file saved as: {output_file}")
    audio_clip.close()
    video_clip.close()

def main_menu():
    show_banner()
    choice = input(Fore.YELLOW + "Choose an option:\n1. Convert video to MP3\n2. Exit\nEnter choice (1 or 2): ")
    if choice == '1':
        video_path = select_file()
        if video_path:
            convert_to_mp3(video_path)
        else:
            print(Fore.RED + "No file selected.")
    elif choice == '2':
        print(Fore.MAGENTA + "Exiting the tool.")
        exit()

if __name__ == "__main__":
    main_menu()
