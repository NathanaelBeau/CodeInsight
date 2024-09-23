# Dataset: CodeInsight

## Overview
The **CodeInsight** dataset is designed for code generation tasks, providing developers with expert-curated examples that bridge the gap between conceptual intent and functional code. This dataset aids in both model fine-tuning and evaluation, addressing common challenges faced by developers.

## Dataset Description
- **Purpose**: To support developers in generating Python code by providing clarified intents, associated code snippets, and related unit tests.
- **Content**: 
  - 3,409 unique, expert-curated Python code examples
  - Includes clarified intents, code snippets, and an average of three related unit tests per example.
  - Covers a wide range of libraries, including Pandas, Numpy, Regex, and over 70 standard Python libraries derived from Stack Overflow.

## Data Format
- **File Format**: JSONL
- **Structure**: Each entry contains the following fields:
  - `id`: Unique identifier for each example
  - `intent`: Clarified description of the coding task
  - `code`: The generated code snippet
  - `unit_tests`: Related unit tests
  - `libraries`: Libraries utilized in the example

## Installation
To use the dataset, download it from [insert download link] and load it into your development environment.

### Requirements
- Python 3.x
- Libraries: [e.g., Pandas, NumPy]

## Usage
Here’s a simple example of how to load and use the dataset:

```python
import pandas as pd

# Load the dataset
data = pd.read_json('path/to/dataset.jsonl', lines=True)

# Example usage
print(data.head())
