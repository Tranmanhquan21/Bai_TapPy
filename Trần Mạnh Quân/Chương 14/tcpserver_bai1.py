import socket


HOST = "127.0.0.1"
PORT = 8090


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"[SERVER] Listening on {HOST}:{PORT} ...")
        conn, addr = server.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            data = conn.recv(1024)
            if not data:
                print("[SERVER] No data received.")
                return

            msg = data.decode("utf-8", errors="replace")
            print(f"[SERVER] Received: {msg}")

            reply = "From SERVER TCP"
            conn.sendall(reply.encode("utf-8"))
            print(f"[SERVER] Sent: {reply}")


if __name__ == "__main__":
    main()
