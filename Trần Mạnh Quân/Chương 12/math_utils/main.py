try:
    # Chay duoc khi goi: python -m math_utils.main
    from math_utils import (
        chia_ps,
        chu_vi_hinh_chu_nhat,
        chu_vi_hinh_tron,
        cong_ps,
        dien_tich_hinh_chu_nhat,
        dien_tich_hinh_tron,
        nhan_ps,
        tru_ps,
    )
except ModuleNotFoundError:
    # Chay duoc khi goi truc tiep file main.py ben trong thu muc math_utils
    from hinhhoc import (
        chu_vi_hinh_chu_nhat,
        chu_vi_hinh_tron,
        dien_tich_hinh_chu_nhat,
        dien_tich_hinh_tron,
    )
    from phanso import chia_ps, cong_ps, nhan_ps, tru_ps


def dinh_dang_phan_so(ps: tuple[int, int]) -> str:
    tu_so, mau_so = ps
    return f"{tu_so}/{mau_so}"


def main() -> None:
    # Demo phep toan phan so
    ps1 = (1, 2)
    ps2 = (3, 4)

    print("=== PHEP TOAN PHAN SO ===")
    print(f"{ps1[0]}/{ps1[1]} + {ps2[0]}/{ps2[1]} = {dinh_dang_phan_so(cong_ps(*ps1, *ps2))}")
    print(f"{ps1[0]}/{ps1[1]} - {ps2[0]}/{ps2[1]} = {dinh_dang_phan_so(tru_ps(*ps1, *ps2))}")
    print(f"{ps1[0]}/{ps1[1]} * {ps2[0]}/{ps2[1]} = {dinh_dang_phan_so(nhan_ps(*ps1, *ps2))}")
    print(f"{ps1[0]}/{ps1[1]} / {ps2[0]}/{ps2[1]} = {dinh_dang_phan_so(chia_ps(*ps1, *ps2))}")

    # Demo hinh hoc
    ban_kinh = 5
    chieu_dai, chieu_rong = 8, 3

    print("\n=== HINH HOC ===")
    print(f"Chu vi hinh tron (r={ban_kinh}): {chu_vi_hinh_tron(ban_kinh):.2f}")
    print(f"Dien tich hinh tron (r={ban_kinh}): {dien_tich_hinh_tron(ban_kinh):.2f}")
    print(f"Chu vi hinh chu nhat ({chieu_dai} x {chieu_rong}): {chu_vi_hinh_chu_nhat(chieu_dai, chieu_rong):.2f}")
    print(f"Dien tich hinh chu nhat ({chieu_dai} x {chieu_rong}): {dien_tich_hinh_chu_nhat(chieu_dai, chieu_rong):.2f}")


if __name__ == "__main__":
    main()
