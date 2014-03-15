from translocation_recipient_control_experiment import TranslocationRecipientControlExperiment
from translocation_recipient_male_biased_simulation import TranslocationRecipientMaleBiasedSimulation

def main():
	control_experiment = TranslocationRecipientMaleBiasedExperiment()
	control_experiment.run()

class TranslocationRecipientMaleBiasedExperiment(TranslocationRecipientControlExperiment):

	OUTPUT_XLS_NAME = "translocation_recipient_male_biased_output.xls"
	NUMBER_OF_SIMULATIONS = 50

	def init_simulation(self):
		return TranslocationRecipientMaleBiasedSimulation()

if __name__ == '__main__':
	main()