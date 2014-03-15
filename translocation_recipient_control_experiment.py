from control_experiment import ControlExperiment
from translocation_recipient_control_simulation import TranslocationRecipientControlSimulation

def main():
	control_experiment = TranslocationRecipientControlExperiment()
	control_experiment.run()

class TranslocationRecipientControlExperiment(ControlExperiment):

	OUTPUT_XLS_NAME = "translocation_recipient_control_output.xls"
	NUMBER_OF_SIMULATIONS = 50

	def run_loop(self, total_population_record_list,
		total_age_record_list,
		total_age_sd_record_list,
		total_number_of_groups_list,
		total_females_per_males_list,
		total_edges_per_agent_list,
		total_population_breakdown_list,
		total_population_relationships_list):

		for i in range(self.NUMBER_OF_SIMULATIONS):
		
			simulation = self.init_simulation()
			simulation.simulation_index = i
			simulation.total_simulations = self.NUMBER_OF_SIMULATIONS
			simulation.run_simulation(False, False)

			total_population_record_list.append(
				simulation.last_gen_population)
			total_age_record_list.append(
				simulation.last_gen_avg_age)
			total_age_sd_record_list.append(
				simulation.last_gen_sd_age)
			total_number_of_groups_list.append(
				simulation.last_gen_groups)
			total_females_per_males_list.append(
				simulation.last_gen_fpm)
			total_edges_per_agent_list.append(
				simulation.last_gen_epa)
			total_population_breakdown_list.append(
				simulation.last_gen_population_breakdown)
			total_population_relationships_list.append(
				simulation.total_agent_relationships_list)
			print i

	def init_simulation(self):
		return TranslocationRecipientControlSimulation()

if __name__ == '__main__':
	main()