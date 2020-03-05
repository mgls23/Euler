def memoised(function_):
    pre_computed = {}

    def wrapper(*args):
        if args not in pre_computed:
            answer = function_(*args)
            pre_computed[args] = answer

        return pre_computed[args]

    return wrapper


def print_results(function_):
    def wrapper(*args, **kwargs):
        arguments = ', '.join(map(str, args))
        for key, value in kwargs.items():
            arguments = arguments and arguments + ', ' or arguments
            arguments += f'{key}={value}'

        results = function_(*args, **kwargs)
        print(f'{function_.__name__}({arguments})={results}')
        return results

    return wrapper


def timed_function(function_):
    def wrapper(*args, **kwargs):
        arguments = ', '.join(map(str, args))
        for key, value in kwargs.items():
            arguments = arguments and arguments + ', ' or arguments
            arguments += f'{key}={value}'

        import time
        start_time = time.time()

        results = function_(*args, **kwargs)

        time_taken = (time.time() - start_time) * 1000
        print(f'{function_.__name__}({arguments})={results}')
        print(f'Took {time_taken} ms')

        return results

    return wrapper
