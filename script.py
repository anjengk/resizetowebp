import os
from PIL import Image

def resize_product_images(input_folder, output_folder='produk_optimized', max_width=1000):
    os.makedirs(output_folder, exist_ok=True)
    allowed_ext = ['.jpg', '.jpeg', '.png']

    for file in os.listdir(input_folder):
        name, ext = os.path.splitext(file)
        if ext.lower() in allowed_ext:
            try:
                img_path = os.path.join(input_folder, file)
                with Image.open(img_path) as img:
                    if img.width > max_width:
                        ratio = max_width / img.width
                        new_height = int(img.height * ratio)
                        img = img.resize((max_width, new_height), Image.LANCZOS)

                    output_path = os.path.join(output_folder, f"{name}.webp")
                    img.save(output_path, "WEBP", quality=85, optimize=True)
                    print(f"✔ {file} → {output_path}")
            except Exception as e:
                print(f"❌ Gagal memproses {file}: {e}")

if __name__ == "__main__":
    folder = input("Masukkan path folder foto produk: ")
    resize_product_images(folder)
