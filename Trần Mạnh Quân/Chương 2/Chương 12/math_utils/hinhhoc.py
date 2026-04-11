"""Cac ham tinh chu vi va dien tich hinh hoc co ban."""

from __future__ import annotations

from math import pi


def chu_vi_hinh_tron(ban_kinh: float) -> float:
    """Tinh chu vi hinh tron."""
    if ban_kinh < 0:
        raise ValueError("Ban kinh khong duoc am")
    return 2 * pi * ban_kinh


def dien_tich_hinh_tron(ban_kinh: float) -> float:
    """Tinh dien tich hinh tron."""
    if ban_kinh < 0:
        raise ValueError("Ban kinh khong duoc am")
    return pi * ban_kinh**2


def chu_vi_hinh_chu_nhat(chieu_dai: float, chieu_rong: float) -> float:
    """Tinh chu vi hinh chu nhat."""
    if chieu_dai < 0 or chieu_rong < 0:
        raise ValueError("Kich thuoc khong duoc am")
    return 2 * (chieu_dai + chieu_rong)


def dien_tich_hinh_chu_nhat(chieu_dai: float, chieu_rong: float) -> float:
    """Tinh dien tich hinh chu nhat."""
    if chieu_dai < 0 or chieu_rong < 0:
        raise ValueError("Kich thuoc khong duoc am")
    return chieu_dai * chieu_rong
