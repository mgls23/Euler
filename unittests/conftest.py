"""Ensure repo root is importable in pytest."""
from __future__ import annotations

import sys
from pathlib import Path


def pytest_configure(config):
	"""Prepend repo root so tests can import solutions.*"""
	root = Path(__file__).resolve().parent
	root_str = str(root)
	if root_str not in sys.path:
		sys.path.insert(0, root_str)
