import tkinter as tk
from tkinter import ttk, messagebox
import pyodbc

# CẤU HÌNH KẾT NỐI SQL SERVER
# Đã cập nhật SERVER theo máy của bạn: QUANTRAN161204\SQLEXPRESS
CONN_STR = (
    "DRIVER={SQL Server};"
    "SERVER=QUANTRAN161204\\SQLEXPRESS;"
    "DATABASE=StoreDB;"
    "Trusted_Connection=yes;"
)

class StoreApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ Thống Quản Lý Bán Hàng")
        self.root.geometry("1000x700")
        
        # Style
        style = ttk.Style()
        style.configure("Treeview", rowheight=25)
        
        # Main Tab Control
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=1, fill="both")
        
        # Tabs
        self.tab_items = ttk.Frame(self.notebook)
        self.tab_customers = ttk.Frame(self.notebook)
        self.tab_orders = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_items, text="Quản Lý Mặt Hàng")
        self.notebook.add(self.tab_customers, text="Quản Lý Khách Hàng")
        self.notebook.add(self.tab_orders, text="Quản Lý Đơn Hàng")
        
        self.setup_items_tab()
        self.setup_customers_tab()
        self.setup_orders_tab()
        
    def get_connection(self):
        try:
            return pyodbc.connect(CONN_STR)
        except Exception as e:
            messagebox.showerror("Lỗi kết nối", f"Không thể kết nối SQL Server:\n{e}")
            return None

    # --- TAB MẶT HÀNG ---
    def setup_items_tab(self):
        # Form
        frame_form = ttk.LabelFrame(self.tab_items, text="Thông tin mặt hàng")
        frame_form.pack(side="top", fill="x", padx=10, pady=5)
        
        labels = ["Mã hàng:", "Tên hàng:", "Nguồn gốc:", "Đơn giá:"]
        self.item_vars = {label: tk.StringVar() for label in labels}
        
        for i, label in enumerate(labels):
            ttk.Label(frame_form, text=label).grid(row=i//2, column=(i%2)*2, padx=5, pady=5, sticky="w")
            ttk.Entry(frame_form, textvariable=self.item_vars[label]).grid(row=i//2, column=(i%2)*2+1, padx=5, pady=5, sticky="ew")
        
        # Buttons
        frame_btns = ttk.Frame(self.tab_items)
        frame_btns.pack(side="top", fill="x", padx=10)
        
        ttk.Button(frame_btns, text="Thêm", command=self.add_item).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Sửa", command=self.edit_item).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Xóa", command=self.delete_item).pack(side="left", padx=5)
        
        # Search
        ttk.Label(frame_btns, text="Tìm kiếm:").pack(side="left", padx=(20, 5))
        self.item_search_var = tk.StringVar()
        ttk.Entry(frame_btns, textvariable=self.item_search_var).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Tìm", command=self.search_items).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Làm mới", command=self.load_items).pack(side="left", padx=5)
        
        # Table
        self.tree_items = ttk.Treeview(self.tab_items, columns=("Ma", "Ten", "NguonGoc", "Gia"), show="headings")
        self.tree_items.heading("Ma", text="Mã Hàng")
        self.tree_items.heading("Ten", text="Tên Hàng")
        self.tree_items.heading("NguonGoc", text="Nguồn Gốc")
        self.tree_items.heading("Gia", text="Đơn Giá")
        self.tree_items.pack(expand=1, fill="both", padx=10, pady=10)
        self.tree_items.bind("<<TreeviewSelect>>", self.on_item_select)
        
        self.load_items()

    def load_items(self, query="SELECT * FROM MatHang"):
        self.tree_items.delete(*self.tree_items.get_children())
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                self.tree_items.insert("", "end", values=tuple(row))
            conn.close()

    def on_item_select(self, event):
        selected = self.tree_items.focus()
        if selected:
            values = self.tree_items.item(selected, "values")
            self.item_vars["Mã hàng:"].set(values[0])
            self.item_vars["Tên hàng:"].set(values[1])
            self.item_vars["Nguồn gốc:"].set(values[2])
            self.item_vars["Đơn giá:"].set(values[3])

    def add_item(self):
        ma = self.item_vars["Mã hàng:"].get()
        ten = self.item_vars["Tên hàng:"].get()
        nguon = self.item_vars["Nguồn gốc:"].get()
        gia = self.item_vars["Đơn giá:"].get()
        
        conn = self.get_connection()
        if conn:
            try:
                conn.execute("INSERT INTO MatHang VALUES (?, ?, ?, ?)", (ma, ten, nguon, gia))
                conn.commit()
                messagebox.showinfo("Thành công", "Đã thêm mặt hàng!")
                self.load_items()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể thêm: {e}")
            finally: conn.close()

    def edit_item(self):
        ma = self.item_vars["Mã hàng:"].get()
        ten = self.item_vars["Tên hàng:"].get()
        nguon = self.item_vars["Nguồn gốc:"].get()
        gia = self.item_vars["Đơn giá:"].get()
        
        conn = self.get_connection()
        if conn:
            try:
                conn.execute("UPDATE MatHang SET TenHang=?, NguonGoc=?, DonGia=? WHERE MaHang=?", (ten, nguon, gia, ma))
                conn.commit()
                messagebox.showinfo("Thành công", "Đã cập nhật mặt hàng!")
                self.load_items()
            except Exception as e:
                messagebox.showerror("Lỗi", f"Không thể sửa: {e}")
            finally: conn.close()

    def delete_item(self):
        ma = self.item_vars["Mã hàng:"].get()
        if messagebox.askyesno("Xác nhận", f"Bạn có chắc muốn xóa mã {ma}?"):
            conn = self.get_connection()
            if conn:
                conn.execute("DELETE FROM MatHang WHERE MaHang=?", (ma,))
                conn.commit()
                self.load_items()
                conn.close()

    def search_items(self):
        val = f"%{self.item_search_var.get()}%"
        query = f"SELECT * FROM MatHang WHERE MaHang LIKE '{val}' OR TenHang LIKE N'{val}' OR NguonGoc LIKE N'{val}'"
        self.load_items(query)

    # --- TAB KHÁCH HÀNG ---
    def setup_customers_tab(self):
        frame_form = ttk.LabelFrame(self.tab_customers, text="Thông tin khách hàng")
        frame_form.pack(side="top", fill="x", padx=10, pady=5)
        
        labels = ["Mã KH:", "Tên KH:", "Địa chỉ:", "SĐT:"]
        self.cust_vars = {label: tk.StringVar() for label in labels}
        
        for i, label in enumerate(labels):
            ttk.Label(frame_form, text=label).grid(row=i//2, column=(i%2)*2, padx=5, pady=5, sticky="w")
            ttk.Entry(frame_form, textvariable=self.cust_vars[label]).grid(row=i//2, column=(i%2)*2+1, padx=5, pady=5, sticky="ew")
            
        frame_btns = ttk.Frame(self.tab_customers)
        frame_btns.pack(side="top", fill="x", padx=10)
        
        ttk.Button(frame_btns, text="Thêm", command=self.add_customer).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Sửa", command=self.edit_customer).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Xóa", command=self.delete_customer).pack(side="left", padx=5)
        
        ttk.Label(frame_btns, text="Tìm kiếm:").pack(side="left", padx=(20, 5))
        self.cust_search_var = tk.StringVar()
        ttk.Entry(frame_btns, textvariable=self.cust_search_var).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Tìm", command=self.search_customers).pack(side="left", padx=5)
        ttk.Button(frame_btns, text="Làm mới", command=self.load_customers).pack(side="left", padx=5)

        self.tree_custs = ttk.Treeview(self.tab_customers, columns=("Ma", "Ten", "DiaChi", "SDT"), show="headings")
        self.tree_custs.heading("Ma", text="Mã KH")
        self.tree_custs.heading("Ten", text="Tên KH")
        self.tree_custs.heading("DiaChi", text="Địa chỉ")
        self.tree_custs.heading("SDT", text="Số điện thoại")
        self.tree_custs.pack(expand=1, fill="both", padx=10, pady=10)
        self.tree_custs.bind("<<TreeviewSelect>>", self.on_cust_select)
        
        self.load_customers()

    def load_customers(self, query="SELECT * FROM KhachHang"):
        self.tree_custs.delete(*self.tree_custs.get_children())
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                self.tree_custs.insert("", "end", values=tuple(row))
            conn.close()

    def on_cust_select(self, event):
        selected = self.tree_custs.focus()
        if selected:
            values = self.tree_custs.item(selected, "values")
            self.cust_vars["Mã KH:"].set(values[0])
            self.cust_vars["Tên KH:"].set(values[1])
            self.cust_vars["Địa chỉ:"].set(values[2])
            self.cust_vars["SĐT:"].set(values[3])

    def add_customer(self):
        ma, ten, dc, sdt = [self.cust_vars[l].get() for l in ["Mã KH:", "Tên KH:", "Địa chỉ:", "SĐT:"]]
        conn = self.get_connection()
        if conn:
            try:
                conn.execute("INSERT INTO KhachHang VALUES (?, ?, ?, ?)", (ma, ten, dc, sdt))
                conn.commit()
                self.load_customers()
            except Exception as e: messagebox.showerror("Lỗi", e)
            finally: conn.close()

    def edit_customer(self):
        ma, ten, dc, sdt = [self.cust_vars[l].get() for l in ["Mã KH:", "Tên KH:", "Địa chỉ:", "SĐT:"]]
        conn = self.get_connection()
        if conn:
            try:
                conn.execute("UPDATE KhachHang SET TenKH=?, DiaChi=?, SoDienThoai=? WHERE MaKH=?", (ten, dc, sdt, ma))
                conn.commit()
                self.load_customers()
            except Exception as e: messagebox.showerror("Lỗi", e)
            finally: conn.close()

    def delete_customer(self):
        ma = self.cust_vars["Mã KH:"].get()
        if messagebox.askyesno("Xác nhận", f"Xóa khách hàng {ma}?"):
            conn = self.get_connection()
            if conn:
                conn.execute("DELETE FROM KhachHang WHERE MaKH=?", (ma,))
                conn.commit()
                self.load_customers()
                conn.close()

    def search_customers(self):
        val = f"%{self.cust_search_var.get()}%"
        query = f"SELECT * FROM KhachHang WHERE MaKH LIKE '{val}' OR TenKH LIKE N'{val}' OR DiaChi LIKE N'{val}' OR SoDienThoai LIKE '{val}'"
        self.load_customers(query)

    # --- TAB ĐƠN HÀNG ---
    def setup_orders_tab(self):
        # Top: List of Invoices
        frame_top = ttk.LabelFrame(self.tab_orders, text="Danh sách hóa đơn")
        frame_top.pack(side="top", fill="both", expand=True, padx=10, pady=5)
        
        # Search bar for orders
        frame_search = ttk.Frame(frame_top)
        frame_search.pack(side="top", fill="x", padx=5, pady=5)
        ttk.Label(frame_search, text="Tìm (Mã HD/Mã KH):").pack(side="left")
        self.order_search_var = tk.StringVar()
        ttk.Entry(frame_search, textvariable=self.order_search_var).pack(side="left", padx=5)
        ttk.Button(frame_search, text="Tìm", command=self.search_orders).pack(side="left", padx=5)
        ttk.Button(frame_search, text="Làm mới", command=self.load_orders).pack(side="left", padx=5)

        self.tree_orders = ttk.Treeview(frame_top, columns=("MaHD", "MaKH", "TenKH", "Ngay", "TongTien"), show="headings")
        self.tree_orders.heading("MaHD", text="Mã HD")
        self.tree_orders.heading("MaKH", text="Mã KH")
        self.tree_orders.heading("TenKH", text="Tên Khách Hàng")
        self.tree_orders.heading("Ngay", text="Ngày Lập")
        self.tree_orders.heading("TongTien", text="Tổng Tiền")
        self.tree_orders.pack(expand=1, fill="both", padx=5, pady=5)
        self.tree_orders.bind("<<TreeviewSelect>>", self.on_order_select)
        
        # Bottom: Detail of selected invoice
        frame_bottom = ttk.LabelFrame(self.tab_orders, text="Chi tiết hóa đơn đang chọn")
        frame_bottom.pack(side="bottom", fill="both", expand=True, padx=10, pady=5)
        
        self.tree_details = ttk.Treeview(frame_bottom, columns=("TenHang", "SL", "DonGia", "ThanhTien"), show="headings")
        self.tree_details.heading("TenHang", text="Tên Mặt Hàng")
        self.tree_details.heading("SL", text="Số Lượng")
        self.tree_details.heading("DonGia", text="Đơn Giá")
        self.tree_details.heading("ThanhTien", text="Thành Tiền")
        self.tree_details.pack(expand=1, fill="both", padx=5, pady=5)
        
        self.load_orders()

    def load_orders(self, where_clause=""):
        self.tree_orders.delete(*self.tree_orders.get_children())
        query = f"""
            SELECT HD.MaHD, HD.MaKH, KH.TenKH, HD.NgayLap, 
                   COALESCE(SUM(CT.SoLuong * MH.DonGia), 0) as TongTien
            FROM HoaDon HD
            LEFT JOIN KhachHang KH ON HD.MaKH = KH.MaKH
            LEFT JOIN ChiTietHoaDon CT ON HD.MaHD = CT.MaHD
            LEFT JOIN MatHang MH ON CT.MaHang = MH.MaHang
            {where_clause}
            GROUP BY HD.MaHD, HD.MaKH, KH.TenKH, HD.NgayLap
        """
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(query)
            for row in cursor.fetchall():
                # Format currency for total money
                formatted_row = list(row)
                formatted_row[4] = f"{row[4]:,.0f} VNĐ"
                self.tree_orders.insert("", "end", values=tuple(formatted_row))
            conn.close()

    def on_order_select(self, event):
        selected = self.tree_orders.focus()
        if not selected: return
        
        ma_hd = self.tree_orders.item(selected, "values")[0]
        self.tree_details.delete(*self.tree_details.get_children())
        
        query = """
            SELECT MH.TenHang, CT.SoLuong, MH.DonGia, (CT.SoLuong * MH.DonGia) as ThanhTien
            FROM ChiTietHoaDon CT
            JOIN MatHang MH ON CT.MaHang = MH.MaHang
            WHERE CT.MaHD = ?
        """
        conn = self.get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute(query, (ma_hd,))
            for row in cursor.fetchall():
                formatted_row = list(row)
                formatted_row[2] = f"{row[2]:,.0f}"
                formatted_row[3] = f"{row[3]:,.0f}"
                self.tree_details.insert("", "end", values=tuple(formatted_row))
            conn.close()

    def search_orders(self):
        val = f"%{self.order_search_var.get()}%"
        where = f"WHERE HD.MaHD LIKE '{val}' OR HD.MaKH LIKE '{val}'"
        self.load_orders(where)

if __name__ == "__main__":
    root = tk.Tk()
    app = StoreApp(root)
    root.mainloop()
