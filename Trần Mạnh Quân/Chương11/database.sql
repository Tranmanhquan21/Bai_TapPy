-- Script tạo database và bảng cho Hệ thống quản lý bán hàng
-- Hệ quản trị cơ sở dữ liệu: SQL Server

CREATE DATABASE StoreDB;
GO

USE StoreDB;
GO

-- 1. Bảng Mặt hàng
CREATE TABLE MatHang (
    MaHang VARCHAR(10) PRIMARY KEY,
    TenHang NVARCHAR(100) NOT NULL,
    NguonGoc NVARCHAR(50),
    DonGia DECIMAL(18, 2) DEFAULT 0
);

-- 2. Bảng Khách hàng
CREATE TABLE KhachHang (
    MaKH VARCHAR(10) PRIMARY KEY,
    TenKH NVARCHAR(100) NOT NULL,
    DiaChi NVARCHAR(200),
    SoDienThoai VARCHAR(15)
);

-- 3. Bảng Hóa đơn
CREATE TABLE HoaDon (
    MaHD VARCHAR(10) PRIMARY KEY,
    MaKH VARCHAR(10),
    NgayLap DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (MaKH) REFERENCES KhachHang(MaKH) ON DELETE CASCADE
);

-- 4. Bảng Chi tiết Hóa đơn
CREATE TABLE ChiTietHoaDon (
    MaHD VARCHAR(10),
    MaHang VARCHAR(10),
    SoLuong INT DEFAULT 1,
    PRIMARY KEY (MaHD, MaHang),
    FOREIGN KEY (MaHD) REFERENCES HoaDon(MaHD) ON DELETE CASCADE,
    FOREIGN KEY (MaHang) REFERENCES MatHang(MaHang) ON DELETE CASCADE
);
GO

-- Chèn dữ liệu mẫu
INSERT INTO MatHang (MaHang, TenHang, NguonGoc, DonGia) VALUES
('MH01', N'Laptop Dell XPS', N'Mỹ', 25000000),
('MH02', N'iPhone 15 Pro', N'Trung Quốc', 30000000),
('MH03', N'Chuột Logitech G502', N'Thụy Sĩ', 1500000);

INSERT INTO KhachHang (MaKH, TenKH, DiaChi, SoDienThoai) VALUES
('KH01', N'Nguyễn Văn A', N'Hà Nội', '0912345678'),
('KH02', N'Trần Thị B', N'TP.HCM', '0987654321');

INSERT INTO HoaDon (MaHD, MaKH, NgayLap) VALUES
('HD01', 'KH01', '2024-03-20'),
('HD02', 'KH02', '2024-03-21');

INSERT INTO ChiTietHoaDon (MaHD, MaHang, SoLuong) VALUES
('HD01', 'MH01', 1),
('HD01', 'MH03', 2),
('HD02', 'MH02', 1);
GO

-- Query kiểm tra tổng tiền hóa đơn (yêu cầu trong bài)
-- SELECT HD.MaHD, KH.TenKH, HD.NgayLap, SUM(CT.SoLuong * MH.DonGia) AS TongTien
-- FROM HoaDon HD
-- JOIN KhachHang KH ON HD.MaKH = KH.MaKH
-- JOIN ChiTietHoaDon CT ON HD.MaHD = CT.MaHD
-- JOIN MatHang MH ON CT.MaHang = MH.MaHang
-- GROUP BY HD.MaHD, KH.TenKH, HD.NgayLap;
