from control_simulation import ControlSimulation
from xlwt import Workbook
import data_saver
import constants
import math

def main():
	control_experiment = ControlExperiment()
	control_experiment.run()

class ControlExperiment:

	OUTPUT_XLS_NAME = "control_control_output.xls"
	NUMBER_OF_SIMULATIONS = 50

	def run(self):
		total_population_record_list = []
		total_age_record_list = []
		total_age_sd_record_list = []
		total_number_of_groups_list = []
		total_females_per_males_list = []
		total_edges_per_agent_list = []
		total_population_breakdown_list = []

		self.run_loop(total_population_record_list,
		 total_age_record_list,
		 total_age_sd_record_list,
		 total_number_of_groups_list,
		 total_females_per_males_list,
		 total_edges_per_agent_list,
		 total_population_breakdown_list)

		self.save_output_data(total_population_record_list,
			total_age_record_list,
			total_age_sd_record_list,
			total_number_of_groups_list,
			total_females_per_males_list,
			total_edges_per_agent_list,
			total_population_breakdown_list)

	def run_loop(self, total_population_record_list,
		total_age_record_list,
		total_age_sd_record_list,
		total_number_of_groups_list,
		total_females_per_males_list,
		total_edges_per_agent_list,
		total_population_breakdown_list):

		for i in range(self.NUMBER_OF_SIMULATIONS):
			
			simulation = ControlSimulation()
			simulation.simulation_index = i
			simulation.total_simulations = self.NUMBER_OF_SIMULATIONS
			simulation.run_simulation()

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

			print i

	def save_output_data(self, total_population_record_list,
			total_age_record_list,
			total_age_sd_record_list,
			total_number_of_groups_list,
			total_females_per_males_list,
			total_edges_per_agent_list,
			total_population_breakdown_list):

		book = Workbook()
		data_saver.save_experiment_data(book,
			total_population_record_list,
			total_age_record_list,
			total_age_sd_record_list,
			total_number_of_groups_list,
			total_females_per_males_list,
			total_edges_per_agent_list)

		data_saver.save_experiment_population_data(
			book, total_population_breakdown_list,
			total_population_record_list)

		output_directory =\
		 constants.OUTPUT_FOLDER + self.OUTPUT_XLS_NAME
		book.save(output_directory)


if __name__ == '__main__':
	main()