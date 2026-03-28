# mulmain.py
from mulagent import MultiFileAgent
import json

agent = MultiFileAgent()  # ✅ 不传任何模型文件
result = agent.run("data")  # 扫描 data 文件夹

print("\n=== MULTI-FILE RESULT ===\n")
print(json.dumps(result, indent=2))