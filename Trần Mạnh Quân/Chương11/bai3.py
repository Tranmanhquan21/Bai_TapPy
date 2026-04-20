import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).with_name("employee_department.db")


MY_DEPARTMENT = {
	"deptno": 50,
	"dname": "IT_SUPPORT",
	"loc": "HA NOI",
}

MY_EMPLOYEE = {
	"empno": 9001,
	"ename": "TRAN MANH QUAN",
	"job": "STUDENT",
	"mgr": 7839,
	"hiredate": "2026-04-20",
	"sal": 3500,
	"comm": None,
	"deptno": 50,
}


def input_with_default(prompt_text, default_value):
	text = input(f"{prompt_text} [{default_value}]: ").strip()
	if text == "":
		return default_value
	return text


def input_number_with_default(prompt_text, default_value):
	while True:
		text = input(f"{prompt_text} [{default_value}]: ").strip()
		if text == "":
			return default_value
		try:
			return int(text)
		except ValueError:
			print("Vui long nhap so nguyen hop le.")


def input_float_or_none_with_default(prompt_text, default_value):
	display_default = "None" if default_value is None else default_value
	while True:
		text = input(f"{prompt_text} [{display_default}] (nhap none neu de trong): ").strip()
		if text == "":
			return default_value
		if text.lower() == "none":
			return None
		try:
			return float(text)
		except ValueError:
			print("Vui long nhap so hop le hoac 'none'.")


def read_department_input(default_department):
	print("\nNhap thong tin department (nhan Enter de giu gia tri mac dinh):")
	return {
		"deptno": input_number_with_default("- Ma phong (deptno)", default_department["deptno"]),
		"dname": input_with_default("- Ten phong (dname)", default_department["dname"]),
		"loc": input_with_default("- Dia diem (loc)", default_department["loc"]),
	}


def read_employee_input(default_employee, default_deptno):
	print("\nNhap thong tin employee (nhan Enter de giu gia tri mac dinh):")
	return {
		"empno": input_number_with_default("- Ma nhan vien (empno)", default_employee["empno"]),
		"ename": input_with_default("- Ten nhan vien (ename)", default_employee["ename"]),
		"job": input_with_default("- Chuc vu (job)", default_employee["job"]),
		"mgr": input_number_with_default("- Ma quan ly (mgr)", default_employee["mgr"]),
		"hiredate": input_with_default("- Ngay vao lam YYYY-MM-DD (hiredate)", default_employee["hiredate"]),
		"sal": float(input_with_default("- Luong (sal)", default_employee["sal"])),
		"comm": input_float_or_none_with_default("- Hoa hong (comm)", default_employee["comm"]),
		"deptno": input_number_with_default("- Ma phong (deptno)", default_deptno),
	}


def get_connection():
	conn = sqlite3.connect(DB_PATH)
	conn.row_factory = sqlite3.Row
	conn.execute("PRAGMA foreign_keys = ON")
	return conn


def create_tables(conn):
	conn.execute(
		"""
		CREATE TABLE IF NOT EXISTS department (
			deptno INTEGER PRIMARY KEY,
			dname TEXT NOT NULL,
			loc TEXT NOT NULL
		)
		"""
	)

	conn.execute(
		"""
		CREATE TABLE IF NOT EXISTS employee (
			empno INTEGER PRIMARY KEY,
			ename TEXT NOT NULL,
			job TEXT NOT NULL,
			mgr INTEGER,
			hiredate TEXT NOT NULL,
			sal REAL NOT NULL,
			comm REAL,
			deptno INTEGER NOT NULL,
			FOREIGN KEY (deptno) REFERENCES department(deptno)
		)
		"""
	)
	conn.commit()


