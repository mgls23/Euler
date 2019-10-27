def create_batch_test(cases, function):
    def case(self):
        for key, model_value in cases:
            test_value = function(key)
            self.assertEqual(test_value, model_value)

    return case


def create_individual_test(function, provided, expected):
    def case(self):
        self.assertEqual(function(provided), expected)

    return case


def create_individual_tests(test_unit, cases, function):
    for key, value in cases.items():
        test_name = 'test_{}'.format(key)
        test = create_individual_test(function=function, provided=key, expected=value)
        setattr(test_unit, test_name, test)
