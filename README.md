#  Hidden-Markov-Model

Solution for exercise 3 of the Master's seminar in bioinformatics. The Vertibi algorithm was implemented and functions were added in order to be able to simply execute the cube example from the lecture.

States, transition and emission probability are loaded from corresponding files which can be found in the folder data.

It is possible to calculate on the native scale as well as on the logarithmic projection.

## Experiment 1 - log vs native

While from a purely mathematical point of view the application of the logarithm should have no influence on the result, experiments have shown that it has a considerable influence on the result.

This is probably due to the lossy representation of floating point numbers. We assume that the results generated on the logarithmic projection offer greater accuracy, as they keep the calculated numbers in a better representable range, since the mantissa of the floating point numbers do not fill up.

For more information on this topic, see the keyword [Range and precision of fractional numbers](https://isaaccomputerscience.org/concepts/data_numbases_range_precision).

## Experiment 2 - reverse-input-list

If the input sequence is mirrored, the first trivial assumption is that the output sequence of the Vertibi algorithm would also be mirrored, but that there would be no structural differences to the first example.

However, when the experiment is carried out, the result is completely different. At this point we assume the reason for this behaviour is the lossy representation of the glide comma numbers mentioned earlier.

This assumption also suggests that when using the logarithmic projection, an result can be observed that is closer to the original result. This behaviour was also confirmed by further experiments.

## Experiment 3 - reverse of state-loop

Changing the loop to find the maximum should in principle have no effect on the result, since all results are calculated regardless of the order. No changes could be found in the experiments performed.