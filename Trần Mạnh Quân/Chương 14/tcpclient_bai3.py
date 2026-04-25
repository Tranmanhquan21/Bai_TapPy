import socket


HOST = "127.0.0.1"
PORT = 8092


def main() -> None:
    text = input("Nhap chuoi mat khau (cach nhau boi dau phay): ").strip()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(text.encode("utf-8"))
        print(f"[CLIENT] Sent: {text}")

        data = client.recv(4096)
        if not data:
            print("[CLIENT] No reply received.")
            return

        reply = data.decode("utf-8", errors="replace")
        if reply:
            print(f"Mat khau hop le: {reply}")
        else:
            print("Khong co mat khau hop le.")


if __name__ == "__main__":
    main()
