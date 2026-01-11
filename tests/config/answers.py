"""Central registry of Project Euler problem answers and expected performance

This is imported by:
- Individual solutions (for self-verification)
- answers.py (for correctness and benchmark testing)
- Benchmark tests (for correctness checking)

Format:
    problem_num: {
        'answer': expected_answer,
        'expected': 'elite' | 'good' | 'acceptable'
    }

Expected speed levels:
    - 'elite': Highest performance (typically < 50ms for most problems)
    - 'good': Good performance (typically < 200ms for most problems)
    - 'acceptable': Acceptable performance (typically < 1s for most problems)

Actual thresholds are defined per-problem in performance-benchmarks-modern.yaml
"""

# Known correct answers with expected performance levels
# Format: problem_num: {'answer': value, 'expected': 'elite'|'good'|'acceptable'}
PROBLEMS = {
	1: {'answer': 233168, 'expected': 'elite'},
	2: {'answer': 4613732, 'expected': 'good'},
	3: {'answer': 6857, 'expected': 'elite'},
	4: {'answer': 906609, 'expected': 'elite'},
	5: {'answer': 232792560, 'expected': 'elite'},
	6: {'answer': 25164150, 'expected': 'elite'},
	7: {'answer': 104743, 'expected': 'good'},
	8: {'answer': 23514624000, 'expected': 'good'},
	9: {'answer': 31875000, 'expected': 'good'},
	10: {'answer': 142913828922, 'expected': 'good'},
	11: {'answer': 70600674, 'expected': 'elite'},
	12: {'answer': 76576500, 'expected': 'good'},
	13: {'answer': 5537376230, 'expected': 'good'},
	14: {'answer': 837799, 'expected': 'acceptable'},
	15: {'answer': 137846528820, 'expected': 'elite'},
	16: {'answer': 1366, 'expected': 'elite'},
	17: {'answer': 21124, 'expected': 'elite'},
	18: {'answer': 1074, 'expected': 'elite'},
	19: {'answer': 171, 'expected': 'elite'},
	20: {'answer': 648, 'expected': 'elite'},
	21: {'answer': 31626, 'expected': 'good'},
	22: {'answer': 871198282, 'expected': 'elite'},
	23: {'answer': 4179871, 'expected': 'acceptable'},
	24: {'answer': 2783915460, 'expected': 'elite'},
	25: {'answer': 4782, 'expected': 'elite'},
	26: {'answer': 983, 'expected': 'elite'},
	27: {'answer': -59231, 'expected': 'good'},
	28: {'answer': 669171001, 'expected': 'elite'},
	29: {'answer': 9183, 'expected': 'elite'},
	30: {'answer': 443839, 'expected': 'acceptable'},
	31: {'answer': 73682, 'expected': 'good'},
	32: {'answer': 45228, 'expected': 'acceptable'},
	33: {'answer': 100, 'expected': 'good'},
	34: {'answer': 40730, 'expected': 'elite'},
	35: {'answer': 55, 'expected': 'good'},
	36: {'answer': 872187, 'expected': 'elite'},
	37: {'answer': 748317, 'expected': 'good'},
	38: {'answer': 932718654, 'expected': 'good'},
	39: {'answer': 840, 'expected': 'elite'},
	40: {'answer': 210, 'expected': 'elite'},
	41: {'answer': 7652413, 'expected': 'elite'},
	42: {'answer': 162, 'expected': 'elite'},
	43: {'answer': 16695334890, 'expected': 'elite'},
	44: {'answer': 5482660, 'expected': 'good'},
	45: {'answer': 1533776805, 'expected': 'acceptable'},
	46: {'answer': 5777, 'expected': 'good'},
	47: {'answer': 134043, 'expected': 'elite'},
	48: {'answer': 9110846700, 'expected': 'acceptable'},
	49: {'answer': 296962999629, 'expected': 'good'},
	50: {'answer': 997651, 'expected': 'good'},
	51: {'answer': 121313, 'expected': 'acceptable'},
	52: {'answer': 142857, 'expected': 'good'},
	53: {'answer': 4075, 'expected': 'elite'},
	54: {'answer': 376, 'expected': 'good'},
	55: {'answer': 249, 'expected': 'elite'},
	56: {'answer': 972, 'expected': 'elite'},
	57: {'answer': 153, 'expected': 'elite'},
	58: {'answer': 26241, 'expected': 'acceptable'},
	59: {'answer': 129448, 'expected': 'acceptable'},
	60: {'answer': 26033, 'expected': 'good'},
	61: {'answer': 28684, 'expected': 'elite'},
	62: {'answer': 127035954683, 'expected': 'elite'},
	63: {'answer': 49, 'expected': 'elite'},
	64: {'answer': 1322, 'expected': 'good'},
	65: {'answer': 272, 'expected': 'elite'},
	66: {'answer': 661, 'expected': 'good'},
	67: {'answer': 7273, 'expected': 'elite'},
	68: {'answer': 6531031914842725, 'expected': 'good'},
	69: {'answer': 510510, 'expected': 'elite'},
	70: {'answer': 8319823, 'expected': 'elite'},
	71: {'answer': 428570, 'expected': 'elite'},
	72: {'answer': 303963552391, 'expected': 'acceptable'},
	76: {'answer': 190569291, 'expected': 'acceptable'},
	77: {'answer': 71, 'expected': 'acceptable'},
	79: {'answer': 73162890, 'expected': 'elite'},
	80: {'answer': 40886, 'expected': 'acceptable'},
	81: {'answer': 427337, 'expected': 'good'},
	82: {'answer': 260324, 'expected': 'good'},
	83: {'answer': 425185, 'expected': 'good'},
	85: {'answer': 2772, 'expected': 'acceptable'},
	87: {'answer': 1097343, 'expected': 'elite'},
	89: {'answer': 743, 'expected': 'good'},
	92: {'answer': 8581146, 'expected': 'elite'},
	93: {'answer': 1258, 'expected': 'good'},
	96: {'answer': 24702, 'expected': 'acceptable'},
	97: {'answer': 8739992577, 'expected': 'elite'},
	105: {'answer': 73702, 'expected': 'elite'},
	106: {'answer': 21384, 'expected': 'good'},
	107: {'answer': 259679, 'expected': 'elite'},
	108: {'answer': 180180, 'expected': 'acceptable'},
	110: {'answer': 9350130049860600, 'expected': 'acceptable'},
	111: {'answer': 612407567715, 'expected': 'elite'},
	112: {'answer': 1587000, 'expected': 'acceptable'},
	113: {'answer': 51161058134250, 'expected': 'elite'},
	114: {'answer': 16475640049, 'expected': 'elite'},
	115: {'answer': 168, 'expected': 'elite'},
	116: {'answer': 20492570929, 'expected': 'elite'},
	118: {'answer': 30559, 'expected': 'acceptable'},  # Implementation incomplete (returns -1)
	148: {'answer': 2129970655314432, 'expected': 'acceptable'},  # Test case: q148(10**9)
	684: {'answer': 922058210, 'expected': 'acceptable'},  # Full problem: q684(2, 90)
	808: {'answer': 3807504276997394, 'expected': 'good'},
}

# Legacy dict for backwards compatibility (maps problem_num -> answer only)
ANSWERS = {num: data['answer'] for num, data in PROBLEMS.items()}
