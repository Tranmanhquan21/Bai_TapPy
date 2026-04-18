"""Cac ham tinh toan phan so co rut gon ket qua."""

from __future__ import annotations

from math import gcd


def _rut_gon(tu_so: int, mau_so: int) -> tuple[int, int]:
    """Rut gon phan so va chuan hoa dau mau so."""
    if mau_so == 0:
        raise ZeroDivisionError("Mau so khong duoc bang 0")

    ucln = gcd(tu_so, mau_so)
    tu_so //= ucln
    mau_so //= ucln

    if mau_so < 0:
        tu_so *= -1
        mau_so *= -1

    return tu_so, mau_so


def cong_ps(tu1: int, mau1: int, tu2: int, mau2: int) -> tuple[int, int]:
    """Cong hai phan so va tra ve phan so da rut gon."""
    return _rut_gon(tu1 * mau2 + tu2 * mau1, mau1 * mau2)


def tru_ps(tu1: int, mau1: int, tu2: int, mau2: int) -> tuple[int, int]:
    """Tru hai phan so va tra ve phan so da rut gon."""
    return _rut_gon(tu1 * mau2 - tu2 * mau1, mau1 * mau2)


def nhan_ps(tu1: int, mau1: int, tu2: int, mau2: int) -> tuple[int, int]:
    """Nhan hai phan so va tra ve phan so da rut gon."""
    return _rut_gon(tu1 * tu2, mau1 * mau2)


def chia_ps(tu1: int, mau1: int, tu2: int, mau2: int) -> tuple[int, int]:
    """Chia hai phan so va tra ve phan so da rut gon."""
    if tu2 == 0:
        raise ZeroDivisionError("Khong the chia cho phan so co tu so bang 0")
    return _rut_gon(tu1 * mau2, mau1 * tu2)
