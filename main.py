import numpy
from viterbi import viterbi

observed_values = numpy.loadtxt('data/observed_values.npy').astype(int)
transition_probabilities = numpy.loadtxt('data/transition_probabilities.npy')
emission_probabilities = numpy.loadtxt('data/emission_probabilities.npy')
initial_distribution = numpy.loadtxt('data/initial_distribution.npy')
backward_observed_values = numpy.flip(observed_values, axis=0)

_ = viterbi(observed_values,
            transition_probabilities,
            emission_probabilities,
            initial_distribution,
            "-noLog",
            log=False)

_ = viterbi(backward_observed_values,
            transition_probabilities,
            emission_probabilities,
            initial_distribution,
            "-noLog-reversed",
            log=False)

_ = viterbi(observed_values,
            transition_probabilities,
            emission_probabilities,
            initial_distribution,
            "log",
            log=True)

_ = viterbi(backward_observed_values,
            transition_probabilities,
            emission_probabilities,
            initial_distribution,
            "log-reversed",
            log=True)
