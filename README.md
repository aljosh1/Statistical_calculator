# Statistical_calculator
# Python Statistical Calculator

A web-based statistical calculator built with Python and Streamlit. The project aims to help users analyze numerical datasets and understand how common statistical measures are calculated.

The core statistical algorithms are implemented from scratch to strengthen my understanding of Python programming, mathematical formulas, and data analysis. The results will later be compared with established statistical libraries.

## Features

The calculator is being developed incrementally, with the following features:

- **Mean:** Calculates the arithmetic average of a dataset.
- **Median:** Finds the middle value after sorting the data.
- **Mode:** Identifies the most frequently occurring value or values.
- **Minimum:** Finds the smallest observation.
- **Maximum:** Finds the largest observation.
- **Range:** Calculates the difference between the maximum and minimum values.

Additional features planned for future versions include variance, standard deviation, data visualization, and comparisons with statistical libraries.

## Technologies Used

- Python
- Streamlit
- Git and GitHub (for version control and project hosting)

## Getting Started

### Prerequisites

Make sure you have Python installed on your computer.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aljosh1
   ```

2. Navigate to the project directory:

   ```bash
   cd statistical_calculator
   ```

3. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

4. Activate the virtual environment.

   On Windows PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux:

   ```bash
   source .venv/bin/activate
   ```

5. Install Streamlit:

   ```bash
   python -m pip install streamlit
   ```

### Running the Application

Start the application with:

```bash
python -m streamlit run app.py
```

Streamlit will provide a local address where you can open the calculator in your web browser.

## How to Use

1. Open the application in your browser.
2. Enter numerical values separated by commas.
3. View the dataset displayed by the application.
4. Examine the calculated statistical measures.
5. Try different datasets to observe how the results change.

Example dataset:

```text
10, 20, 30, 40, 50
```

Expected results:

| Statistic | Result |
|---|---:|
| Mean | 30 |
| Median | 30 |
| Mode | No mode |
| Minimum | 10 |
| Maximum | 50 |
| Range | 40 |

## Learning Objectives

This project is designed to develop my understanding of:

- Python functions and control flow.
- Lists, loops, and dictionaries.
- Input validation and error handling.
- Statistical formulas and their implementation.
- Building interactive web applications with Streamlit.
- Testing algorithms against established statistical libraries.

## Future Improvements

- Implement population and sample variance.
- Implement population and sample standard deviation.
- Add quartiles and the interquartile range.
- Improve input validation and error handling.
- Add data visualization.
- Compare custom implementations with NumPy and Python's statistics library.
- Add automated tests for statistical calculations.
- Improve the interface and user experience.

## Project Status

This project is under active development. New statistical operations and improvements will be added as development progresses.

## Author

Alabi Joshua Ibukunoluwa

## License

A license has not yet been selected.