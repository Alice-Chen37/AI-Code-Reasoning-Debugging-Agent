from mulagent import MultiFileAgent
import json

if __name__ == "__main__":
    agent = MultiFileAgent()
    result = agent.run("data")  # 扫描 data 文件夹

    print("\n=== MULTI-FILE RESULT ===\n")
    print(json.dumps(result, indent=2))