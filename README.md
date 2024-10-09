srapy for crawling
filtering url list
scrape to markdown
clean
rag

---

ulusofona_spider not to use -> tentativa de usar o scrapy logo para scrape mas nao estava muito bem formatado

ulusofona_url_spider.py -> usei esta spider para criar uma lista com todos os urls descoberstos e mandar para um ficheiro.

---

Issue no WSL por falta de browser

WSL environment: WSL doesn't natively support GUI applications, including browsers. This can cause issues with Selenium and ChromeDriver.
Chrome installation: Make sure Chrome is installed in your WSL environment. You can install it using:

```
sudo apt update
sudo apt install -y fonts-liberation libnspr4 libnss3 libvulkan1 xdg-utils
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt-get install -f
sudo apt --fix-broken install
sudo apt update && sudo apt upgrade -y
```

---

Issue disk space com o crlh 

I left my laptop (running Debian 12 with KDE) running a web scraping script using Selenium overnight. After several hours, the root partition completely filled up, causing my system to crash. I suspect it's due to temporary files, but I’m not sure exactly what’s causing it. The script works fine for shorter runs, like processing a few dozen URLs, but when it runs for a long time, storage gets exhausted. I need help figuring out what’s happening and how to prevent this storage issue during long script runs.

GPT Thoughts

The issue is likely related to the way Chrome and Selenium are handling temporary files, particularly with headless mode. Even though you added some arguments to disable caching (`--disk-cache-size=0`, `--disable-application-cache`), Chrome can still create temporary files in the `/tmp` or `/var/tmp` directories, which may fill up your root partition if left unchecked over a long period.

Here's what might be happening and some ways to address it:

1. **Selenium Temporary Files**:
   - Selenium can create temporary files for each browser session. When running continuously for a long time, these can accumulate, especially if the browser restarts every 50 URLs, as configured.
   - You might want to inspect `/tmp` or `/var/tmp` for any accumulated files (e.g., `chromedriver` logs or temporary user profiles created by Chrome).

2. **Chrome User Data Directory**:
   - Even with headless mode and caching disabled, Chrome still creates a temporary user data directory. You can explicitly set a directory to be used as the user data directory and clean it up manually after each session:
     ```python
     chrome_options.add_argument(f"--user-data-dir=/path/to/custom_temp")
     ```
     This way, you control where Chrome stores temporary data, and you can remove it as needed.

3. **Log File Size**:
   - If a lot of errors occur (e.g., retries for failed URLs), the log file (`scraping_log.txt`) might grow significantly. Ensure it’s not filling up your storage. You can set a maximum size for the log file by rotating logs using `logging.handlers.RotatingFileHandler`.

4. **Systemd Journal Logs**:
   - If your system uses `journald` and your script produces a lot of output, check if logs are growing under `/var/log/journal/`. You may need to clear them if they take up too much space.

5. **Monitoring Free Space**:
   - To monitor space usage during long runs, you could periodically check disk usage in the script. For example:
     ```python
     import shutil

     def check_disk_usage():
         total, used, free = shutil.disk_usage("/")
         print(f"Free space: {free // (2**30)} GB")

     check_disk_usage()
     ```

---

