"""Shared pytest configuration"""
from pathlib import Path

import pytest


@pytest.fixture(scope="session")
def project_root():
	"""Get project root directory

	Returns:
		 Path to project root

	Example:
		 def test_something(project_root):
			  data_file = project_root / "data" / "test.txt"
	"""
	return Path(__file__).parent.parent


@pytest.fixture(scope="session")
def benchmarks_config():
	"""Load benchmark configuration

	Returns:
		 BenchmarkConfig instance with loaded YAML

	Example:
		 def test_threshold(benchmarks_config):
			  thresholds = benchmarks_config.get_thresholds(1)
			  assert thresholds['elite'] < 1.0
	"""
	from tests.benchmark.benchmarks_parser import BENCHMARKS
	return BENCHMARKS


def pytest_configure(config):
	"""Register custom markers"""
	config.addinivalue_line("markers", "slow: marks tests as slow (>1s)")
	config.addinivalue_line("markers", "benchmark: performance benchmark tests")
	config.addinivalue_line("markers", "unit: unit tests for helpers")
	config.addinivalue_line("markers", "integration: integration tests")
