import numpy
from viterbi import viterbi

observed_values = numpy.loadtxt('data/observed_values.npy').astype(int)
transition_probabilities = numpy.loadtxt('data/transition_probabilities.npy')
emission_probabilities = numpy.loadtxt('data/emission_probabilities.npy')
initial_distribution = numpy.loadtxt('data/initial_distribution.npy')

result = viterbi(observed_values,
                 transition_probabilities,
                 emission_probabilities,
                 initial_distribution,
                 log=True)

print("Viterbi-Path: " + result)
