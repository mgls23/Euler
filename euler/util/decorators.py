def memoised(function_):
    pre_computed = {}

    def wrapper(*args):
        if args not in pre_computed:
            answer = function_(*args)
            pre_computed[args] = answer

        return pre_computed[args]

    return wrapper