def seed_data(conn):
	departments = [
		(10, "ACCOUNTING", "NEW YORK"),
		(20, "RESEARCH", "DALLAS"),
		(30, "SALES", "CHICAGO"),
		(40, "OPERATIONS", "BOSTON"),
	]

	employees = [
		(7369, "SMITH", "CLERK", 7902, "1980-12-17", 800, None, 20),
		(7499, "ALLEN", "SALESMAN", 7698, "1981-02-20", 1600, 300, 30),
		(7521, "WARD", "SALESMAN", 7698, "1981-02-22", 1250, 500, 30),
		(7566, "JONES", "MANAGER", 7839, "1981-04-02", 2975, None, 20),
		(7654, "MARTIN", "SALESMAN", 7698, "1981-09-28", 1250, 1400, 30),
		(7698, "BLAKE", "MANAGER", 7839, "1981-05-01", 2850, None, 30),
		(7782, "CLARK", "MANAGER", 7839, "1981-06-09", 2450, None, 10),
		(7788, "SCOTT", "ANALYST", 7566, "1982-12-09", 3000, None, 20),
		(7839, "KING", "PRESIDENT", None, "1981-11-17", 5000, None, 10),
		(7844, "TURNER", "SALESMAN", 7698, "1981-09-08", 1500, 0, 30),
		(7876, "ADAMS", "CLERK", 7788, "1983-01-12", 1100, None, 20),
		(7900, "JAMES", "CLERK", 7698, "1981-12-03", 950, None, 30),
		(7902, "FORD", "ANALYST", 7566, "1981-12-03", 3000, None, 20),
		(7934, "MILLER", "CLERK", 7782, "1982-01-23", 1300, None, 10),
	]

	conn.executemany(
		"INSERT OR IGNORE INTO department(deptno, dname, loc) VALUES (?, ?, ?)",
		departments,
	)
	conn.executemany(
		"""
		INSERT OR IGNORE INTO employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
		VALUES (?, ?, ?, ?, ?, ?, ?, ?)
		""",
		employees,
	)
	conn.commit()


def print_rows(title, rows):
	print(f"\n{title}")
	if not rows:
		print("(khong co du lieu)")
		return

	for row in rows:
		print(dict(row))


def task_a_list_managers(conn):
	rows = conn.execute(
		"""
		SELECT empno, ename, job, deptno, sal
		FROM employee
		WHERE UPPER(job) = 'MANAGER'
		ORDER BY empno
		"""
	).fetchall()
	print_rows("A) Danh sach nhan vien co chuc vu MANAGER:", rows)


def task_b_insert_department(conn, my_department):
	conn.execute(
		"""
		INSERT OR REPLACE INTO department(deptno, dname, loc)
		VALUES (:deptno, :dname, :loc)
		""",
		my_department,
	)
	conn.commit()

	rows = conn.execute(
		"SELECT deptno, dname, loc FROM department WHERE deptno = :deptno",
		{"deptno": my_department["deptno"]},
	).fetchall()
	print_rows("B) Da them/cap nhat department cua ban:", rows)


def task_c_insert_employee(conn, my_employee):
	conn.execute(
		"""
		INSERT OR REPLACE INTO employee(empno, ename, job, mgr, hiredate, sal, comm, deptno)
		VALUES (:empno, :ename, :job, :mgr, :hiredate, :sal, :comm, :deptno)
		""",
		my_employee,
	)
	conn.commit()

	rows = conn.execute(
		"SELECT * FROM employee WHERE empno = :empno",
		{"empno": my_employee["empno"]},
	).fetchall()
	print_rows("C) Da them/cap nhat employee cua ban:", rows)


def task_d_update_clark(conn, my_employee):
	conn.execute(
		"""
		UPDATE employee
		SET ename = :ename,
			job = :job,
			mgr = :mgr,
			hiredate = :hiredate,
			sal = :sal,
			comm = :comm,
			deptno = :deptno
		WHERE UPPER(ename) = 'CLARK'
		""",
		my_employee,
	)
	conn.commit()

	rows = conn.execute(
		"SELECT * FROM employee WHERE empno = 7782"
	).fetchall()
	print_rows("D) Sau khi cap nhat nhan vien CLARK:", rows)


def task_e_delete_miller(conn):
	conn.execute("DELETE FROM employee WHERE UPPER(ename) = 'MILLER'")
	conn.commit()

	rows = conn.execute(
		"SELECT * FROM employee WHERE UPPER(ename) = 'MILLER'"
	).fetchall()
	print_rows("E) Sau khi xoa nhan vien MILLER:", rows)


def main():
	my_department = read_department_input(MY_DEPARTMENT)
	my_employee = read_employee_input(MY_EMPLOYEE, my_department["deptno"])

	conn = get_connection()
	try:
		create_tables(conn)
		seed_data(conn)

		task_a_list_managers(conn)
		task_b_insert_department(conn, my_department)
		task_c_insert_employee(conn, my_employee)
		task_d_update_clark(conn, my_employee)
		task_e_delete_miller(conn)
	finally:
		conn.close()


if __name__ == "__main__":
	main()
