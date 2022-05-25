print("访问https://github.com/Chenzsabc/PDF_combiner以获得支持信息"
from PyPDF2 import PdfFileReader
from PyPDF2 import PdfFileWriter
import os
def GetFileName(dir_path):
    file_list = [os.path.join(dirpath, filesname) \
                 for dirpath, dirs, files in os.walk(dir_path) \
                 for filesname in files]
    return file_list
def MergePDF(dir_path, file_name):
    output = PdfFileWriter()
    outputPages = 0
    file_list = GetFileName(dir_path)
    for pdf_file in file_list:
        print("文件：%s" % pdf_file.split('\\')[-1], end=' ')
        # 读取PDF文件
        input = PdfFileReader(open(pdf_file, "rb"))
        # 获得源PDF文件中页面总数
        pageCount = input.getNumPages()
        outputPages += pageCount
        print("页数：%d" % pageCount)
        # 分别将page添加到输出output中
        for iPage in range(pageCount):
            output.addPage(input.getPage(iPage))
    print("\n合并后的总页数:%d" % outputPages)
    # 写入到目标PDF文件
    print("合并中")
    with open(os.path.join(dir_path, file_name), "wb") as outputfile:
        # 注意这里的写法和正常的上下文文件写入是相反的
        output.write(outputfile)
    print("合并完成")

def list_all_files(rootdir):
    import os
    _files = []
	# 列出文件夹下所有的目录与文件
    list = os.listdir(rootdir)
    for i in range(0, len(list)):
		# 构造路径
        path = os.path.join(rootdir, list[i])
		# 判断路径是否为文件目录或者文件
		# 如果是目录则继续递归
        if os.path.isdir(path):
            _files.extend(list_all_files(path))
        if os.path.isfile(path):
            _files.append(path)
    return _files
if __name__ == '__main__':
    # 设置存放多个pdf文件的文件夹
    dir_path = input("输入路径：")
    print(list_all_files(dir_path))
    # 目标文件的名字
    file_name = "我也不知道该取什么名字.pdf"
    MergePDF(dir_path, file_name)
