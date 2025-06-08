# run_crawler.py
import os
import sys
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# 設定日誌
logging.basicConfig(
    filename="crawler.log",  # 日誌檔案名稱
    level=logging.ERROR,     # 記錄錯誤級別以上的訊息
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():
    try:
        os.chdir(r"d:\codeForLang\tmp\TWBingo_v2\bingo_scrapy")
        process = CrawlerProcess(get_project_settings())
        process.crawl("bingo_spider")  # 這裡對應你的 spider 名稱
        process.start()
    except Exception as e:
        # 記錄錯誤到日誌檔案
        logging.error("An error occurred while running the crawler.", exc_info=True)
        # 顯示錯誤訊息到終端
        print(f"An error occurred: {e}")
        input("Press Enter to exit...")  # 停下來讓使用者查看錯誤訊息

if __name__ == "__main__":
    main()
