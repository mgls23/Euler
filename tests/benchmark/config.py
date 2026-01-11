"""Benchmark configuration and utilities

Central module for benchmark configuration that all testing modules import from.
Provides pythonic access to performance thresholds from YAML config.
"""
from pathlib import Path

import yaml


class BenchmarkConfig:
	"""Parse and access benchmark configuration (pythonic version)"""

	def __init__(self, config_file: str = "performance-benchmarks-modern.yaml"):
		"""Initialize benchmark config

		Args:
			config_file: Name of YAML file in tests/config/
		"""
		config_path = Path(__file__).parent.parent / "config" / config_file
		with open(config_path) as f:
			self._config = yaml.safe_load(f)

	@property
	def global_thresholds(self):
		"""Access global thresholds"""
		return self._config['global_thresholds']

	@property
	def problems(self):
		"""Access problem-specific benchmarks"""
		return self._config['problems']

	def __getitem__(self, problem_num: int):
		"""Dict-like access: benchmarks[problem_num]

		Returns:
			Dict with keys: elite, good, acceptable, notes

		Example:
			>>> benchmarks = BenchmarkConfig()
			>>> benchmarks[1]['elite']
			0.1
		"""
		if problem_num in self.problems:
			return self.problems[problem_num]
		# Return global defaults if not found
		return {
			**self.global_thresholds,
			'notes': 'Using global defaults'
		}

	# Legacy method for backwards compatibility
	def get_thresholds(self, problem_num: int):
		"""Get thresholds for a problem (legacy method, use benchmarks[num] instead)"""
		return self[problem_num]

	def get_all_problems(self):
		"""Get list of all problems with benchmarks"""
		return sorted(self.problems.keys())


# Global singleton instance
benchmarks = BenchmarkConfig()
