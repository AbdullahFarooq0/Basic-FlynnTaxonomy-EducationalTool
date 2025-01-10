import streamlit as st
from sisd import visualize_sisd
from simd import visualize_simd
from misd import visualize_misd
from mimd import visualize_mimd

st.title("Flynn's Taxonomy Visualization")
st.write("""
This application demonstrates the four architectures in Flynn's Taxonomy:
**SISD**, **SIMD**, **MISD**, and **MIMD**.
Explore educational diagrams, animations, and real-life examples. Test your understanding with a quiz!
""")

# Sidebar for architecture selection
architecture = st.sidebar.selectbox("Choose an architecture:", ["SISD", "SIMD", "MISD", "MIMD", "Quiz"])

if architecture == "SISD":
    st.header("SISD: Single Instruction, Single Data")
    st.markdown("### Description:")
    st.write("In SISD, instructions are executed one by one on a single data point.")
    st.image("images/sisd_diagram.png", caption="SISD Data Flow", use_container_width=True) # Educational Diagram

    st.markdown("### Real-Life Example:")
    with st.expander("See Real-Life Example"):
        st.write("**Example:** A simple calculator performing addition step-by-step.")

    numbers = st.text_input("Enter a list of numbers (comma-separated):", "1,2,3,4")
    try:
        numbers = list(map(int, numbers.split(",")))
        if st.button("Visualize SISD"):
            visualize_sisd(numbers)
    except ValueError:
        st.error("Invalid input! Please enter a comma-separated list of integers.")

elif architecture == "SIMD":
    st.header("SIMD: Single Instruction, Multiple Data")
    st.markdown("### Description:")
    st.write("In SIMD, the same instruction is applied to multiple data points simultaneously.")
    st.image("images/simd_diagram.png", caption="SIMD Data Flow", use_container_width=True) # Educational Diagram

    st.markdown("### Real-Life Example:")
    with st.expander("See Real-Life Example"):
        st.write("**Example:** Applying filters to an image where all pixels are processed simultaneously.")

    data = st.text_input("Enter a list of numbers (comma-separated):", "1,2,3,4")
    try:
        data = list(map(int, data.split(",")))
        if st.button("Visualize SIMD"):
            visualize_simd(data)
    except ValueError:
        st.error("Invalid input! Please enter a comma-separated list of integers.")

elif architecture == "MISD":
    st.header("MISD: Multiple Instruction, Single Data")
    st.markdown("### Description:")
    st.write("In MISD, multiple instructions are applied to the same data point.")
    st.image("images/misd_diagram.png", caption="MISD Data Flow", use_container_width=True) # Educational Diagram

    st.markdown("### Real-Life Example:")
    with st.expander("See Real-Life Example"):
        st.write("**Example:** Fault tolerance in pipelines where multiple algorithms validate the same input.")

    data = st.number_input("Enter a single number:", value=5)
    if st.button("Visualize MISD"):
        visualize_misd(data)

elif architecture == "MIMD":
    st.header("MIMD: Multiple Instruction, Multiple Data")
    st.markdown("### Description:")
    st.write("In MIMD, different instructions operate on different data points simultaneously.")
    st.image("images/mimd_diagram.png", caption="MIMD Data Flow", use_container_width=True) # Educational Diagram

    st.markdown("### Real-Life Example:")
    with st.expander("See Real-Life Example"):
        st.write("**Example:** Cloud-based systems running sorting and summing operations simultaneously.")

    data1 = st.text_input("Enter the first array (comma-separated):", "5,2,9")
    data2 = st.text_input("Enter the second array (comma-separated):", "1,2,3")
    try:
        data1 = list(map(int, data1.split(",")))
        data2 = list(map(int, data2.split(",")))
        if st.button("Visualize MIMD"):
            visualize_mimd(data1, data2)
    except ValueError:
        st.error("Invalid input! Please enter comma-separated lists of integers.")

elif architecture == "Quiz":
    st.header("Flynn's Taxonomy Quiz")
    st.write("Test your understanding of the concepts.")
    question1 = st.radio(
        "1. Which architecture applies a single instruction to multiple data points?",
        ["SISD", "SIMD", "MISD", "MIMD"]
    )
    if st.button("Submit Answer for Q1"):
        if question1 == "SIMD":
            st.success("Correct!")
        else:
            st.error("Try again!")
