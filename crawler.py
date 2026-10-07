import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://news.cctv.com/tech/"

try:
    resp = requests.get(url, headers=headers, timeout=10)
    # 手动指定网页编码
    resp.encoding = "utf-8"
    resp.raise_for_status()
    time.sleep(1)

    soup = BeautifulSoup(resp.text, "html.parser")
    all_text = soup.get_text(strip=True)

    save_path = r"D:\python_crawler_project\data_output\result.txt"
    with open(save_path, "w", encoding="utf-8") as f:
        f.write(all_text)

    print("抓取完成！")
    print(f"文件保存位置：{save_path}")
    print("请前往D盘打开result.txt查看内容，控制台不再打印网页文本")

except Exception as e:
    print("访问出错：", e)
