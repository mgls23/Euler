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
	2: {'answer': 4613732, 'expected': 'elite'},
	3: {'answer': 6857, 'expected': 'good'},
	4: {'answer': 906609, 'expected': 'good'},
	5: {'answer': 232792560, 'expected': 'elite'},
	6: {'answer': 25164150, 'expected': 'elite'},
	7: {'answer': 104743, 'expected': 'good'},
	8: {'answer': 23514624000, 'expected': 'elite'},
	9: {'answer': 31875000, 'expected': 'elite'},
	10: {'answer': 142913828922, 'expected': 'good'},
	11: {'answer': 70600674, 'expected': 'elite'},
	12: {'answer': 76576500, 'expected': 'good'},
	13: {'answer': 5537376230, 'expected': 'elite'},
	14: {'answer': 837799, 'expected': 'acceptable'},
	15: {'answer': 137846528820, 'expected': 'elite'},
	16: {'answer': 1366, 'expected': 'elite'},
	17: {'answer': 21124, 'expected': 'good'},
	18: {'answer': 1074, 'expected': 'elite'},
	19: {'answer': 171, 'expected': 'elite'},
	20: {'answer': 648, 'expected': 'elite'},
	21: {'answer': 31626, 'expected': 'good'},
	22: {'answer': 871198282, 'expected': 'good'},
	23: {'answer': 4179871, 'expected': 'good'},
	24: {'answer': 2783915460, 'expected': 'elite'},
	25: {'answer': 4782, 'expected': 'good'},
	26: {'answer': 983, 'expected': 'good'},
	27: {'answer': -59231, 'expected': 'good'},
	28: {'answer': 669171001, 'expected': 'elite'},
	29: {'answer': 9183, 'expected': 'elite'},
	30: {'answer': 443839, 'expected': 'good'},
	31: {'answer': 73682, 'expected': 'elite'},
	32: {'answer': 45228, 'expected': 'good'},
	33: {'answer': 100, 'expected': 'elite'},
	34: {'answer': 40730, 'expected': 'good'},
	35: {'answer': 55, 'expected': 'acceptable'},
	36: {'answer': 872187, 'expected': 'good'},
	37: {'answer': 748317, 'expected': 'good'},
	38: {'answer': 932718654, 'expected': 'good'},
	39: {'answer': 840, 'expected': 'good'},
	40: {'answer': 210, 'expected': 'elite'},
	41: {'answer': 7652413, 'expected': 'good'},
	42: {'answer': 162, 'expected': 'good'},
	43: {'answer': 16695334890, 'expected': 'good'},
	44: {'answer': 5482660, 'expected': 'acceptable'},
	45: {'answer': 1533776805, 'expected': 'elite'},
	46: {'answer': 5777, 'expected': 'good'},
	47: {'answer': 134043, 'expected': 'acceptable'},
	48: {'answer': 9110846700, 'expected': 'elite'},
	49: {'answer': 296962999629, 'expected': 'good'},
	50: {'answer': 997651, 'expected': 'good'},
	51: {'answer': 121313, 'expected': 'acceptable'},
	52: {'answer': 142857, 'expected': 'good'},
	53: {'answer': 4075, 'expected': 'good'},
	54: {'answer': 376, 'expected': 'good'},
	55: {'answer': 249, 'expected': 'acceptable'},
	56: {'answer': 972, 'expected': 'good'},
	57: {'answer': 153, 'expected': 'good'},
	58: {'answer': 26241, 'expected': 'acceptable'},
	59: {'answer': 129448, 'expected': 'good'},
	60: {'answer': 26033, 'expected': 'acceptable'},
	61: {'answer': 28684, 'expected': 'good'},
	62: {'answer': 127035954683, 'expected': 'acceptable'},
	63: {'answer': 49, 'expected': 'good'},
	64: {'answer': 1322, 'expected': 'good'},
	65: {'answer': 272, 'expected': 'good'},
	67: {'answer': 7273, 'expected': 'good'},
	68: {'answer': 6531031914842725, 'expected': 'good'},
	69: {'answer': 510510, 'expected': 'good'},
	70: {'answer': 8319823, 'expected': 'acceptable'},
	71: {'answer': 428570, 'expected': 'acceptable'},
	72: {'answer': 303963552391, 'expected': 'good'},
	76: {'answer': 190569291, 'expected': 'elite'},
	77: {'answer': 71, 'expected': 'good'},
	79: {'answer': 73162890, 'expected': 'elite'},
	80: {'answer': 40886, 'expected': 'good'},
	81: {'answer': 427337, 'expected': 'elite'},
	82: {'answer': 260324, 'expected': 'good'},
	83: {'answer': 425185, 'expected': 'good'},
	85: {'answer': 2772, 'expected': 'good'},
	87: {'answer': 1097343, 'expected': 'acceptable'},
	89: {'answer': 743, 'expected': 'good'},
	92: {'answer': 8581146, 'expected': 'acceptable'},
	93: {'answer': 1258, 'expected': 'good'},
	96: {'answer': 24702, 'expected': 'good'},
	97: {'answer': 8739992577, 'expected': 'elite'},
	105: {'answer': 73702, 'expected': 'good'},
	106: {'answer': 21384, 'expected': 'good'},
	107: {'answer': 259679, 'expected': 'good'},
	108: {'answer': 180180, 'expected': 'acceptable'},
	110: {'answer': 9350130049860600, 'expected': 'acceptable'},
	111: {'answer': 612407567715, 'expected': 'acceptable'},
	112: {'answer': 1587000, 'expected': 'acceptable'},
	113: {'answer': 51161058134250, 'expected': 'good'},
	114: {'answer': 16475640049, 'expected': 'good'},
	115: {'answer': 168, 'expected': 'good'},
	116: {'answer': 20492570929, 'expected': 'good'},
}

# Legacy dict for backwards compatibility (maps problem_num -> answer only)
ANSWERS = {num: data['answer'] for num, data in PROBLEMS.items()}
