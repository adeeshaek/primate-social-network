import os

from control_simulation import ControlSimulation

from translocation_donor_control_simulation import TranslocationDonorControlSimulation
from translocation_donor_male_biased_simulation import TranslocationDonorMaleBiasedSimulation
from translocation_donor_female_biased_simulation import TranslocationDonorFemaleBiasedSimulation

from translocation_recipient_control_simulation import TranslocationRecipientControlSimulation
from translocation_recipient_male_biased_simulation import TranslocationRecipientMaleBiasedSimulation
from translocation_recipient_female_biased_simulation import TranslocationRecipientFemaleBiasedSimulation

"""
runs all the simulations, and preserves the .dot output
from a single run
"""
control_dot_directory = "dot/control/"
control_excel_filename = "control_control.xls"
donor_control_dot_directory = "dot/donor_control/"
donor_control_excel_filename = "donor_control.xls"
recipient_control_dot_directory = "dot/recipient_control/"
recipient_control_excel_filename = "recipient_control.xls"
donor_male_biased_dot_directory = "dot/donor_male_biased/"
donor_male_biased_excel_filename = "donor_male_biased.xls"
recipient_male_biased_dot_directory = "dot/recipient_male_biased/"
recipient_male_biased_excel_filename = "recipient_male_biased.xls"
donor_female_biased_dot_directory = "dot/donor_female_biased/"
donor_female_biased_excel_filename = "donor_female_biased.xls"
recipient_female_biased_dot_directory = "dot/recipient_female_biased/"
recipient_female_biased_excel_filename = "recipient_female_biased.xls"

simulations = [ControlSimulation(
	control_excel_filename, 
	control_dot_directory), 
 TranslocationDonorControlSimulation(
 	donor_control_excel_filename, 
 	donor_control_dot_directory),
 TranslocationRecipientControlSimulation(
 	recipient_control_excel_filename, 
 	recipient_control_dot_directory),
 TranslocationDonorMaleBiasedSimulation(
 	donor_male_biased_excel_filename, 
 	donor_male_biased_dot_directory),
 TranslocationRecipientMaleBiasedSimulation(
 	recipient_male_biased_excel_filename, 
 	recipient_male_biased_dot_directory),
 TranslocationDonorFemaleBiasedSimulation(
 	donor_female_biased_excel_filename, 
 	donor_female_biased_dot_directory),
 TranslocationRecipientFemaleBiasedSimulation(
 	recipient_female_biased_excel_filename, 
 	recipient_female_biased_dot_directory)]

directories = ["control/","donor_control/",
"recipient_control/", "donor_male_biased/",
"donor_female_biased/", "recipient_male_biased/",
"recipient_female_biased"]

for directory in directories:
	if not os.path.exists(directory):
    os.makedirs(directory)

number_of_simulations = len(simulations)
for i in range (number_of_simulations):
	simulation = simulations[i]
	simulation.total_simulations = number_of_simulations
	simulation.simulation_index = i
	simulation.run_simulation(True,False)
