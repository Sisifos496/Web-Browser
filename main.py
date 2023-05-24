from tkinter import *
import webbrowser
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import functools
# Importing libraries

webbrowser.Chrome("google-chrome")
# Initializing Web Browser

root = Tk()

root.config(background="orange")
# Color

star = PhotoImage(file="star.png")

logo = PhotoImage(file="Logo.png")

root.title("Web Browser")

root.resizable(False, False)

root.geometry("500x300")

def web_browsing(entry_text):
    webbrowser.open_new_tab("https://www.google.com/search?q=" + entry_text)
# Directing to Browser

all_saved = ""

def saved_ones():
    root3 = Toplevel()

    root3.config(background="orange")

    root3.title("Saved Ones")

    root3.geometry("500x100")

    root3.resizable(False, False)

    saved_ones_entry = Entry(root3)
    saved_ones_entry.place(x=140, y=50)
    saved_ones_entry.insert(0, "SAVING SEARCH")
    # Another Window about recording

    def saving():
        global all_saved
        all_saved += saved_ones_entry.get() + "\n"

        with open("saved_ones.txt", "a") as file:
            file.write(all_saved)
        time.sleep(0.5)
    # Putting Saved Ones In a File


    save_button_search = Button(root3, text="SAVE", command=saving)
    save_button_search.place(x=200, y=15)
# To save some basic search terms

all_save = ""

def editing_saved(event):
    root4 = Toplevel()

    root4.config(background="orange")

    root4.title("EDIT SAVED")

    root4.geometry("150x500")

    root4.resizable(False, False)

    with open("saved_ones.txt", "r") as file:

        all_saved_list = file.readlines()
        all_saved_list = list(filter(lambda x: x != "\n", all_saved_list))
        all_saved_list = list(filter(lambda x: x != "", all_saved_list))

    saved_buttons = []

    def delete_saved_button(button):
        button.destroy()
        saved_buttons.remove(button)

    for i in range(len(all_saved_list)):
        saved_button = Button(root4, text=all_saved_list[i], command=lambda text=all_saved_list[i]: web_browsing(text))
        saved_button.pack()
        saved_buttons.append(saved_button)
        saved_button.bind("<Button-2>", lambda event, button=saved_button: delete_saved_button(button))

    def saving_changes():
        global all_save
        for button in saved_buttons:
            all_save += button.cget("text") + "\n"
        with open("saved_ones.txt", "w") as file:
           file.write(all_save)

    save_saved_buttons = Button(root4, text="SAVE", command=saving_changes)
    save_saved_buttons.place(x=45, y=450)
# If you right click it deletes saved one and if you left click you go to website

logo_image = Label(root, image=logo, height=140, width=140, bg="orange")
logo_image.place(x=180, y=60)

star_image = Label(root, image=star, height=100, width=100, bg="orange")
star_image.place(x=-20, y=15)
star_image.bind("<Button-1>", editing_saved)

search_entry = Entry(root, borderwidth=5, bg="orange", fg="black", font="Comfortaa")
search_entry.place(x=150, y=200)

def history():
    with open("history.txt", "a") as file:
        file.write(search_entry.get())
        file.write("\n")
# Writing history into a txt file

def show_history():
    root2 = Toplevel()

    root2.config(background="orange")

    root2.title("History")

    root2.geometry("300x500")

    root2.resizable(False, False)

    with open("history.txt", "r") as file:
      history_list = file.readlines()

    all_history = ""

    for line in history_list:
        all_history += line

    history_label = Label(root2)
    history_label.pack()

    history_text = Text(history_label)
    history_text.pack()
    # Showing a window with

    def saving_history():
        save_of_history = history_text.get("1.0", "end")
        with open("history.txt", "w") as file:
            file.write(save_of_history)

    save_button = Button(root2, text="SAVE", command=saving_history)
    save_button.place(x=10, y=400)

    history_text.insert("1.0", all_history)

    def deleting_history():
        history_text.delete("1.0", "end")

    deleting_history_button = Button(root2, text="DELETE HISTORY", command=deleting_history)
    deleting_history_button.place(x=80, y=400)
    # Creating a text area the history is written and putting buttons to delete and when rearranged to save

search_button = Button(root, text="SEARCH", command=lambda: [web_browsing(search_entry.get()), history()], font="Comfortaa")
search_button.place(x=208, y=250)

search_entry.bind("<Return>", lambda event: search_button.invoke())

def built_in_web_browsing(search_entry):
    options = Options()

    options.add_argument("--headless")

    options.add_argument("--disable-gpu")
    # Searching without showing browser

    browser = webdriver.Safari()

    url = "https://www.google.com/search?q=" + search_entry

    browser.get(url)

    titles = browser.find_elements(By.XPATH, "//div[@class='yuRUbf']//h3")

    links = browser.find_elements(By.XPATH, '//div[@class="yuRUbf"]//a')

    urls = [link.get_attribute('href') for link in links]

    root5 = Toplevel()

    root5.config(background="orange")

    root5.geometry("600x600")

    def direct(example_url):
        webbrowser.open(example_url)

    for i in range(5):
        search_label = Label(root5, text=titles[i].text)
        link_button = Button(root5, text=urls[i], command=functools.partial(direct, urls[i]))
        search_label.pack()
        link_button.pack()
       # Scraping the first 5 results in google and then opening a new page and putting title and the links together

built_in_search_button = Button(root, text='!!Search!!', command=lambda: [built_in_web_browsing(search_entry.get()), history()], font="Comfortaa")
built_in_search_button.place(x=5, y=270)

history_button = Button(root, text="HISTORY", font="Comfortaa", command=show_history, width=8)
history_button.place(x=383, y=10)

saved_ones_button = Button(root, text="SAVED", font="Comfortaa", command=saved_ones, width=8)
saved_ones_button.place(x=10, y=10)

root.mainloop()
