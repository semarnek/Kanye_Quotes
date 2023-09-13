from tkinter import *
import requests


def get_quote():
    quote_req = requests.get(url="https://api.kanye.rest/")
    # quote_req.raise_for_status()
    quote_dict = quote_req.json()
    canvas.itemconfig(quote_text, text=f"{quote_dict['quote']}")


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)


canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="", width=250, font=("Comic Sans MS", 20, "bold"), fill="black")
canvas.grid(row=0, column=0)
get_quote()

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)


window.mainloop()