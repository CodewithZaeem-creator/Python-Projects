import qrcode
import os


print("================================")
print("       🔳 QR Code Generator     ")
print("================================")

while True:
    print("\nwhat do you want to do")
    print("1-Generate a qrcode")
    print("2-quit")

    Choice=input("\nEnter your choice:").strip()
    if Choice=="2":
        print("Thanks for Using QR Code Generator  ")
        break

    elif Choice=="1":
        # get link

        link=input("Enter the link of the source:").strip()
        if not link:
            print("You didn't enter anything.Try again")
            continue
        # get the filename

        filename=input("Save as(e.g. Myqr):")
        if not filename:
            filename="Qrcode"

        # get custome color

        print("\n choose a color(or press enter to skip):")
        fill=input("QR CODE color(e.g. Black, Darkblue or red)):").strip()
        back=input("background color(e.g. White, yello):").strip()
        if not fill:
            fill = "black"
        if not back:
            back = "white"
        

        # get size
        size = input("QR code size 1-20 (or press Enter for default 10): ").strip()
        if not size:
            size = 10
        else:
            size=int(size)

        # genrate Qrcode

        qr=qrcode.QRCode(box_size=size)
        qr.add_data(link)
        qr.make(fit=True)
        img=qr.make_image(fill_color=fill, back_color=back)

        # save it
        
        full_name=f"{filename}.png"
        img.save(full_name)
        print(f"\n✅ QR code saved as {full_name}!")

        # open it automatically

        os.startfile(full_name)
    else:
        print("❌ Invalid choice. Enter 1 or 2.")

        

        
        

         

