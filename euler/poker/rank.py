from abc import abstractmethod


def fight_it_out(ranks1, ranks2):
    for i in range(len(ranks1)):
        rank1, rank2 = ranks1[i], ranks2[i]
        if not rank1 == rank2:
            return rank1.can_own(rank2)

    raise Exception('Draws??!')


class Rank:
    def can_own(self, that_guy):
        if not isinstance(that_guy, Rank): raise Exception('WTF are you doing')

        my_rank = self.get_rank()
        that_guys_rank = that_guy.get_rank()
        if my_rank == that_guys_rank:
            return self._can_own_that_geezer(that_guy)
        else:
            return my_rank > that_guys_rank

    def get_rank(self):
        return ALL_RANKS.index(type(self))

    def _can_own_that_geezer(self, that_guy):
        return fight_it_out(self.fighters(), that_guy.fighters())

    @abstractmethod
    def __eq__(self, other):
        raise Exception('Implement this please')

    @abstractmethod
    def fighters(self):
        raise Exception('Implement this please')


class RoyalStraightFlush(Rank):
    def __eq__(self, other):
        pass

    def _can_own_that_geezer(self, that_guy):
        pass


class Triple(Rank):
    pass


class FullHouse(Rank):
    def __eq__(self, that_guy: 'FullHouse'):
        return self.triple == that_guy.triple and self.pair == that_guy.pair

    def fighters(self):
        return [self.triple, self.pair]

    def __init__(self, triple: 'Triple', pair: 'Pair'):
        self.triple = triple
        self.pair = pair


class DoublePair(Rank):
    def __eq__(self, other):
        pass

    def fighters(self):
        pass


class Pair(Rank):
    pass


# class HighCard(Rank):
#     def fighters(self):


ALL_RANKS = [
    RoyalStraightFlush
    , FOUR_OF_A_KIND
    , Flush
    , Straight
    , FullHouse
    , TRIPLE
    , DoublePair
    , Pair
    , HighCard
]
