from tkinter import *from tkinter.filedialog import askopenfilenamefrom PIL import Image, ImageTk, ImageDraw,ImageFontfrom tkinter import filedialogdef select_image():    # ask the user for the filename    file_path = filedialog.askopenfilename()    # only show the image if they chose something    if file_path:        #hiding the entry        entry.place(x=1000000,y=1000000)        with Image.open(file_path) as im:            label.config(text="here is your watermarked image click the save button.")            #hiding the browse button            button.place(x=100000000000,y=100000000000000)            draw = ImageDraw.Draw(im)            font = ImageFont.truetype("BedPillow-GOoeA.otf", 50)            draw.text((10,10),f"{entry.get()}", font=font)            canvas.image_tk = ImageTk.PhotoImage(im)            # configure the canvas item to use this image            canvas.itemconfigure(image_id, image=canvas.image_tk)            def save_image():                file = filedialog.asksaveasfile(mode='wb', defaultextension=".png",                                                filetypes=(("PNG file", "*.png"), ("All Files", "*.*")))                if file:                    im.save(file)            save_image = Button(text="save image",command=save_image)            save_image.place(x=350, y=580)window = Tk()window.title(string="image watermark app")window.config(padx=100,pady=100,background="green")label = Label(text="click the button below and choose an image to add a text watermark.",background="green")label.place(x=200,y=-80)button = Button(text="Browse images",command=select_image)button.place(x=350,y=-30)#the canvas where the image will be displaycanvas = Canvas(window, width= 800, height=800, bg="grey")canvas.pack()image_id = canvas.create_image(0,0, anchor="nw")entry = Entry(width=40)entry.insert(END, string="Enter the watermark text for your image")entry.place(x=300, y=250)window.mainloop()