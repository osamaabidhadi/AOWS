from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
import threading
import os

from img_stg import ImgStg
from file_handler import fileHandler
from utils import compatible_path

#ALL PATHS
DIR_PATH = compatible_path(os.path.dirname(os.path.realpath(__file__)))
TEXT_PATH = ""
IMAGE_PATH = ""
DEST_PATH = DIR_PATH
ERROR = ""
STG = ImgStg()

RESOURCES = f"{DIR_PATH}\\resources\\"

LOGS = {
    "img_path":0,
    "txt_path":0,
    "dest_path":0
}


def change_log(reset=False):
    text_log = ""
    T.config(state=NORMAL)
    T.delete('1.0', END)

    if reset == False:
        # TEXT PATH
        if LOGS["txt_path"] == 0:
            text_log += "0_0-TEXT FILE IS NOT SELECTED!(not required for data extraction)\n\n"
        else:
            text_log += "^_^-TEXT FILE IS SELECTED.\n\n"
        # IMAGE PATH
        if LOGS["img_path"] == 0:
            text_log += "0_0-IMAGE FILE IS NOT SELECTED!\n\n"
        else:
            text_log += "^_^-IMAGE FILE IS SELECTED.\n\n"
        # DESTINATION PATH
        if LOGS["dest_path"] == 0:
            text_log += "0_0-DEST FOLDER IS NOT SELECTED!\n\n"
        else:
            text_log += "^_^-DEST FOLDER IS SELECTED.\n\n"
    
    T.insert(END,text_log)
    T.config(state=DISABLED)
    


    

def get_error(mode="embed"):
    """
    This function checks if the required paths are selected.
    and returns 0 if there is no error.
    """
    global ERROR
    if mode == "embed": # if embed is selected
        if TEXT_PATH == "":
            messagebox.showinfo("INFO", "TEXT PATH IS NOT SELECTED !")
            return 1
    
    if IMAGE_PATH =="":
        messagebox.showinfo("INFO", "IMAGE PATH IS NOT SELECTED !")
        return 1
    
    return 0
    



def select_text_btn():
    """
    this function selects the text file and checks if it is a txt file.
    """
    global TEXT_PATH
    TEXT_PATH = filedialog.askopenfilename()
    if "txt" != TEXT_PATH[len(TEXT_PATH)-3:]:
        TEXT_PATH = ""
    else:
        LOGS["txt_path"] = 1
    
    change_log()


def select_img_btn():
    """
    this function selects the image file and checks if it is a image file.
    """
    global IMAGE_PATH, IMAGE
    IMAGE_PATH = filedialog.askopenfilename()
    IMAGE = ImageTk.PhotoImage(Image.open(compatible_path(IMAGE_PATH)).resize((295,279)))
    label1.configure(image=IMAGE)
    label1.image=IMAGE
    LOGS["img_path"] = 1
    change_log()

def select_dest_btn():
    """
    this function selects the destination folder.
    """
    global DEST_PATH
    DEST_PATH = filedialog.askdirectory()
    LOGS["dest_path"] = 1
    change_log()


def embed_btn():
    """
    this function starts the embedding process.
    """
    if get_error("embed") == 0:
        text = fileHandler.read(TEXT_PATH)
        print(text,IMAGE_PATH)
        threading.Thread(target=STG._merge_txt, args=(IMAGE_PATH,TEXT_PATH,DEST_PATH)).start()

def extract_btn():
    """
    this function starts the extraction process.
    """
    if get_error("extract") == 0:
        threading.Thread(target=STG._unmerge_txt, args=(IMAGE_PATH, DEST_PATH)).start()

def reset_btn():
    """
    this function resets the settings.
    """
    global TEXT_PATH, IMAGE_PATH, DEST_PATH
    if messagebox.askquestion("Reset Settings", "Are you sure ?\nSelected paths will be deleted !") == "yes":
        TEXT_PATH = ""
        IMAGE_PATH = ""
        DEST_PATH = DIR_PATH

        LOGS["txt_path"] = 0
        LOGS["img_path"] = 0
        LOGS["dest_path"] = 0

        T.delete('1.0', END)

        label1.configure(image="")
        label1.image=""

        change_log(reset=True)


# GUI - TKINTER
window = Tk()
window.title("AOWZ") # title of the window
window.geometry("689x665") # size of the window
window.configure(bg = "#87ceeb") # background color of the window

canvas = Canvas(
    window,
    bg = "#87ceeb",
    height = 665,
    width = 689,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = compatible_path(RESOURCES + "background.png"))
background = canvas.create_image(
    344.5, 332.5,
    image=background_img)

img0 = PhotoImage(file = compatible_path(RESOURCES + "img0.png"))

b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = reset_btn,
    relief = "flat")

b0.place(
    x = 606, y = 227,
    width = 69,
    height = 72)

img1 = PhotoImage(file= compatible_path(RESOURCES + "img1.png"))

b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = embed_btn,
    activebackground="#87ceeb",
    relief = "flat")

b1.place(
    x = 21, y = 450,
    width = 108,
    height = 111)

img2 = PhotoImage(file = compatible_path(RESOURCES + "img2.png"))

b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = extract_btn,
    activebackground="#87ceeb",
    relief = "flat")

b2.place(
    x = 195, y = 450,
    width = 108,
    height = 111)

img3 = PhotoImage(file = compatible_path(RESOURCES + "img3.png"))

b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_dest_btn,
    activebackground="#87ceeb",
    relief = "flat")

b3.place(
    x = 21, y = 316,
    width = 74,
    height = 75)

img4 = PhotoImage(file = compatible_path(RESOURCES + "img4.png"))

b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_img_btn,
    activebackground="#87ceeb",
    relief = "flat")

b4.place(
    x = 21, y = 230,
    width = 74,
    height = 75)

img5 = PhotoImage(file = compatible_path(RESOURCES + "img5.png"))

b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = select_text_btn,
    activebackground="#87ceeb",
    relief = "flat")

b5.place(
    x = 21, y = 144,
    width = 74,
    height = 75)



# compatible_path function is used to make the path compatible with the os !

IMAGE = Image.open(compatible_path(RESOURCES) + "no_image.png")

p1 = PhotoImage(file = compatible_path(RESOURCES + "ico_menu.png"))
window.iconphoto(False, p1)

label1 = Label()
label1.place(x=360, y=360)

T = Text(window, height = 5, width = 65)
T.insert(END, "...")
T.place(x=55, y=35)
T.config(borderwidth=0,state=DISABLED)

window.resizable(False, False)
window.mainloop()
