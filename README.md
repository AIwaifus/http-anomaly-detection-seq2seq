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

At the testing stage, the model receives benign and anomalous samples. For each sample, the value of loss is calculated. If this value is greater than the threshold, then the request is considered anomalous.

## Sample Data

### Benign Sample

GET /vulnbank/assets/fonts/Pe-icon-7-stroke.woff?d7yf1v HTTP/1.1

Host: 10.0.212.25

Connection: keep-alive

Origin: http://10.0.212.25

User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36

Accept: */*

Referer: http://10.0.212.25/vulnbank/assets/css/pe-icon-7-stroke.css

Accept-Encoding: gzip, deflate

Accept-Language: en-US,en;q=0.9

Cookie: PHPSESSID=j1pavglp5ue30266c0j88ged30

### Anomalous sample

POST /vulnbank/online/api.