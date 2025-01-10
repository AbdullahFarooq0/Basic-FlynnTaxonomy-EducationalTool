import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import time
import numpy as np

def visualize_simd(data):
    st.write("### SIMD: Single Instruction, Multiple Data")
    st.write("""
    In SIMD, a single instruction is applied to multiple data points simultaneously.
    Here, we are squaring each value in the input list.
    """)

    # Check for valid input
    if not data:
        st.error("No data provided! Please input a list of numbers.")
        return

    try:
        # Start timing for performance metrics
        start_time = time.time()

        # Computation
        result = [x**2 for x in data]
        end_time = time.time()

        df = pd.DataFrame({"Original Data": data, "Processed Data (Squared)": result})

        # Step-by-step explanation
        st.write("**Step-by-Step Process:**")
        for i, (original, processed) in enumerate(zip(data, result)):
            st.write(f"Step {i + 1}: {original} squared is {processed}")

        # Visualization: Original vs Processed Data
        st.write("**Visualization:**")
        fig, ax = plt.subplots()
        ax.bar(range(len(data)), data, label="Original Data", alpha=0.6, color='blue')
        ax.bar(range(len(data)), result, label="Processed Data (Squared)", alpha=0.6, color='green')
        ax.set_title("SIMD: Single Instruction Applied to Multiple Data Points")
        ax.set_xlabel("Data Index")
        ax.set_ylabel("Value")
        ax.legend()
        st.pyplot(fig)

        # Show final results in a table
        st.write("**Final Results Table:**")
        st.table(df)

        # Display performance metrics
        st.write(f"**Time Taken:** {end_time - start_time:.4f} seconds")

        # Allow downloading results
        csv = df.to_csv(index=False)
        st.download_button(
            "Download Results as CSV",
            data=csv,
            file_name="simd_results.csv",
            mime="text/csv"
        )

        # Advanced computation: Matrix multiplication
        st.write("### Advanced Computation: Matrix Multiplication")
        matrix = np.array([[1, 2], [3, 4]])
        st.write("**Input Matrix:**")
        st.write(matrix)
        squared_matrix = np.dot(matrix, matrix)
        st.write("**Squared Matrix (Matrix Multiplication):**")
        st.write(squared_matrix)

    except Exception as e:
        st.error(f"An error occurred during computation: {e}")
