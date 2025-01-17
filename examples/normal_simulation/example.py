import time
import sys
import os
sys.path.append(os.path.abspath("/home/rod/Desktop/sumo-modular-framework"))

from environment.core.BaseEnv import SumoBaseEnvironment
from environment.modules.CellsModule import CellsModule
from environment.modules.EmissionsModule import EmissionsModule, EmissionType
from environment.modules.EmissionsRendererModule import EmissionsRendererModule
from environment.modules.InductionLoopsModule import InductionLoopsModule

class CustomExperiment(SumoBaseEnvironment):
	def __init__(self, env_dir, out_dir=False, use_gui=False, num_seconds=20000, start_at=0):
		super().__init__(env_dir, out_dir, use_gui, num_seconds, start_at)


		cells 		= CellsModule(self._cell_shapes, self._edges_in_cells, self.cell_max_height, self.cell_max_width, self.cell_height, self.cell_width)
		emissions 	= EmissionsModule(cells, self.output_dir,[EmissionType.CO2], update_every=60, save_every=60, save_to_file=True)
		inductions 	= InductionLoopsModule(self.output_dir, self._induction_loops)
		emissions_renderer = EmissionsRendererModule(emissions, [EmissionType.CO2], False)

		# Extra modules
		extra_modules = []
		extra_modules.append(cells)
		extra_modules.append(emissions)
		extra_modules.append(emissions_renderer)
		extra_modules.append(inductions)

		self.set_extra_modules(extra_modules)



	def run(self):
		start = time.time()

		self.reset()
		while not self.is_done:
				self.step()

if __name__ == "__main__":
	env = CustomExperiment(env_dir="/home/rod/Desktop/sumo-modular-framework/examples/normal_simulation/simulation_env/",out_dir="/home/rod/Desktop/sumo-modular-framework/examples/normal_simulation/outputs",use_gui=False,num_seconds=86400)
	env.run()
