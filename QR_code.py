import customtkinter as ct
from PIL import Image
from qrcode import QRCode, constants

ct.set_appearance_mode("dark")
ct.set_default_color_theme('green')

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("minimal example app")
        self.minsize(800, 500)
        self.title("QR code generator")

        self.roboto_font = ct.CTkFont(family='Roboto', size=22, weight='bold')

        self.frame = ct.CTkFrame(master=self, width=800, height=500)
        self.frame.pack(padx=20, pady=20)

        self.qr_image = ct.CTkButton(master=self.frame, width=400, height=400, text='Here will be a QR code!', hover=False, state="disabled", font=self.roboto_font)
        self.qr_image.grid(row=0, column = 0, padx=(20, 0), pady=20)

        self.menu_frame = ct.CTkFrame(master=self.frame, width=300, height=500, fg_color='transparent')
        self.menu_frame.grid(row=0, column = 1)

        self.title_text = ct.CTkTextbox(master=self.menu_frame, width=300, height=30, fg_color='transparent', border_spacing=10, font=self.roboto_font)
        self.title_text.insert('0.0', '      QR code generator')
        self.title_text.pack()

        self.wellcome_text = ct.CTkTextbox(master=self.menu_frame, width=300, height=140, fg_color='transparent', font=('Roboto', 14)) # transparent
        self.wellcome_text.insert('0.0',
                            'Create QR code image from text or link.\n' 
                            'By default it will have name "QR code.png"\n'
                            'or you can call it yourself. Also you can\n'
                            "check QR code here after it's creating.\n"
                            'The file will be in the same folder(directory)\nas this app.')
        self.wellcome_text.pack(padx=(15, 0), pady=(15, 0))

        self.text_url = ct.CTkEntry(master=self.menu_frame, width=250, height=35, placeholder_text="Write text here or paste link")
        self.text_url.pack(pady=10)

        self.name_file = ct.CTkEntry(master=self.menu_frame, width=250, height=35, placeholder_text="Write name of file here, if you want")
        self.name_file.pack(pady=10)

        self.button = ct.CTkButton(master=self.menu_frame, command=self.qrcode_func, width=250, height=40, text="Create QR code", font=('Roboto', 20))
        self.button.pack(pady=(20, 0))

    def qrcode_func(self):
        qr = QRCode(version=1, error_correction=constants.ERROR_CORRECT_L, box_size=10, border=2)
        qr.add_data(self.text_url.get())
        qr.make(fit=True)
        qrcode_img = qr.make_image(fill_color="black", back_color='white')

        if self.name_file.get() == '':
            qrcode_img.save(f"QR code.png")
            q_image = ct.CTkImage(dark_image=Image.open(f"QR code.png"), size=(350, 350))
        else:
            qrcode_img.save(f"{self.name_file.get()}.png")
            q_image = ct.CTkImage(dark_image=Image.open(f"{self.name_file.get()}.png"), size=(350, 350))

        self.qr_image.configure(image=q_image)
        self.qr_image.configure(width=400) # without this it's not working properly idk why
        self.qr_image.configure(text='')


if __name__ == "__main__":
    app = App()
    app.mainloop()