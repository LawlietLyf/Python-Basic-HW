
import os
from PyPDF2 import PdfReader, PdfWriter


def merge_first_pages(source_folder, output_file):
    
    writer = PdfWriter()

    # 遍历指定文件夹内的所有文件
    for filename in os.listdir(source_folder):
        # 检查文件是否为PDF文件
        if filename.endswith('.pdf'):
            # 构建完整的文件路径
            file_path = os.path.join(source_folder, filename)

            # 以二进制读模式打开PDF文件
            with open(file_path, 'rb') as file:
                # 创建一个PdfFileReader对象
                reader = PdfReader(file)

                # 检查PDF文件至少有一页
                if len(reader.pages) > 0:
                    # 获取PDF的第一页并添加到writer对象中
                    writer.add_page(reader.pages[0])

    # 打开（或创建）输出文件，准备写入合并后的PDF
    with open(output_file, 'wb') as output_pdf:
        # 将合并的页面写入输出文件
        writer.write(output_pdf)

# 调用函数，合并'mypdfs'文件夹中的PDF的第一页到一个名为'new.pdf'的文件中
merge_first_pages('mypdfs', 'new.pdf')