import os
import pandas as pd
import matplotlib.pyplot as plt


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "sales-data-sample.csv")


def main() -> None:
    df = pd.read_csv(CSV_PATH)

    df["OrderDate"] = pd.to_datetime(df["OrderDate"], errors="coerce")
    df = df.dropna(subset=["OrderDate"])

    revenue_col = "Sales"

    df["Year"] = df["OrderDate"].dt.year
    df["Month"] = df["OrderDate"].dt.month
    df["Quarter"] = df["OrderDate"].dt.to_period("Q").astype(str)

    revenue_by_month = (
        df.groupby(["Year", "Month"], as_index=False)[revenue_col].sum()
        .sort_values(["Year", "Month"])
    )
    revenue_by_year = df.groupby("Year", as_index=False)[revenue_col].sum().sort_values("Year")
    revenue_by_quarter = (
        df.groupby("Quarter", as_index=False)[revenue_col].sum()
        .sort_values("Quarter")
    )
    revenue_by_item = (
        df.groupby("Sub_Category", as_index=False)[revenue_col].sum()
        .sort_values(revenue_col, ascending=False)
    )

    plt.figure(figsize=(10, 5))
    x_labels = revenue_by_month.apply(
        lambda r: f"{int(r['Year'])}-{int(r['Month']):02d}", axis=1
    )
    plt.plot(x_labels, revenue_by_month[revenue_col], marker="o")
    plt.title("Doanh thu theo thang")
    plt.xlabel("Thang")
    plt.ylabel("Doanh thu")
    plt.xticks(rotation=60, ha="right")
    plt.tight_layout()
    plt.savefig("revenue_by_month.png", dpi=120)

    plt.figure(figsize=(8, 5))
    plt.bar(revenue_by_year["Year"].astype(str), revenue_by_year[revenue_col])
    plt.title("Doanh thu theo nam")
    plt.xlabel("Nam")
    plt.ylabel("Doanh thu")
    plt.tight_layout()
    plt.savefig("revenue_by_year.png", dpi=120)

    plt.figure(figsize=(10, 5))
    plt.plot(revenue_by_quarter["Quarter"], revenue_by_quarter[revenue_col], marker="o")
    plt.title("Doanh thu theo quy")
    plt.xlabel("Quy")
    plt.ylabel("Doanh thu")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("revenue_by_quarter.png", dpi=120)

    plt.figure(figsize=(10, 6))
    plt.barh(revenue_by_item["Sub_Category"], revenue_by_item[revenue_col])
    plt.title("Doanh thu theo loai mat hang")
    plt.xlabel("Doanh thu")
    plt.ylabel("Loai mat hang")
    plt.tight_layout()
    plt.savefig("revenue_by_item_type.png", dpi=120)

    plt.show()


if __name__ == "__main__":
    main()
