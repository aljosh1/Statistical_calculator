
import streamlit as st

st.title("Statistical Calculator")
st.write("Enter numbers to analyze your dataset.")


# ==========================================
# 1. FUNCTION TO CALCULATE THE MEAN
# ==========================================

def calculate_mean(numbers):
    if len(numbers) == 0:
        raise ValueError("The dataset cannot be empty.")

    total = 0

    for number in numbers:
        total = total + number

    mean = total / len(numbers)

    return mean


# ==========================================
# 2. FUNCTION TO CALCULATE THE MEDIAN
# ==========================================

def calculate_median(numbers):
    if len(numbers) == 0:
        raise ValueError("The dataset cannot be empty.")

    sorted_numbers = sorted(numbers)

    n = len(sorted_numbers)

    middle = n // 2

    if n % 2 == 1:
        median = sorted_numbers[middle]

    else:
        median = (
            sorted_numbers[middle - 1]
            + sorted_numbers[middle]
        ) / 2

    return median


# ==========================================
# 3. FUNCTION TO CALCULATE THE MODE
# ==========================================

def calculate_mode(numbers):
    if len(numbers) == 0:
        raise ValueError("The dataset cannot be empty.")

    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    highest_frequency = max(frequency.values())

    if highest_frequency == 1:
        return []

    modes = []

    for number, count in frequency.items():
        if count == highest_frequency:
            modes.append(number)

    return sorted(modes)

# ==========================================
# 4. FUNCTION TO CALCULATE THE MINIMUM
# ==========================================

def calculate_minimum(numbers):
    if len(numbers) == 0:
        raise ValueError("The dataset cannot be empty.")

    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


# ==========================================
# 5. FUNCTION TO CALCULATE THE MAXIMUM
# ==========================================

def calculate_maximum(numbers):
    if len(numbers) == 0:
        raise ValueError("The dataset cannot be empty.")

    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


# ==========================================
# 6. FUNCTION TO CALCULATE THE RANGE
# ==========================================

def calculate_range(numbers):
    minimum = calculate_minimum(numbers)
    maximum = calculate_maximum(numbers)

    return maximum - minimum

# ==========================================
# 7. ACCEPT DATA FROM THE USER
# ==========================================

user_input = st.text_input(
    "Enter numbers separated by commas",
    placeholder="10, 20, 30, 40, 50"
)


# ==========================================
# 8. PROCESS THE DATA AND DISPLAY RESULTS
# ==========================================

if user_input:
    try:
        numbers = [
            float(value.strip())
            for value in user_input.split(",")
        ]

        st.subheader("Your Dataset")
        st.write(numbers)

        # Calculate the statistics
        mean = calculate_mean(numbers)
        median = calculate_median(numbers)
        mode = calculate_mode(numbers)
        minimum = calculate_minimum(numbers)
        maximum = calculate_maximum(numbers)
        range_value = calculate_range(numbers)

        # Display the results
        st.subheader("Statistical Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Mean", f"{mean:.2f}")

        with col2:
            st.metric("Median", f"{median:.2f}")

        with col3:
            if mode:
                mode_text = ", ".join(
                    f"{value:g}" for value in mode
                )
                st.metric("Mode", mode_text)
            else:
                st.metric("Mode", "No mode")

        col4, col5, col6 = st.columns(3)

        with col4:
            st.metric("Minimum", f"{minimum:.2f}")

        with col5:
            st.metric("Maximum", f"{maximum:.2f}")

        with col6:
            st.metric("Range", f"{range_value:.2f}")

    except ValueError:
        st.error(
            "Please enter valid numbers separated by commas."
        )
