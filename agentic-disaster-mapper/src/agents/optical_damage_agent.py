class OpticalDamageAgent:
    def __init__(self):
        self.name = "OpticalDamageAgent"

    def run(self, input_data):
        print(f"[{self.name}] Running dummy optical damage detection ...")
        return {"damage_mask": "dummy_optical_mask.tif"}
