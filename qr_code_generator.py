import tkinter
import customtkinter as ctk
import qrcode
import tkinter.messagebox as msgbox

def generate_qr():
    data = entry_url.get()
    filename = entry_file.get()

    if not data or not filename:
        msgbox.showerror("Fill required areas", "Please fill out the required areas.")
        return

    if filename.endswith('.png'):
        filename = filename[:-4]

    qr = qrcode.QRCode(box_size=10, border=1)
    qr.add_data(data)
    image = qr.make_image(fill_color='black', back_color='white')
    image.save(f"{filename}.png")
    msgbox.showinfo("QR Code Generated", f"{filename}.png successfully saved.")

app = ctk.CTk()
app.title("GRCodeGenerator")
app.config(bg="black")
app.geometry("300x400")

#Here is main frame
frame = ctk.CTkFrame(master=app, fg_color="black")
frame.pack(pady=20, padx=20, fill="both", expand=True)

#Here is main label
label = ctk.CTkLabel(master=frame, text="QRCode Generator", font=("Poppins", 24, "bold"))
label.pack(pady=(20,10))

#Here is first text label and entry
label_url = ctk.CTkLabel(master=frame, text="Enter the text or URL", font=("Poppins", 14 ))
label_url.pack(pady=(20,0), anchor="w", padx=12)
entry_url = ctk.CTkEntry(master=frame, height=26, corner_radius=8)
entry_url.pack(pady=5, padx=12, fill="x")

#Here is second text label and entry
label_file = ctk.CTkLabel(master =frame, text="Enter file name", font=("Poppins", 14 ))
label_file.pack(pady=(20,0), anchor="w", padx=12)
entry_file = ctk.CTkEntry(master=frame, height=26, corner_radius=8)
entry_file.pack(pady=5, padx=12, fill="x")

#Here is "Send" button
send_button = ctk.CTkButton(master=frame, text="Send", width=120, height=40, corner_radius=10, cursor="hand2", command=generate_qr, fg_color="black", hover_color="gray")
send_button.pack(pady=(40,20))
app.mainloop()

