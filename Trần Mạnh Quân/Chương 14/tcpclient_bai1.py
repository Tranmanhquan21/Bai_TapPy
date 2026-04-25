import socket


HOST = "127.0.0.1"
PORT = 8090


def main() -> None:
    message = "From CLIENT TCP"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(message.encode("utf-8"))
        print(f"[CLIENT] Sent: {message}")

        data = client.recv(1024)
        if not data:
            print("[CLIENT] No reply received.")
            return

        reply = data.decode("utf-8", errors="replace")
        print(f"[CLIENT] Received: {reply}")


if __name__ == "__main__":
    main()
