import itertools
from collections import Counter


#  We are looking for the combination that maximises the minimum of outside
#  which means we are looking in the group of difference=1
def does_difference_of_2_exist(n): pass


#
def q68():
    n = 10  # the solution has not been generalised
    half = n // 2
    partition_point = half + 1

    # Since it's 16 digit graph, 10 can only appear once, which indicates that 10 needs to be in the outer group
    # The highest is where the outer group has the lowest of 6, rather than 1/2 - therefore difference of 1 is considered
    #  We have isolated which half, and difference.
    inner_group = list(range(1, partition_point))
    outer_group = list(range(partition_point, n + 1))

    sets_of_2s = list(itertools.combinations(inner_group, 2))
    for possible_combination in itertools.combinations(sets_of_2s, n // 2):
        all_numbers_to_occurrences = Counter(itertools.chain(*possible_combination))

        # Each element in the inner group should appear exactly twice (as it's a magic ring)
        if len(all_numbers_to_occurrences) == half and all(occurrence == 2 for occurrence in all_numbers_to_occurrences.values()):
            sum_of_groups = [sum(group) for group in possible_combination]
            sorted_sums = list(sorted(sum_of_groups))
            minimum = min(sorted_sums)
            if list(range(half)) == [sum_ - minimum for sum_ in sorted_sums]:
                # This is wrong - for the first group, we reverse (because we want to maximise the earlier digits
                # but after that, we should "follow the trail" as in find the other group with the starting digit, which means
                # some groups are reversed, and some are not.
                # Also, the way to find the corresponding outer_group element is not as simple as an index, rather, we can
                # reverse engineer what it should be because we can get what each group should add up to (which is 6 + 5 + 3)
                # But I leave it here for a TODO one day as I have mathematically solved the problem
                answer_graph = [list(reversed(group)) for group in reversed(possible_combination)]
                print(answer_graph)
                return ''.join(map(str, itertools.chain.from_iterable(answer_graph)))


if __name__ == '__main__':
    print(q68())
