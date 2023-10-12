# Test runner framework

from typing import Callable

class TestRunner:
    def __init__(self, mapping: dict[str, Callable[[], bool]]):
        self.mapping = mapping

    def print_status(self, status: bool):
        result_string = "Result : {}"
        if status:
            result_string = result_string.format("✅")
        else:
            result_string = result_string.format("❌")
        print(result_string)

    def run(self, test_name: str) -> tuple[bool, list[str]]:
        if len(test_name) == 0:
            # run all
            test_result = True
            failed_tests = []
            for test_name, test_func in self.mapping.items():
                print("Running test : ", test_name)
                result = test_func()
                if result == False:
                    failed_tests.append(test_name)
                    test_result = False
                self.print_status(result)
            return (test_result, failed_tests)
        else:
            if test_name in self.mapping:
                print("Running test : ", test_name)
                result = self.mapping[test_name]()
                self.print_status(result)
                return (result, "" if result == True else test_name)
            else:
                return (False, "{} not availble in test mapping, available tests: \n{}".format(test_name, self.mapping))
