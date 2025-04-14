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