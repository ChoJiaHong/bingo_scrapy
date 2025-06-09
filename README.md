# bingo_scrapy

## Setup

Install dependencies with:

```bash
pip install -r requirements.txt
```

`requirements.txt` includes `scrapy`, `python-dotenv`, `pymssql`, `pymongo` and
`requests`.

The crawler reads environment variables from `.env` in the `bingo_scrapy` directory, so make sure this file is available.

## Packaging

`run_crawler.py` can be packaged with PyInstaller. The included `run_crawler.spec` expects `.env` to be packaged as well. To build:

```bash
pyinstaller run_crawler.spec
```

## Running via Task Scheduler

`run_crawler.py` now changes the working directory to the location of the executable at startup. This avoids errors when the process is started from another directory, such as when using Windows Task Scheduler.
The log file `crawler.log` is also created in this directory.
