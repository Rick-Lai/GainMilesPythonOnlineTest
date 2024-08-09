# 使用官方 Python 映像作為基礎映像
FROM python:3.11.7

# 設定工作目錄
WORKDIR /app

# 複製當前目錄內容到工作目錄
COPY . /app

# 安裝 Python 依賴包
RUN pip install Flask

# 初始化資料庫
RUN python init_db.py

# 暴露應用程序運行的端口
EXPOSE 5000

# 執行 Flask 應用程序
CMD ["python", "app.py"]
