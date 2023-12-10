# THIS IS NO LONGER MAINTAINED
# http-anomaly-detection-seq2seq
An immersive Natural Language Processing (NLP) based solution to identify and flag suspicious HTTP requests. The project was initially forked from [seq2seq-web-attack-detection](https://github.com/PositiveTechnologies/seq2seq-web-attack-detection) and is now being maintained by AIwaifus. 

## Model Parameters
• batch_size - 128 - the number of samples in a batch.

• embed_size - 64 -  the dimension of embedding space (should be less than vocabulary size).

• hidden_size - 64 - the number of hidden states in lstm.

• num_layers - 2 - the number of lstm blocks.

• checkpoints - path to checkpoint directory.

• std_factor - 6. - the number of stds that is used for defining a model threshold.

• dropout - 0.7 - the probability that each element is kept.

• vocab - the Vocabulary object.

In the parameters setting stage,  the threshold setting is introduced. Set_threshold calculates the threshold value using mean and std of loss values of valid samples.

At the testing