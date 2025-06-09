# run_crawler.py
import os
import sys
import logging
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

def main():
    try:
        # 將工作目錄設為腳本或執行檔所在位置
        base_dir = os.path.dirname(
            os.path.abspath(sys.executable if getattr(sys, "frozen", False) else __file__)
        )
        os.chdir(base_dir)

        # 在設定目錄後才初始化日誌檔案，避免因排程器目錄不同導致找不到檔案
        logging.basicConfig(
            filename=os.path.join(base_dir, "crawler.log"),
            level=logging.ERROR,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )

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
