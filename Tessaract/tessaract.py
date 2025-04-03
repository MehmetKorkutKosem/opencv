from PIL import Image
import pytesseract


image = Image.open("D:\\opencv\\tst_images\\text.png")

# Görüntüyü işleyip, içerisindeki yazıyı metne dönüştürüyoruz. 'lang="eng"' ile dilin İngilizce olduğunu belirtiyoruz.
text = pytesseract.image_to_string(image, lang="eng")

# Çıkarılan metni ekrana yazdırıyoruz.
print(text)