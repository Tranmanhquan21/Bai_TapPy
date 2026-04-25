import socket
import threading
import tkinter as tk
from tkinter import ttk


HOST = "127.0.0.1"
PORT = 8093


class ChatClient:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("TCP Chat Client")

        self.text = tk.Text(root, height=18, width=60, state="disabled", wrap="word")
        self.text.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.entry = ttk.Entry(root)
        self.entry.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="ew")
        self.entry.bind("<Return>", self.send_message)

        self.send_btn = ttk.Button(root, text="Send", command=self.send_message)
        self.send_btn.grid(row=1, column=1, padx=(0, 10), pady=(0, 10))

        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((HOST, PORT))

        self.recv_thread = threading.Thread(target=self.recv_loop, daemon=True)
        self.recv_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

    def append_message(self, msg: str) -> None:
        self.text.configure(state="normal")
        self.text.insert("end", msg + "\n")
        self.text.see("end")
        self.text.configure(state="disabled")

    def recv_loop(self) -> None:
        while True:
            try:
                data = self.sock.recv(4096)
            except OSError:
                break
            if not data:
                self.root.after(0, self.append_message, "[SYSTEM] Server disconnected.")
                break
            msg = data.decode("utf-8", errors="replace")
            self.root.after(0, self.append_message, f"[SERVER] {msg}")

    def send_message(self, event=None) -> None:
        msg = self.entry.get().strip()
        if not msg:
            return
        try:
            self.sock.sendall(msg.encode("utf-8"))
        except OSError:
            self.append_message("[SYSTEM] Send failed.")
            return
        self.append_message(f"[YOU] {msg}")
        self.entry.delete(0, "end")

    def on_close(self) -> None:
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            pass
        self.sock.close()
        self.root.destroy()


def main() -> None:
    root = tk.Tk()
    ChatClient(root)
    root.mainloop()


if __name__ == "__main__":
    main()
