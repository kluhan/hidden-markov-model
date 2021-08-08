#  Hidden-Markov-Model

Solution for exercise 3 of the Master's seminar in bioinformatics. The Vertibi algorithm was implemented and functions were added in order to be able to simply execute the cube example from the lecture.

States, transition and emission probability are loaded from corresponding files which can be found in the folder data.

It is possible to calculate on the native scale as well as on the logarithmic projection.

## Exercise 1

### Experiment 1 - log vs native

While from a purely mathematical point of view the application of the logarithm should have no influence on the result, experiments have shown that it has a considerable influence on the result.

This is probably due to the lossy representation of floating point numbers. We assume that the results generated on the logarithmic projection offer greater accuracy, as they keep the calculated numbers in a better representable range, since the mantissa of the floating point numbers do not fill up.

For more information on this topic, see the keyword [Range and precision of fractional numbers](https://isaaccomputerscience.org/concepts/data_numbases_range_precision).

### Experiment 2 - reverse-input-list

If the input sequence is mirrored, the first trivial assumption is that the output sequence of the Vertibi algorithm would also be mirrored, but that there would be no structural differences to the first example.

However, when the experiment is carried out, the result is completely different. At this point we assume the reason for this behavior is the lossy representation of the glide comma numbers mentioned earlier.

This assumption also suggests that when using the logarithmic projection, an result can be observed that is closer to the original result. This behavior was also confirmed by further experiments.

### Experiment 3 - reverse of state-loop

Changing the loop to find the maximum should in principle have no effect on the result, since all results are calculated regardless of the order. No changes could be found in the experiments performed.



## Exercise 2

### Experiment 1 - posteriori
The results are shown in the file posteriori-decoding-noLog

## Experiment 2 - reversed
Naively the guess is that the results differ from one another. After executing the algorithm, this is indeed the case. The reason for this, is that in each step the algorithm adds values based on the step before. After the order of the inputs is changed the steps differ from one another, which lastly changes the results.
The final results are shown in the file posteriori-decoding-noLog and posteriori-decoding-noLog-reversed.

## Experiment 3 - differences
### Viterbi
The Viterbi-algorithm calculates the single best state sequence of a given observation sequence in a hidden Markov model. 
This approach is used to solve the decoding problem of the HHM.[Hidden Markov Models ,Blunsom 2004](https://web.archive.org/web/20111125100934/http://digital.cs.usu.edu/~cyan/CS7960/hmm-tutorial.pdf)

### Posteriori-Decoding
On the other hand, the Postiori-Decoding give the probability of each step, in consideration of the step before. This is a vastly different approach and taking a closer look, the Postiori-Decoding gives a completely different result. Additionally to calculate the results of the algorithm, it needs the results of the Viterbi algorithm. 
He is used in the Baum-Welch-Algorithm to solve the HMM learning problem.[Hidden Markov Models ,Blunsom 2004](https://web.archive.org/web/20111125100934/http://digital.cs.usu.edu/~cyan/CS7960/hmm-tutorial.pdf)

## Disclaimer
**All experiments were performed with numpy 128-bit floating point numbers. The results can vary greatly depending on the size of the used data type.**

