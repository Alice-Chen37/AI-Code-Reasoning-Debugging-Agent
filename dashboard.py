import streamlit as st
from mulagent import MultiFileAgent
import os
import tempfile
import shutil

st.set_page_config(page_title="AI Code Reasoning & Debugging", layout="wide")
st.title("🧠 AI Code Reasoning & Debugging Dashboard")

# ===============================
# 配置模型路径与参数
# ===============================
st.sidebar.header("模型配置")
model_path = st.sidebar.text_input("模型路径", "models/ggml-gpt4all-j-v1.3-groovy.bin")
batch_size = st.sidebar.number_input("批量处理大小", min_value=1, max_value=20, value=5)
log_level = st.sidebar.selectbox("日志等级", ["INFO", "DEBUG", "ERROR"])

# ===============================
# 文件上传
# ===============================
st.sidebar.header("上传代码文件")
uploaded_files = st.sidebar.file_uploader(
    "选择 Python 文件（可多选）",
    type=["py"],
    accept_multiple_files=True
)

# ===============================
# 批量处理按钮
# ===============================
if st.sidebar.button("开始多文件分析"):
    if not uploaded_files:
        st.warning("请先上传至少一个 Python 文件")
    else:
        # 创建临时工作目录
        temp_dir = tempfile.mkdtemp()
        for f in uploaded_files:
            with open(os.path.join(temp_dir, f.name), "wb") as out_file:
                out_file.write(f.read())

        st.info(f"已上传 {len(uploaded_files)} 个文件，开始 AI 处理...")

        # 初始化多文件 agent
        agent = MultiFileAgent(model_path)

        # 批量处理文件
        results = []
        file_list = [os.path.join(temp_dir, f.name) for f in uploaded_files]
        for i in range(0, len(file_list), batch_size):
            batch_files = file_list[i:i + batch_size]
            batch_results = agent.process_files(batch_files)  # 返回 dict {filename: annotation}
            results.append(batch_results)

        # 合并结果
        final_results = {}
        for r in results:
            final_results.update(r)

        # ===============================
        # 日志和可视化展示
        # ===============================
        st.subheader("📄 AI 生成注释 & 日志")
        for fname, annotation in final_results.items():
            st.markdown(f"**文件：{os.path.basename(fname)}**")
            st.code(annotation, language="python")

        # 保存日志
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        for fname, annotation in final_results.items():
            log_file = os.path.join(log_dir, os.path.basename(fname) + ".log")
            with open(log_file, "w", encoding="utf-8") as f:
                f.write(annotation)

        st.success(f"处理完成！日志已保存到 `{log_dir}` 文件夹")
        shutil.rmtree(temp_dir)