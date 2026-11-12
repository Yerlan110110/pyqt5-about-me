#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = ["PyQt5==5.15.11"]
# ///

# ─── How to run ───
# 1. Install uv (if not installed):
#      curl -LsSf https://astral.sh/uv/install.sh | sh
# 2. Run directly (no venv, no pip install needed):
#      uv run app.py
# 3. Or make executable and run:
#      chmod +x app.py && ./app.py
# ──────────────────

"""A simple PyQt5 form with labels in Kazakh."""

from __future__ import annotations

import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication,
    QFormLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QWidget,
)


def build_window() -> QWidget:
    """Build the form and connect its button."""
    window = QWidget()
    window.setWindowTitle("Мен туралы ақпарат")
    window.resize(500, 300)

    form = QFormLayout(window)
    name_field = QLineEdit()
    group_field = QLineEdit()
    specialty_field = QLineEdit()

    form.addRow(QLabel("Аты-жөні"), name_field)
    form.addRow(QLabel("Тобы"), group_field)
    form.addRow(QLabel("Мамандығы"), specialty_field)

    button = QPushButton("Көрсету")
    result = QLabel()
    result.setTextFormat(Qt.TextFormat.PlainText)
    result.setWordWrap(True)
    form.addRow(button)
    form.addRow(result)

    def show_info() -> None:
        """Display the entered information or ask for missing fields."""
        name = name_field.text().strip()
        group = group_field.text().strip()
        specialty = specialty_field.text().strip()

        if not name or not group or not specialty:
            result.setText("Барлық өрісті толтырыңыз.")
            return

        result.setText(f"Аты-жөні: {name}\nТобы: {group}\nМамандығы: {specialty}")

    button.clicked.connect(show_info)
    return window


def main() -> None:
    """Show the window and run the Qt event loop."""
    app = QApplication(sys.argv)
    window = build_window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
