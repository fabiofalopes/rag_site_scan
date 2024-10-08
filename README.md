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
