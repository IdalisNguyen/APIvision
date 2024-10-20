import os
import io
from google.cloud import vision
from google.cloud import vision_v1
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

# Cấu hình đường dẫn đến file JSON chứa thông tin xác thực
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ocr-version-01-dc686160df09.json'

# Khởi tạo client
client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'F:\\Phuoc\\Đề Tài Cơ Sở\\google\\VisionAPI\\data\\23.9'
IMAGE_FILE = '21.9_mau1.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

# Chuẩn bị hình ảnh cho Crop Hints
image = vision_v1.types.Image(content=content)

# Cấu hình yêu cầu để chỉ định số lượng gợi ý cắt ảnh (Crop Hint)
crop_hints_params = vision_v1.CropHintsParams(aspect_ratios=[1.0])  # Sử dụng tỉ lệ khung hình 1:1
image_context = vision_v1.ImageContext(crop_hints_params=crop_hints_params)

# Gửi yêu cầu Crop Hints
response = client.crop_hints(image=image, image_context=image_context)

# Mở hình ảnh và tạo đối tượng ImageDraw để vẽ khung
with Image.open(FILE_PATH) as img:
    draw = ImageDraw.Draw(img)
    
    # Vẽ các khung Crop Hints lên hình ảnh
    for crop_hint in response.crop_hints_annotation.crop_hints:
        vertices = crop_hint.bounding_poly.vertices
        box = [(vertex.x, vertex.y) for vertex in vertices]
        draw.polygon(box, outline="red", width=5)  # Vẽ khung màu đỏ với độ dày là 5

    # Hiển thị hình ảnh với khung Crop Hints
    plt.figure(figsize=(10, 10))  # Điều chỉnh kích thước hình ảnh
    plt.imshow(img)
    plt.axis('on')  # Hiển thị trục tọa độ
    plt.show()
