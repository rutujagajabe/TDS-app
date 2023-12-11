# largest_number_app.py

import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

def main():
    st.title("Find the Largest Number")

    # Input for three numbers (now accepts floats)
    num1 = st.number_input("Enter the first number:", value=0.0, step=0.1)
    num2 = st.number_input("Enter the second number:", value=0.0, step=0.1)
    num3 = st.number_input("Enter the third number:", value=0.0, step=0.1)

    # Button to calculate and display the largest number
    if st.button("Find the Largest Number"):
        largest_number = find_largest_number(num1, num2, num3)
        st.success(f"The largest number is: {largest_number}")

if __name__ == "__main__":
    main()
