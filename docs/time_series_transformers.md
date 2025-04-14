# Introduction
## Definition
They use an Encoder-Decoder architecture that works very well with sequence-to-sequence tasks.

## Advantages
- Traditional RNNs or LSTMs process sequences step-by-step and respect their order &rarr; Transformers process all tokens
simultaneously, allowing computational boosting and long-range dependencies to be captured more effectively.
    - This expands the **Local Forecasting** (step-by-step) with **Probabilistic Forecasting** &rarr; Global Probabilistic
    - In order to preserve the order, a Positional Encoding is required
    - It computes positional encodings and adds them into the input token embeddings that are fed into the Transformer

# Architectures
## Informer
### Definition
It is Encoder-Decoder architecture.

### Process
1. Input time series is encoded in a lower dimensional representation by passing it through the Encoder
2. The encoded sequence is pass to the Decoder along with part of the original sequence
3. The Decoder generates all the output time steps simultaneously

### Advantages
1. It generates all output time steps simultaneously

### Drawbacks
1. Quadratic computation of self attention &rarr; Addressed by using Probabilistic Sparse Attention and not Full Attention
2. Memory bottleneck fo stacking layers for long inputs
3. Speed plunge in predicting long outputs
