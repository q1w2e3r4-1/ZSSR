from PIL import Image
import os

# 指定包含JPG文件的目录
jpg_directory = './jpgs'
# 指定保存PNG文件的目录
png_directory = './test_data'

# 确保输出目录存在
if not os.path.exists(png_directory):
    os.makedirs(png_directory)

# 遍历目录中的所有文件
for filename in os.listdir(jpg_directory):
    if filename.lower().endswith('.jpg') or filename.lower().endswith('.jpeg'):
        # JPG文件的完整路径
        jpg_file_path = os.path.join(jpg_directory, filename)
        # PNG文件的完整路径
        png_file_path = os.path.join(png_directory, f"{os.path.splitext(filename)[0]}.png")

        # 打开图像并转换为PNG
        with Image.open(jpg_file_path) as img:
            img.save(png_file_path, 'PNG')

print("转换完成。")