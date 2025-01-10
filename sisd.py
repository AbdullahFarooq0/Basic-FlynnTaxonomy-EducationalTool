import streamlit as st
import time

def visualize_sisd(numbers):
    st.write("### SISD: Single Instruction, Single Data")
    st.write("Processing data sequentially:")
    
    result = 0
    start_time = time.time()  # Performance Measurement
    for i, num in enumerate(numbers):
        st.write(f"Step {i + 1}: Add {num}")
        result += num
        time.sleep(0.5)  # Simulate processing delay
    end_time = time.time()

    st.success(f"Final Result: {result}")
    st.write(f"**Time Taken:** {end_time - start_time:.4f} seconds")

    # Allow downloading results
    csv = f"Step,Value\n" + "\n".join([f"{i+1},{num}" for i, num in enumerate(numbers)])
    st.download_button("Download Results as CSV", data=csv, file_name="sisd_results.csv", mime="text/csv")
