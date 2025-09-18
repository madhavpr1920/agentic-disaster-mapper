class PreprocessingAgent:
    def __init__(self):
        self.name = "PreprocessingAgent"

    def run(self, input_path: str):
        print(f"[{self.name}] Preprocessing {input_path} ...")
        return input_path
