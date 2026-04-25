# Chương 14 - TCP Socket (Bài 1 & Bài 2)

## Yêu cầu

- **Bài 1**: Kết nối TCP qua port **8090**. Client gửi `From CLIENT TCP`, server nhận và trả về `From SERVER TCP`. In ra thông điệp ở cả server và client.
- **Bài 2**: Kết nối TCP qua port **8091**. Client gửi 2 số nguyên `a b`, server tính `a + b` và trả kết quả về client.

## Cách chạy (Windows / PowerShell)

Mở **2 terminal** trong VS Code.

### Bài 1 (port 8090)

Terminal 1 (server):

```powershell
python .\tcpserver_bai1.py
```

Terminal 2 (client):

```powershell
python .\tcpclient_bai1.py
```

### Bài 2 (port 8091)

Terminal 1 (server):

```powershell
python .\tcpserver_bai2.py
```

Terminal 2 (client):

```powershell
python .\tcpclient_bai2.py
```

## Ghi chú

- Server đang thiết kế để nhận **1 kết nối** rồi kết thúc (đúng dạng bài tập cơ bản).
- Nếu port bị chiếm, hãy tắt chương trình đang dùng port đó hoặc đổi `PORT` trong file.
