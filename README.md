# hidden-markov-model
Exercise for the Master's seminar Bioinformatics




# Exercies 2
## a 
The results are shown in the file posteriori-decoding-noLog

## b
Naively the guess is that the results differ from one another. After executing the algorithm, this is indeed the case. The reason for this, is that in each step the algorithm adds values based on the step befor. After the order of the inputs is changed the steps differ from one another, which lastly changes the results.
The final results are shown in the file posteriori-decoding-noLog and posteriori-decoding-noLog-reversed.

## b
### Viterbi
The Viterbi-algorithm calculates the single best state sequence of a given observation sequence in a hidden Markov model. 
This approach is used to solve the decoding problem of the HHM.[Hidden Markov Models ,Blunsom 2004](https://web.archive.org/web/20111125100934/http://digital.cs.usu.edu/~cyan/CS7960/hmm-tutorial.pdf)

### Posteriori-Decoding
On the other hand, the Postiori-Decoding give the probability of each step, in consideration of the step befor. This is a vastly different approach and taking a closer look, the Postiori-Decoding gives a completely different result. Additionally to calculate the results of the algorithm, it needs the results of the Viterbi algorithm. 
He is used in the Baum-Welch-Algorithm to solve the HMM learnproblem.[Hidden Markov Models ,Blunsom 2004](https://web.archive.org/web/20111125100934/http://digital.cs.usu.edu/~cyan/CS7960/hmm-tutorial.pdf)

