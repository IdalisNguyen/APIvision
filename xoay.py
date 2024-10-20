import os
import io
from google.cloud import vision
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

# Cấu hình đường dẫn đến file JSON chứa thông tin xác thực
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ocr-version-01-dc686160df09.json'

# Khởi tạo client
client = vision.ImageAnnotatorClient()

FOLDER_PATH = r'F:\\Phuoc\\Đề Tài Cơ Sở\\google\\VisionAPI\\data\\23.9'
IMAGE_FILE = '21.9_mau1.jpg'
FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

with io.open(FILE_PATH, 'rb') as image_file:
    content = image_file.read()

image = vision_v1.types.Image(content=content)
response = client.document_text_detection(image=image)

# In toàn bộ văn bản OCR được nhận dạng
docText = response.full_text_annotation.text
print(docText)
