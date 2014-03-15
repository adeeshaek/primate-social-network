from control_experiment import ControlExperiment

from translocation_donor_control_experiment import TranslocationDonorControlExperiment
from translocation_donor_male_biased_experiment import TranslocationDonorMaleBiasedExperiment
from translocation_donor_female_biased_experiment import TranslocationDonorFemaleBiasedExperiment

from translocation_recipient_control_experiment import TranslocationRecipientControlExperiment
from translocation_recipient_male_biased_experiment import TranslocationRecipientMaleBiasedExperiment
from translocation_recipient_female_biased_experiment import TranslocationRecipientFemaleBiasedExperiment

import gc
NUMBER_OF_SIMULATIONS = 50

print "------------------------------------"
print "starting all experiments"
print "------------------------------------"

print "------------------------------------"
print "starting control experiment"
print "------------------------------------"
control_experiment =\
 ControlExperiment(NUMBER_OF_SIMULATIONS)
control_experiment.run()
del(control_experiment)
gc.collect()

print "------------------------------------"
print "starting donor control experiment"
print "------------------------------------"
donor_control_experiment =\
 TranslocationDonorControlExperiment(NUMBER_OF_SIMULATIONS)
donor_control_experiment.run()
del(donor_control_experiment)
gc.collect()

print "------------------------------------"
print "starting donor male biased experiment"
print "------------------------------------"
donor_male_biased_experiment =\
 TranslocationRecipientMaleBiasedExperiment(NUMBER_OF_SIMULATIONS)
donor_male_biased_experiment.run()
del(donor_male_biased_experiment)
gc.collect()

print "------------------------------------"
print "starting donor male biased experiment"
print "------------------------------------"
donor_female_biased_experiment =\
 TranslocationDonorFemaleBiasedExperiment(NUMBER_OF_SIMULATIONS)
donor_female_biased_experiment.run()
del(donor_female_biased_experiment)
gc.collect()

print "------------------------------------"
print "starting recipient control experiment"
print "------------------------------------"
recipient_control_experiment =\
 TranslocationRecipientControlExperiment(NUMBER_OF_SIMULATIONS)
recipient_control_experiment.run()
del(recipient_control_experiment)
gc.collect()

print "------------------------------------"
print "starting recipient male biased experiment"
print "------------------------------------"
recipient_male_biased_experiment =\
 TranslocationRecipientMaleBiasedExperiment(NUMBER_OF_SIMULATIONS)
recipient_male_biased_experiment.run()
del(recipient_male_biased_experiment)
gc.collect()

print "------------------------------------"
print "starting recipient male biased experiment"
print "------------------------------------"
recipient_female_biased_experiment =\
 TranslocationRecipientFemaleBiasedExperiment(NUMBER_OF_SIMULATIONS)
recipient_female_biased_experiment.run()
del(recipient_female_biased_experiment)
gc.collect()

print "------------------------------------"
print "all experiments complete"
print "------------------------------------"