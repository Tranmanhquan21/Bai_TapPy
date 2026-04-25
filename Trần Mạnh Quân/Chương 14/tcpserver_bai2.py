import socket


HOST = "127.0.0.1"
PORT = 8091


def parse_two_ints(text: str) -> tuple[int, int]:
    parts = text.strip().split()
    if len(parts) != 2:
        raise ValueError("Expected exactly 2 integers: 'a b'")
    return int(parts[0]), int(parts[1])


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

            raw = data.decode("utf-8", errors="replace")
            print(f"[SERVER] Received raw: {raw!r}")

            try:
                a, b = parse_two_ints(raw)
                total = a + b
                reply = str(total)
                conn.sendall(reply.encode("utf-8"))
                print(f"[SERVER] a={a}, b={b} -> sum={total}")
                print(f"[SERVER] Sent: {reply}")
            except Exception as exc:
                err = f"ERROR: {exc}"
                conn.sendall(err.encode("utf-8"))
                print(f"[SERVER] Sent error: {err}")


if __name__ == "__main__":
    main()
