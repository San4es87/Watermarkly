from tkinter import *
from PIL import  Image, ImageDraw, ImageFont
from tkinter import filedialog



# ---------------------------- Open image ------------------------------- #
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def open_img():
    x = openfn()
    img = Image.open(x)
    drawing = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 30)
    drawing.text((0, 0), text="Alex", fill=2, font=font)
    img.show()
    img.save("photo_with_watermark.jpg")


# ---------------------------- UI SETUP ------------------------------- #

root = Tk()
root.title("Watermark")
root.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="watermark_logo.png")
canvas.create_image(100, 100, image=photo)
canvas.pack()

my_label = Label(root,
                 text="Watermark", font=("Arial", 25))
my_label.pack()



btn = Button(root, text='open image', command=open_img)
btn.pack()


root.mainloop()
