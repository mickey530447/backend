import unittest
import os
import json
import sys

class DriverTest(unittest.TestCase):
    def test_testresult_possible_answer(self):
        sync_path = os.path.abspath(os.path.dirname(os.path.abspath(__file__)) + '/../sync')
        testResultPath = sync_path + "/translated.json"

        if (os.path.exists(testResultPath)):
            with open(sync_path + "/translated.json", "r") as read_it:
                testresults = json.load(read_it)

            with open(sync_path + '/testcases.db.json', "r") as read_it:
                testcases = json.load(read_it)
                # Extract a dict of possible answer ids per testcase for easier comparison
                possible_answers = {testcase['testNumber']: [answer['ans_id'] for answer in testcase['possibleAnswers']] for testcase in testcases}

            for result in testresults:
                with self.subTest(case=result):
                    curr_test_num = result['testNumber']
                    curr_result_num = result['result']
                    self.assertIn(curr_test_num, possible_answers, 'Testcase %d is not alive or does not exist' % curr_test_num)
                    # test whether each answer id in the new test results exists in the test case descriptions
                    self.assertIn(curr_result_num, possible_answers[curr_test_num], 'Error in test result number: ' + str(curr_test_num))
        else:
            print("There are no new test results")

if __name__ == '__main__':
    unittest.main()
