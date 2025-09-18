import sys
import os

# Add project root (the folder containing `src`) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from src.agents.preprocessing_agent import PreprocessingAgent
from src.agents.sar_flood_agent import SARFloodAgent
from src.agents.fusion_agent import FusionAgent
from src.agents.optical_damage_agent import OpticalDamageAgent

def run_pipeline(input_path: str):
    pre = PreprocessingAgent()
    sar = SARFloodAgent()
    opt = OpticalDamageAgent()
    fus = FusionAgent()

    data = pre.run(input_path)
    sar_out = sar.run(data)
    opt_out = opt.run(data)
    final = fus.run(sar_out, opt_out)

    print("Final output:", final)
    
if __name__ == "__main__":
    input_path = "path/to/disaster_data"
    run_pipeline(input_path)
    