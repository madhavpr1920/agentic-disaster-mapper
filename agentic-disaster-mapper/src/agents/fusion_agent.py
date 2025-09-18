class FusionAgent:
    def __init__(self):
        self.name = "FusionAgent"

    def run(self, sar_output, optical_output):
        print(f"[{self.name}] Fusing SAR + Optical results ...")
        return {"report": "dummy_disaster_report.geojson"}
