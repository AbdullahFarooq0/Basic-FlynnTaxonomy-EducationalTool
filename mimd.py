import pandas as pd
import streamlit as st
import time

def visualize_mimd(data1, data2):
    st.write("### MIMD: Multiple Instruction, Multiple Data")
    st.write("""
    Performing two parallel tasks:
    1. Sorting the first array.
    2. Summing the second array.
    """)

    # Start timing for performance metrics
    start_time = time.time()

    # Task 1: Sorting the first array
    sorted_data = sorted(data1)
    df_sorted = pd.DataFrame(sorted_data, columns=["Sorted Values"])

    # Task 2: Summing the second array
    sum_data = sum(data2)
    end_time = time.time()

    # Display Task 1 Results
    st.write("**Task 1: Sorted Data**")
    st.table(df_sorted)

    # Display Task 2 Results
    st.write("**Task 2: Sum of Data**")
    st.success(f"Sum of the second array: {sum_data}")

    # Display performance metrics
    st.write(f"**Time Taken:** {end_time - start_time:.4f} seconds")

    # Allow downloading results
    csv_sorted = df_sorted.to_csv(index=False)
    st.download_button(
        "Download Sorted Data as CSV",
        data=csv_sorted,
        file_name="mimd_sorted_results.csv",
        mime="text/csv"
    )

    # Allow downloading sum result as a text file
    st.download_button(
        "Download Sum Result",
        data=f"Sum of second array: {sum_data}",
        file_name="mimd_sum_result.txt",
        mime="text/plain"
    )
