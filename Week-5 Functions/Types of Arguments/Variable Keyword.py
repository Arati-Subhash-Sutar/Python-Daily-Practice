# 1. Print Student Profile Details
def print_profile(**kwargs):
    print("--- Student Profile ---")
    for k, v in kwargs.items():
        print(f"{k}: {v}")

print_profile(name="Arati", course="Data Analytics", year=2026, city="Sangli")


# 2. Configure Database Connection Settings
def db_config(**kwargs):
    print("--- Database Config ---")
    for k, v in kwargs.items():
        print(f"{k} = {v}")

db_config(host="localhost", user="root", pass_key="secret123", port=3306)


# 3. Product Specification Formatter
def show_specs(**kwargs):
    print("--- Product Specifications ---")
    for k, v in kwargs.items():
        print(f"{k.capitalize()}: {v}")

show_specs(brand="Dell", processor="i5", ram="16GB", storage="512GB SSD")


# 4. System Event Logger
def log_event(**kwargs):
    print("--- Log Entry ---")
    for k, v in kwargs.items():
        print(f"[{k.upper()}]: {v}")

log_event(level="info", module="auth", message="User logged in successfully")


# 5. HTML Tag Generator
def make_html_tag(tag, **kwargs):
    attrs = " ".join(f'{k}="{v}"' for k, v in kwargs.items())
    print(f"<{tag} {attrs}>Content</{tag}>")

make_html_tag("a", href="https://github.com", class_="btn", target="_blank")


# 6. Calculate Total Cart Price with Tax/Discount
def calc_total(base_price, **kwargs):
    total = base_price
    for k, v in kwargs.items():
        if k == "discount":
            total -= v
        elif k == "tax":
            total += v
    print(f"Final Amount: {total}")

calc_total(1000, discount=150, tax=50)


# 7. Employee Payroll Details
def print_payslip(emp_id, **kwargs):
    print(f"Payslip for ID: {emp_id}")
    total_pay = sum(kwargs.values())
    for k, v in kwargs.items():
        print(f"  {k}: {v}")
    print(f"Total Earnings: {total_pay}")

print_payslip(101, basic=25000, hra=5000, bonus=3000)


# 8. Filter and Count Keyword Arguments
def count_kwargs(**kwargs):
    print(f"Total keyword arguments passed: {len(kwargs)}")
    print(f"Keys: {list(kwargs.keys())}")

count_kwargs(x=10, y=20, z=30, active=True)


# 9. Dynamic Query Builder Simulator
def build_query(table, **kwargs):
    conditions = " AND ".join(f"{k} = '{v}'" for k, v in kwargs.items())
    print(f"SELECT * FROM {table} WHERE {conditions};")

build_query("students", city="Pune", status="Active", course="Python")


# 10. Update User Settings Dictionary
def update_settings(current, **kwargs):
    current.update(kwargs)
    print("Updated Settings:", current)

settings = {"theme": "dark", "notifications": True}
update_settings(settings, theme="light", sound=False)
