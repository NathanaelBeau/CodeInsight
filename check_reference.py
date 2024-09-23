from codeinsight import CodeInsightDataset

def check_reference(dataset: CodeInsightDataset):
    results = {}

    # Loop through each problem in the dataset
    for problem in dataset:
        code = problem.data["code"]

        # Check this code against the associated unit tests
        test_result = problem.test(code)
        problem_id = problem.problem_id
        results[problem_id] = test_result

    return results

if __name__ == "__main__":
    dataset = CodeInsightDataset(mode='all')
    results = check_reference(dataset)

    for problem_id, success in results.items():
        status = "PASSED" if success else "FAILED"
        print(f"Tests for problem ID {problem_id}: {status}")
