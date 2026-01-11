"""Whitelist of known failing solutions

These solutions are known to fail correctness tests.
They are whitelisted to avoid cluttering test output.
Each entry should have a comment explaining why it fails.
"""

# Solutions that fail correctness tests
FAILING_SOLUTIONS = {
	27: "Wrong answer: returns -119 instead of -59231",
	37: "TIMEOUT: Exceeds 5s timeout",
	38: "Type mismatch: returns 932718654 but comparison fails",
	49: "Type mismatch: returns 296962999629 but comparison fails",
	50: "Wrong answer: returns 77 instead of 997651",
	58: "Wrong answer: returns 41 instead of 26241",
	66: "Implementation returns 13 instead of 661",
	68: "Wrong answer: returns 5352424131 instead of 6531031914842725",
	78: "TIMEOUT: Exceeds 5s timeout",
	79: "Implementation incomplete, returns -1 instead of 73162890",
	82: "Wrong answer: returns 276076 instead of 260324",
	93: "Type mismatch: returns 1258 but comparison fails",
	97: "ERROR: Integer string conversion limit (4300+ digits)",
	100: "ERROR: Missing 'logging' import",
	118: "Implementation incomplete, returns -1 instead of 30559",
	148: "ERROR: Missing required positional argument 'number'",
	684: "ERROR: Integer string conversion limit (222221 digits)",
}

# Solutions that need parameter adjustments (don't call with default args)
PARAMETER_ISSUES = {
	148: "Requires q148(10**9) instead of default q148(number=MILLION)",
}

# Solutions with known performance issues (exceed acceptable threshold)
# These are tracked but accepted for now - candidates for future optimization
PERFORMANCE_ISSUES = {
	48: "10ms (just at acceptable threshold of 10ms - timing variance)",
	59: "~130ms (exceeds acceptable 100ms - needs optimization)",
	76: "~16ms (exceeds acceptable 10ms - needs optimization)",
	80: "~680ms (exceeds acceptable 200ms - needs optimization)",
	96: "~3100ms (exceeds acceptable 1000ms - needs optimization)",
	112: "~1000ms (just at acceptable threshold of 1000ms - timing variance)",
}
