import socket
import threading


HOST = "0.0.0.0"
PORT = 8093


def recv_loop(conn: socket.socket) -> None:
    while True:
        data = conn.recv(4096)
        if not data:
            print("[SERVER] Client disconnected.")
            break
        msg = data.decode("utf-8", errors="replace")
        print(f"[CLIENT] {msg}")


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"[SERVER] Listening on {HOST}:{PORT} ...")
        conn, addr = server.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")

            t = threading.Thread(target=recv_loop, args=(conn,), daemon=True)
            t.start()

            while True:
                try:
                    text = input("[YOU] ")
                except (EOFError, KeyboardInterrupt):
                    print("\n[SERVER] Closing...")
                    break
                if not text:
                    continue
                try:
                    conn.sendall(text.encode("utf-8"))
                except OSError:
                    print("[SERVER] Send failed. Client may have disconnected.")
                    break


if __name__ == "__main__":
    main()
