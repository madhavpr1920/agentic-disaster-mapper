class SARFloodAgent:
    def __init__(self):
        self.name = "SARFloodAgent"

    def run(self, input_data):
        print(f"[{self.name}] Running dummy SAR flood detection ...")
        return {"flood_mask": "dummy_sar_mask.tif"}
