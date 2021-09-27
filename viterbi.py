import numpy


def viterbi(observed_values,
            transition_probabilities_input,
            emission_probabilities_input,
            initial_distribution,
            file_name,
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

    transition_probabilities= numpy.copy(transition_probabilities_input)
    emission_probabilities = numpy.copy(emission_probabilities_input)
    # Amount of steps
    epochs = observed_values.shape[0]

    # Amount of states
    states = transition_probabilities.shape[0]

    # Hightest probability to end in specific state
    omega = numpy.zeros((epochs, states), dtype=numpy.longdouble)
    prev = numpy.zeros((epochs - 1, states), dtype=numpy.longdouble)

    # Two Dimensional Array, which holds all forward probability for every
    # state and epoch
    forward_probs = numpy.zeros((epochs, states), dtype=numpy.longdouble)

    # Two Dimensional Array, which holds all backword probability for every
    # state and epoch
    backward_probs = numpy.zeros((epochs, states), dtype=numpy.longdouble)

    # Since we start at the pack of the list we need to init it with a one,
    # instead of a zero
    backward_probs[epochs - 1] = numpy.ones((states))

    # Two Dimensional Array, which holds all posteriori probability for every
    # state and epoch
    posteriori_probs = numpy.zeros((epochs, states), dtype=numpy.longdouble)

    # Calculation of the probability for the observed initial state
    if log:
        omega[0, :] = numpy.log(initial_distribution * emission_probabilities[:, observed_values[0]-1]) #noqa
        with numpy.nditer(transition_probabilities, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = numpy.log(x)
        with numpy.nditer(emission_probabilities, op_flags=['readwrite']) as it:
            for x in it:
                x[...] = numpy.log(x)
        x = transition_probabilities
        x = emission_probabilities
    else:
        omega[0, :] = initial_distribution * emission_probabilities[:, observed_values[0]-1] #noqa
        forward_probs[0, :] = initial_distribution * emission_probabilities[:, observed_values[0]-1] #noqa

    for epoch in range(1, epochs):
        for state in range(1, -1, -1):

            # Calculate the probability of obtaining the observed value for
            # each possible transition.
            if log:
                probability = omega[epoch - 1] + \
                    transition_probabilities[:, state]
                omega[epoch, state] = numpy.max(probability) + emission_probabilities[state, observed_values[epoch]-1]
            else:
                probability = omega[epoch - 1] * \
                    transition_probabilities[:, state]
                omega[epoch, state] = numpy.max(probability) * emission_probabilities[state, observed_values[epoch]-1]

            prev[epoch - 1, state] = numpy.argmax(probability)

            # This is our most probable state given previous state at epoch

            # save probability of the most probable state
            # Calculate forward probability's for Posteriori-Decoding
            # The sum of the equations is calculated with matrix
            # multiplication(.dot), since that way a generice implementation
            # is provided!
            if not log:
                forward_probs[epoch, state] = emission_probabilities[state, observed_values[epoch]-1] * forward_probs[epoch - 1].dot(transition_probabilities[:, state]) #noqa

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

        # Posteriori-Decoding, calculate backward probability's.
        # The sum of the equations is calculated with matrix
        # multiplication(.dot), since that way a generice implementation is
        # provided!
        # The results are at this point in the reversed order, since we started
        # do calculate them from the end!
        if not log:
            for state in range(states):
                backward_probs[i, state] = (backward_probs[i+1]*emission_probabilities[:, observed_values[i]-1]).dot(transition_probabilities[state, :]) #noqa

    # Flip the path array since we were backtracking
    path = numpy.flip(path, axis=0)

    # Convert numeric values to actual hidden states
    result = ""
    for element in path:
        if element == 0:
            result = result + "F"
        else:
            result = result + "L"

    # Posteriori-Decoding, calculate posteriori probability's.
    if not log:
        # Flip the backward probability's to provide the probability's in
        # the correct order
        backward_probs = numpy.flip(backward_probs, axis=0)
        increase = 1
        for i in range(epochs):
            # A counter to manage the constant multiplication used
            if(i % 20 == 0):
                # increase the multiplication factor
                increase *= numpy.longdouble(10**5)

            # Calculate the posteriori probability based on the given algorithm
            posteriori_probs[i, :] = ((forward_probs[i, :]*increase) * (backward_probs[i, :]*increase)) / (numpy.max(omega[epochs-1, :])*increase) #noqa

            # Remove the constant factor and override the current posteriori
            # probability, to give a correct value
            posteriori_probs[i, :] = posteriori_probs[i, :] / increase

            numpy.savetxt("results\\posteriori-decoding"+file_name, posteriori_probs) #noqa

    dirName = "results\\viterbi-Path"+file_name
    text_file = open(dirName, "w")
    text_file.write(result)
    text_file.close()

    return result
