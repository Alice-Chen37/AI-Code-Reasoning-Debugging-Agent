from tools import scan_project, detect_cross_file_bug

class MultiFileAgent:
    def __init__(self):
        pass  # 不需要 GPT4All

    def build_context(self, files):
        context = ""
        for name, code in files.items():
            context += f"\nFile: {name}\n{code}\n"
        return context

    def generate_reasoning(self, context):
        # 模拟 LLM 输出 reasoning
        return (
            "Step 1: Inspect all project files\n"
            "Step 2: Identify functions and dependencies\n"
            "Step 3: Detect compute_total bug in calc.py\n"
            "Step 4: Suggest fix by removing '+ 10'"
        )

    def generate_trajectory(self, reasoning):
        steps = reasoning.split("\n")
        return [
            {"step": i+1, "action": s.strip(), "type": "cross-file reasoning"}
            for i, s in enumerate(steps) if s.strip()
        ]

    def run(self, project_path):
        files = scan_project(project_path)
        context = self.build_context(files)
        debug_info = detect_cross_file_bug(files)
        reasoning = self.generate_reasoning(context)
        trajectory = self.generate_trajectory(reasoning)

        return {
            "files": list(files.keys()),
            "debug": debug_info,
            "reasoning": reasoning,
            "trajectory": trajectory
        }