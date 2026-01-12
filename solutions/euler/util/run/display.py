"""Display and formatting utilities for Project Euler solution results."""

import shutil
from typing import List

import polars as pl
from colorama import Fore, Style
from rich.console import Console
from rich.table import Table
from rich.text import Text

from tests.config.whitelist import FAILING_SOLUTIONS, PERFORMANCE_ISSUES

from .performance import PERFORMANCE_CATEGORIES, CATEGORY_STYLES

# Skip printing per-solution lines and summary for whitelisted failures.
SHOW_WHITELISTED = False


def format_problem_num(problem_num: int, pad: int = 3) -> str:
    """Format problem number with zero padding for output."""
    return f"Q{problem_num:0{pad}d}"


def print_results_table(df: pl.DataFrame):
    """Print per-solution results as a rich table."""
    terminal_width = shutil.get_terminal_size(fallback=(160, 24)).columns
    console = Console(width=max(160, terminal_width))
    rows_df = df
    if not SHOW_WHITELISTED:
        rows_df = rows_df.filter(~pl.col('whitelisted'))
    rows_df = rows_df.sort('problem')

    def max_len(values: List[str], minimum: int, maximum: int | None = None) -> int:
        max_value = max((len(v) for v in values), default=minimum)
        width = max(minimum, max_value)
        if maximum is not None:
            width = min(maximum, width)
        return width

    problem_vals = [str(row['problem']) for row in rows_df.iter_rows(named=True)]
    runtime_vals = [
        f"{row['elapsed_ms']:06.2f}ms" if row['elapsed_ms'] is not None else "-"
        for row in rows_df.iter_rows(named=True)
    ]
    status_vals = [
        f"{PERFORMANCE_CATEGORIES[row['category']]['symbol']} {row['category'].lower()}"
        if row.get('category') in PERFORMANCE_CATEGORIES
        else f"\u2717 {row.get('status', '-').lower()}"
        for row in rows_df.iter_rows(named=True)
    ]
    note_vals = [(row.get('notes') or "-") for row in rows_df.iter_rows(named=True)]
    grade_vals = [
        (row.get('category') or row.get('status') or "-").lower()
        for row in rows_df.iter_rows(named=True)
    ]
    exp_vals = [
        (row.get('expected_level') or "-").lower()
        for row in rows_df.iter_rows(named=True)
    ]
    id_width = max_len(problem_vals + ["id"], minimum=2)
    ms_width = max_len(runtime_vals + ["ms"], minimum=8)
    state_width = max_len(status_vals + ["state"], minimum=12, maximum=32)
    note_width = max_len(note_vals + ["note"], minimum=24, maximum=60)
    grade_width = max_len(grade_vals + ["grade"], minimum=5)
    exp_width = max_len(exp_vals + ["expected"], minimum=8)

    # Account for Rich table borders and column separators:
    # | col1 | col2 | col3 | ... | colN | = 3 chars per column + 1 final border
    num_columns = 6
    border_width = (num_columns * 3) + 1
    total_width = (
        id_width + ms_width + note_width + grade_width +
        exp_width + state_width + border_width
    )
    console = Console(width=max(160, total_width))

    results_table = Table(title="Solution Results", show_header=True, header_style="bold", expand=False)
    results_table.add_column("id", no_wrap=True, justify="right", width=id_width)
    results_table.add_column("ms", no_wrap=True, justify="right", width=ms_width)
    results_table.add_column("note", overflow="ellipsis", no_wrap=True, width=note_width)
    results_table.add_column("grade", no_wrap=True, width=grade_width)
    results_table.add_column("expected", no_wrap=True, width=exp_width)
    results_table.add_column("state", no_wrap=True, width=state_width)

    for row in rows_df.iter_rows(named=True):
        problem = str(row['problem'])
        elapsed = row['elapsed_ms']
        runtime = f"{elapsed:06.2f}ms" if elapsed is not None else "-"
        category = row.get('category')
        status = row.get('status', '')
        expected = (row.get('expected_level') or '-').lower()
        notes = row.get('notes') or ''
        explanation = notes or "-"

        if category in PERFORMANCE_CATEGORIES:
            emoji = PERFORMANCE_CATEGORIES[category]['symbol']
            grade = category.lower()
            row_style = CATEGORY_STYLES.get(category, None)
        else:
            emoji = '\u2717'
            grade = status.lower() if status else '-'
            row_style = 'red'

        if status == 'WHITELISTED':
            row_style = 'yellow'

        row_values = [problem]
        if row_style:
            row_values.append(Text(runtime, style=row_style))
        else:
            row_values.append(runtime)
        row_values.extend([explanation])

        level_weights = {'elite': 3, 'good': 2, 'acceptable': 1}
        grade_weight = level_weights.get(grade)
        expected_weight = level_weights.get(expected)

        grade_text = grade
        expected_text = expected
        recommendation = ""
        if grade_weight is not None and expected_weight is not None:
            if grade_weight < expected_weight:
                grade_text = Text(grade, style="yellow")
                expected_text = Text(expected, style="yellow")
                recommendation = Text("regress", style="yellow")
            elif grade_weight > expected_weight:
                grade_text = Text(grade, style="green")
                expected_text = Text(expected, style="green")
                recommendation = Text("upgrade", style="green")

        # Show category for performance categories, status otherwise
        if category in PERFORMANCE_CATEGORIES:
            state = f"{emoji} {grade}"
        else:
            state = f"{emoji} {status.lower() if status else '-'}"

        if recommendation:
            state = f"{state} ({recommendation})"
        state_text = Text(state, style=row_style) if row_style else state
        row_values.extend([grade_text, expected_text, state_text])
        results_table.add_row(*row_values)

    console.print(results_table)


