import numpy


def viterbi(observed_values,
            transition_probabilities,
            emission_probabilities,
            initial_distribution,
            log=True):
    """Calculates the viterbi-path for a given hidden-markov-model, heavily
    inspired by Abhisek Janas Blogpost "Implement Viterbi Algorithm in Hidden
    Markov Model using Python and R" at February 21, 2019.
    The Blog as well as the original source-code can be found under http://www.adeveloperdiary.com/data-science/machine-learning/implement-viterbi-algorithm-in-hidden-markov-model-using-python-and-r/ #noqa

    Args:
        observed_values (np.array): visible part of the hidden-markov-model
        transition_probabilities (np.array): transition probabilities for the
            hidden part of the hidden-markov-model
        emission_probabilities (np.array): transition probabilities for the
            visible part of the hidden-markov-model
        initial_distribution (np.array): probabilities for the initial status
        log (bool) = True: The results are calculated using the logarithmic
            projection

    Returns:
        (np.array): the viterbi-path for the given hidden-markov-model
    """
    epochs = observed_values.shape[0]
    states = transition_probabilities.shape[0]

    omega = numpy.zeros((epochs, states), dtype=numpy.float32)
    prev = numpy.zeros((epochs - 1, states), dtype=numpy.float32)

    # Calculation of the probability for the observed initial state
    if log:
        omega[0, :] = numpy.log(initial_distribution * emission_probabilities[:, observed_values[0]-1]) #noqa
    else:
        omega[0, :] = initial_distribution * emission_probabilities[:, observed_values[0]-1] #noqa

    for epoch in range(1, epochs):
        for state in range(1, -1, -1):
            # Calculate the probability of obtaining the observed value for
            # each possible transition.

            if log:
                probability = omega[epoch - 1] + \
                    numpy.log(transition_probabilities[:, state]) + \
                    numpy.log(emission_probabilities[state, observed_values[epoch]-1]) #noqa
            else:
                probability = omega[epoch - 1] * \
                    transition_probabilities[:, state] * \
                    emission_probabilities[state, observed_values[epoch]-1]

            # This is our most probable state given previous state at epoch
            prev[epoch - 1, state] = numpy.argmax(probability)

            # save probability of the most probable state
            omega[epoch, state] = numpy.max(probability)

    # Path Array
    path = numpy.zeros(epochs)

    # Find the most probable last hidden state
    last_state = numpy.argmax(omega[epochs - 1, :]).astype(int)

    # Start building the path
    path[0] = last_state

    # Start backtracking
    backtrack_index = 1
    for i in range(epochs - 2, -1, -1):
        # Calculate the next hidden state based on its successor
        next_hidden = prev[i, last_state]
        # Add state to the path
        path[backtrack_index] = next_hidden
        # Save state for the next backtracking step
        last_state = next_hidden.astype(int)
        backtrack_index += 1

    # Flip the path array since we were backtracking
    path = numpy.flip(path, axis=0)

    # Convert numeric values to actual hidden states
    result = ""
    for element in path:
        if element == 0:
            result = result + "F"
        else:
            result = result + "L"

    return result
