import socket


HOST = "127.0.0.1"
PORT = 8092


def is_valid_password(pw: str) -> bool:
    if not (6 <= len(pw) <= 12):
        return False
    has_lower = any("a" <= ch <= "z" for ch in pw)
    has_upper = any("A" <= ch <= "Z" for ch in pw)
    has_digit = any("0" <= ch <= "9" for ch in pw)
    has_special = any(ch in "$#@" for ch in pw)
    return has_lower and has_upper and has_digit and has_special


def filter_passwords(text: str) -> str:
    items = [part.strip() for part in text.split(",")]
    valid = [pw for pw in items if pw and is_valid_password(pw)]
    return ",".join(valid)


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f"[SERVER] Listening on {HOST}:{PORT} ...")
        conn, addr = server.accept()
        with conn:
            print(f"[SERVER] Connected by {addr}")
            data = conn.recv(4096)
            if not data:
                print("[SERVER] No data received.")
                return

            raw = data.decode("utf-8", errors="replace")
            print(f"[SERVER] Received raw: {raw!r}")

            result = filter_passwords(raw)
            conn.sendall(result.encode("utf-8"))
            print(f"[SERVER] Sent: {result!r}")


if __name__ == "__main__":
    main()
