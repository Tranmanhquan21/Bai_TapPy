import socket


HOST = "127.0.0.1"
PORT = 8091


def main() -> None:
    a = input("Nhap so nguyen a: ").strip()
    b = input("Nhap so nguyen b: ").strip()

    payload = f"{a} {b}"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(payload.encode("utf-8"))
        print(f"[CLIENT] Sent: {payload}")

        data = client.recv(1024)
        if not data:
            print("[CLIENT] No reply received.")
            return

        reply = data.decode("utf-8", errors="replace")
        print(f"[CLIENT] Received: {reply}")


if __name__ == "__main__":
    main()
