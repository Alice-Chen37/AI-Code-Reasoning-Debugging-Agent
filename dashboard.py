import streamlit as st
import json
from mulagent import MultiFileAgent
from tools import scan_project

st.set_page_config(page_title="AI Code Reasoning Agent", layout="wide")
st.title("AI Code Reasoning & Debugging Agent")

# 选择扫描的文件夹
project_path = st.text_input("Enter project folder path:", "data")

if st.button("Run Agent"):
    agent = MultiFileAgent()
    result = agent.run(project_path)

    st.subheader("Files Detected")
    for f in result["files"]:
        st.write(f"- {f}")

    st.subheader("Cross-File Bug Info")
    st.json(result["debug"])

    st.subheader("Reasoning Steps")
    steps = result["reasoning"].split("\n")
    for s in steps:
        st.write(s)

    st.subheader("Trajectory")
    st.json(result["trajectory"])

    st.subheader("File Contents")
    files = scan_project(project_path)
    for name, code in files.items():
        st.code(code, language="python")