def print_summary(df: pl.DataFrame, total_time: float, summary_rows: int):
    """Print summary statistics from dataframe."""
    print("\n" + "=" * 60)
    print("PERFORMANCE SUMMARY")
    print("=" * 60)

    passed = df.filter(pl.col('status') == 'PASS')
    if len(passed) == 0:
        print(f"\n{Fore.YELLOW}No passing solutions to summarize.{Style.RESET_ALL}")
        return

    console = Console()

    # Performance score
    total = len(passed)
    elite_score = len(passed.filter(pl.col('category') == 'ELITE')) * 3
    good_score = len(passed.filter(pl.col('category') == 'GOOD')) * 2
    acceptable_score = len(passed.filter(pl.col('category') == 'ACCEPTABLE')) * 1
    max_score = total * 3
    actual_score = elite_score + good_score + acceptable_score

    percentage = (actual_score / max_score * 100) if max_score > 0 else 0
    print(f"\n{Fore.MAGENTA}Performance Score: {actual_score}/{max_score} ({percentage:.1f}%){Style.RESET_ALL}")
    print(f"Total execution time: {total_time:.2f}ms ({total_time / 1000:.2f}s)")

    # Category counts (tabular)
    category_weights = {
        'elite': 3,
        'good': 2,
        'acceptable': 1,
        'needs_optimization': 0
    }
    weight_expr = pl.col('category').map_elements(
        lambda cat: category_weights.get(cat, -1),
        return_dtype=pl.Int64
    )
    counts = (
        passed
        .with_columns(pl.col('category').str.to_lowercase())
        .group_by('category')
        .agg(pl.len().alias('count'))
        .with_columns(weight_expr.alias('weight'))
        .sort('weight', descending=True)
        .drop('weight')
    )
    counts_table = Table(title="Category Counts", show_header=True, header_style="bold")
    counts_table.add_column("category")
    counts_table.add_column("count", justify="right")
    for row in counts.iter_rows(named=True):
        counts_table.add_row(str(row['category']), str(row['count']))
    console.print(counts_table)


def print_failures(df: pl.DataFrame):
    """Print correctness and performance failures."""
    correctness_failures = df.filter(
        (pl.col('status').is_in(['FAILED', 'TIMEOUT', 'ERROR'])) &
        (~pl.col('whitelisted'))
    )

    performance_failures = df.filter(pl.col('status') == 'PERF_FAIL')

    if len(correctness_failures) > 0:
        print(f"\n{Fore.RED}{'=' * 60}")
        print(f"\u26a0\ufe0f  CORRECTNESS FAILURES ({len(correctness_failures)})")
        print(f"{'=' * 60}{Style.RESET_ALL}")
        for row in correctness_failures.iter_rows(named=True):
            print(f"{Fore.RED}   {format_problem_num(row['problem'])}: {row['error']}{Style.RESET_ALL}")

    if len(performance_failures) > 0:
        print(f"\n{Fore.RED}{'=' * 60}")
        print(f"\u26a0\ufe0f  PERFORMANCE FAILURES ({len(performance_failures)})")
        print(f"{'=' * 60}{Style.RESET_ALL}")
        for row in performance_failures.iter_rows(named=True):
            print(f"{Fore.RED}   {format_problem_num(row['problem'])}: {row['error']}{Style.RESET_ALL}")


