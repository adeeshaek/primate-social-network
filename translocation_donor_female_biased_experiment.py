from translocation_donor_control_experiment import TranslocationDonorControlExperiment
from translocation_donor_female_biased_simulation import TranslocationDonorFemaleBiasedSimulation

def main():
	control_experiment = TranslocationDonorFemaleBiasedExperiment()
	control_experiment.run()

class TranslocationDonorFemaleBiasedExperiment(TranslocationDonorControlExperiment):

	OUTPUT_XLS_NAME = "translocation_donor_female_biased_output.xls"
	NUMBER_OF_SIMULATIONS = 50

	def init_simulation(self):
		return TranslocationDonorFemaleBiasedSimulation()

if __name__ == '__main__':
	main()