import json
from tools import scan_project, detect_cross_file_bug

MEMORY_FILE = "memory.json"

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f, indent=2)


class ReasoningAgent:
    def __init__(self):
        self.memory = load_memory()

    def generate_reasoning(self, code):
        # 模拟 LLM 输出
        return (
            "Step 1: Read the code\n"
            "Step 2: Identify compute_total function\n"
            "Step 3: Detect unexpected '+ 10' addition\n"
            "Step 4: Suggest fix by removing '+ 10'"
        )

    def generate_trajectory(self, reasoning):
        steps = reasoning.split("\n")
        trajectory = []
        for i, step in enumerate(steps):
            if step.strip():
                trajectory.append({
                    "step": i + 1,
                    "action": step.strip(),
                    "type": "reasoning"
                })
        return trajectory

    def run(self, file_path):
        files = scan_project("data")  # 扫描 data 文件夹
        code = files.get(file_path, "")
        debug_info = detect_cross_file_bug({file_path: code})
        reasoning = self.generate_reasoning(code)
        trajectory = self.generate_trajectory(reasoning)

        result = {
            "file": file_path,
            "debug": debug_info,
            "reasoning": reasoning,
            "trajectory": trajectory
        }

        self.memory[file_path] = result
        save_memory(self.memory)

        return result


if __name__ == "__main__":
    agent = ReasoningAgent()
    res = agent.run("main.py")
    print(json.dumps(res, indent=2))