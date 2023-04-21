import sqlite3 as sq


def read_start_parameters_from_db(session_settings: dict, version: str):
    with sq.connect("./db/window.db") as db_window:
        cur = db_window.cursor()
        for parameter in session_settings:
            cur.execute(f"SELECT {parameter} FROM start_parameters WHERE name == '{version}'")
            session_settings[parameter] = cur.fetchall()[0][0]


def write_exit_parameters_in_db(settings: dict, version: str):
    with sq.connect("./db/window.db") as db_window:
        for parameter in settings:
            cur = db_window.cursor()
            cur.execute(f"UPDATE start_parameters SET {parameter} ='{settings[parameter]}' WHERE name == '{version}'")
