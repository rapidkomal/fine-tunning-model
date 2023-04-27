# fine-tunning-model

### Fine-tuning improves on few-shot learning by training on many more examples than can fit in the prompt, letting you achieve better results on a wide number of tasks. Once a model has been fine-tuned, you won't need to provide examples in the prompt anymore. This saves costs and enables lower-latency requests.

#### Installation
```pip install --upgrade openai```

```export OPENAI_API_KEY="<OPENAI_API_KEY>"```

#### Prepare training data
Your data must be a JSONL document, where each line is a prompt-completion pair corresponding to a training example. You can use our CLI data preparation tool to easily convert your data into this file format.

```
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
{"prompt": "<prompt text>", "completion": "<ideal generated text>"}
...
```

```openai tools fine_tunes.prepare_data -f <LOCAL_FILE>```

#### Create a fine-tuned model

```openai api fine_tunes.create -t <TRAIN_FILE_ID_OR_PATH> -m <BASE_MODEL>```

#### To follow model

```openai api fine_tunes.follow -i <YOUR_FINE_TUNE_JOB_ID>```