def print_whitelist_warnings(df: pl.DataFrame):
    """Print warnings about whitelisted failures."""
    if not SHOW_WHITELISTED:
        return

    whitelisted = df.filter(pl.col('whitelisted'))

    if len(whitelisted) > 0:
        print(f"\n{Fore.YELLOW}{'=' * 60}")
        print(f"\u26a0\ufe0f  WHITELISTED FAILURES ({len(whitelisted)})")
        print(f"{'=' * 60}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}These solutions are known to fail and are whitelisted:{Style.RESET_ALL}\n")

        for row in whitelisted.iter_rows(named=True):
            problem = row['problem']
            reason = FAILING_SOLUTIONS.get(problem, "Unknown reason")
            print(f"{Fore.YELLOW}   {format_problem_num(problem)}: {reason}{Style.RESET_ALL}")

        print(f"\n{Fore.YELLOW}Update whitelist in: tests/config/whitelist.py{Style.RESET_ALL}")


def print_performance_issues(df: pl.DataFrame):
    """Print known performance issues (solutions exceeding acceptable threshold)."""
    # Filter for problems in PERFORMANCE_ISSUES that passed correctness
    perf_issues = df.filter(
        (pl.col('problem').is_in(list(PERFORMANCE_ISSUES.keys()))) &
        (pl.col('status') == 'PASS')
    )

    if len(perf_issues) > 0:
        console = Console(width=max(160, shutil.get_terminal_size(fallback=(160, 24)).columns))
        print(f"\n{Fore.CYAN}{'=' * 60}")
        print(f"\u23f1\ufe0f  KNOWN PERFORMANCE ISSUES ({len(perf_issues)})")
        print(f"{'=' * 60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}These solutions exceed acceptable threshold but are accepted:{Style.RESET_ALL}\n")

        table = Table(show_header=True, header_style="bold")
        table.add_column("id", justify="right")
        table.add_column("ms", justify="right")
        table.add_column("reason")

        for row in perf_issues.iter_rows(named=True):
            problem = row['problem']
            reason = PERFORMANCE_ISSUES.get(problem, "Unknown reason")
            elapsed = row['elapsed_ms']
            table.add_row(
                str(problem),
                f"{elapsed:.2f}ms",
                reason
            )

        console.print(table)
        print(f"\n{Fore.CYAN}These are candidates for future optimization.{Style.RESET_ALL}")


def print_divergences(df: pl.DataFrame):
    """Print performance divergences (upgrades and regressions)."""
    divergences = df.filter(pl.col('divergence').is_not_null())

    if len(divergences) > 0:
        console = Console(width=max(160, shutil.get_terminal_size(fallback=(160, 24)).columns))
        upgrades = divergences.filter(pl.col('divergence').str.contains("\u2b06\ufe0f"))
        # Filter out known performance issues from regressions
        regressions = divergences.filter(
            pl.col('divergence').str.contains("\u2b07\ufe0f") &
            (~pl.col('problem').is_in(list(PERFORMANCE_ISSUES.keys())))
        )

        if len(upgrades) > 0:
            print(f"\n{Fore.GREEN}{'=' * 60}")
            print(f"\u2b06\ufe0f  PERFORMANCE UPGRADES ({len(upgrades)})")
            print(f"{'=' * 60}{Style.RESET_ALL}")
            print(f"{Fore.GREEN}These solutions perform better than expected:{Style.RESET_ALL}\n")

            table = Table(show_header=True, header_style="bold")
            table.add_column("id", justify="right")
            table.add_column("rec")
            table.add_column("elite", justify="right")
            table.add_column("good", justify="right")
            table.add_column("acc", justify="right")
            for row in upgrades.iter_rows(named=True):
                table.add_row(
                    str(row['problem']),
                    row['divergence'].replace("\u2b06\ufe0f  Could upgrade:", "").strip(),
                    str(row['elite_threshold']),
                    str(row['good_threshold']),
                    str(row['acceptable_threshold']),
                )
            console.print(table)

        if len(regressions) > 0:
            print(f"\n{Fore.RED}{'=' * 60}")
            print(f"\u2b07\ufe0f  PERFORMANCE REGRESSIONS ({len(regressions)})")
            print(f"{'=' * 60}{Style.RESET_ALL}")
            print(f"{Fore.RED}These solutions perform worse than expected:{Style.RESET_ALL}\n")

            table = Table(show_header=True, header_style="bold")
            table.add_column("id", justify="right")
            table.add_column("rec")
            table.add_column("elite", justify="right")
            table.add_column("good", justify="right")
            table.add_column("acc", justify="right")
            for row in regressions.iter_rows(named=True):
                table.add_row(
                    str(row['problem']),
                    row['divergence'].replace("\u2b07\ufe0f  Regression:", "").strip(),
                    str(row['elite_threshold']),
                    str(row['good_threshold']),
                    str(row['acceptable_threshold']),
                )
            console.print(table)
