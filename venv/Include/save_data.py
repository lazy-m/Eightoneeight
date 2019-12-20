import requests
import os


def download_file(url, local_path, requests):
    """下载数据"""
    file_name = url[0].split('/')[-1]
    # 检查本地是否存在这个文件夹
    if not os.path.exists(local_path):
        os.makedirs(local_path)

    with open(local_path + "\\" + file_name, "wb") as file:
        file.write(requests.content)
