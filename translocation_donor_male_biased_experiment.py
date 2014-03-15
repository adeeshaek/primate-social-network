from translocation_donor_control_experiment import TranslocationDonorControlExperiment
from translocation_donor_male_biased_simulation import TranslocationDonorMaleBiasedSimulation

def main():
	control_experiment = TranslocationDonorMaleBiasedExperiment()
	control_experiment.run()

class TranslocationDonorMaleBiasedExperiment(TranslocationDonorControlExperiment):

	OUTPUT_XLS_NAME = "translocation_donor_male_biased_output.xls"
	NUMBER_OF_SIMULATIONS = 50

	def init_simulation(self):
		return TranslocationDonorMaleBiasedSimulation()

if __name__ == '__main__':
	main()