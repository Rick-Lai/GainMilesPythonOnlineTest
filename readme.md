command
===
py app.py  
進入 http://127.0.0.1:5000/item  

建立Docker
===
如果有執行 py init_db.py 或 items.db 已存在  
需先刪除items.db再執行 docker-compose up  
如果docker網頁無法連線:  
ctrl+c 停止 docker  
docker run -p 5000:5000 test-test  