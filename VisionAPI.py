import os
import io
from google.cloud import vision
from google.cloud import vision_v1
from google.cloud.vision_v1 import types

# Cấu hình đường dẫn đến file JSON chứa thông tin xác thực
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ocr-version-01-73d491d290f9.json'

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

# Truy cập các trang trong full_text_annotation
pages = response.full_text_annotation.pages

for page in pages:
    for block in page.blocks:  # Sử dụng page.blocks thay vì pages.blocks
        print('Block confidence:', block.confidence)

        for paragraph in block.paragraphs:
            print('Paragraph confidence:', paragraph.confidence)

            for word in paragraph.words:
                word_text = ''.join([symbol.text for symbol in word.symbols])
                print('Word text: {0} (confidence: {1})'.format(word_text, word.confidence))

                for symbol in word.symbols:
                    print('\tSymbol: {0} (confidence: {1})'.format(symbol.text, symbol.confidence))
