# LLM LoRA Fine-Tuning

This repository contains the complete training pipeline used to fine-tune **ayarlicazhocam**, my personal AI assistant, using LoRA and open-source Large Language Models.

The project covers the entire workflow, including data collection, preprocessing, dataset creation, supervised fine-tuning (SFT), and publishing models and datasets on Hugging Face.

## Features

* LoRA / QLoRA fine-tuning
* Supervised Fine-Tuning (SFT)
* Hugging Face Datasets integration
* Google Colab training notebooks
* Chat template preprocessing
* Hugging Face model publishing

## Dataset

The training dataset was built specifically for the "ayarlicazhocam" assistant.

### Data Collection

* Information was collected through web scraping from publicly available sources relevant to the project.
* **No synthetic conversations or AI-generated training samples were used.**
* The remaining conversations, instructions, and responses were **written manually** to improve the assistant's behavior and domain knowledge.
* The dataset includes both **Turkish** and **English** conversational examples.

## Hugging Face

### Model

* `gorkemergune/ayarlicazhocam-llama-3.2-3b`

### Dataset

* `gorkemergune/ayarlicazhocam_finetune`

## Tech Stack

* Python
* Unsloth
* Hugging Face Transformers
* TRL
* PEFT
* BitsAndBytes

## Purpose

The objective of this project is to develop **ayarlicazhocam**, a conversational AI assistant capable of providing accurate and helpful responses related to software engineering, artificial intelligence, university life, and the "ayarlicazhocam" ecosystem.

## License

This repository is intended for research and educational purposes.

## Author

**Görkem Ergüne**

* GitHub: https://github.com/gorkemergune
* Hugging Face: https://huggingface.co/gorkemergune
