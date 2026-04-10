class Formatters:
    @staticmethod
    def format_currency(amount):
        return f"{amount:,.0f} VNĐ"

    @staticmethod
    def format_header(title):
        line = "=" * 60
        return f"\n{line}\n{title.center(60)}\n{line}"
