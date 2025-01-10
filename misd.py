import pandas as pd
import streamlit as st
import time

def visualize_misd(data):
    st.write("### MISD: Multiple Instruction, Single Data")
    st.write("Applying multiple instructions to the same data:")

    # Start timing for performance metrics
    start_time = time.time()

    # Perform operations
    operations = {
        "Square": data**2,
        "Cube": data**3,
        "Reciprocal": None if data == 0 else 1 / data,
    }
    end_time = time.time()

    df = pd.DataFrame(operations.items(), columns=["Operation", "Result"])

    # Show results
    st.table(df)

    # Display performance metrics
    st.write(f"**Time Taken:** {end_time - start_time:.4f} seconds")

    # Allow downloading results
    csv = df.to_csv(index=False)
    st.download_button(
        "Download Results as CSV",
        data=csv,
        file_name="misd_results.csv",
        mime="text/csv"
    )
