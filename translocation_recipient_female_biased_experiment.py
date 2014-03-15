from translocation_recipient_control_experiment import TranslocationRecipientControlExperiment
from translocation_recipient_female_biased_simulation import TranslocationRecipientFemaleBiasedSimulation

def main():
	control_experiment = TranslocationRecipientMaleBiasedExperiment()
	control_experiment.run()

class TranslocationRecipientFemaleBiasedExperiment(TranslocationRecipientControlExperiment):

	OUTPUT_XLS_NAME = "translocation_recipient_female_biased_output.xls"
	NUMBER_OF_SIMULATIONS = 50

	def init_simulation(self):
		return TranslocationRecipientFemaleBiasedSimulation()

if __name__ == '__main__':
	main()