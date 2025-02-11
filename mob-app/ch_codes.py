import qrcode
import random
import os
from PIL import Image 

def generate_code():
    random_number = random.randint(0, 999999)
    return f"ch{random_number:06d}"  

def generate_qrcode(text, filename, logo_path=None):
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_H,  
        box_size=10, 
        border=4,  
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white").convert('RGB')
    
    if logo_path:
        logo = Image.open(logo_path)
        logo_size = min(img.size) // 5 
        logo = logo.resize((logo_size, logo_size), Image.Resampling.LANCZOS)

        img_width, img_height = img.size
        logo_position = (
            (img_width - logo_size) // 2,
            (img_height - logo_size) // 2
        )

        img.paste(logo, logo_position)

    img.save(filename) 

def get_unique_filename(folder, base_name="qrcode", extension="png"):
    """Generate a unique filename by incrementing a number."""
    counter = 1
    while True:
        filename = os.path.join(folder, f"{base_name}{counter}.{extension}")
        if not os.path.exists(filename):
            return filename
        counter += 1

if __name__ == "__main__":
    file_path = 'G:/opportunities/ALX/CHEEMBA/backend/qrcodes'
   
    os.makedirs(file_path, exist_ok=True)

    code = generate_code() 
    print(f"Generated code: {code}")
 
    filename = get_unique_filename(file_path)
    logo_path = "logo.png"  
    generate_qrcode(code, filename, logo_path) 
    
    print(f"QR code saved as '{filename}'")