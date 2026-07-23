# LLM LoRA Fine-Tuning

This repository contains the complete training pipeline used to fine-tune **ayarlicazhocam**, my personal AI assistant, using LoRA and open-source Large Language Models.

> **Note:** This is a **research project** and my **first end-to-end fine-tuning experiment**. The goal is to learn the full LoRA/SFT workflow hands-on — data collection, dataset design, training, publishing, and evaluation — and to study what actually works and what breaks along the way. Results, mistakes, and findings are documented openly (see [`BENCHMARK_REPORT.md`](BENCHMARK_REPORT.md)) as part of the learning process.

The project covers the entire workflow, including data collection, synthetic data generation, preprocessing, dataset creation, supervised fine-tuning (SFT), and publishing models and datasets on Hugging Face.

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

The dataset combines three complementary sources:

* **Web scraping** — information collected from publicly available sources relevant to the project (see [`scrapers/`](scrapers/)).
* **Manually written** — conversations, instructions, and responses hand-authored to shape the assistant's behavior and domain knowledge.
* **Synthetically generated** — bulk instruction/response pairs produced programmatically to expand topic coverage and scale up the dataset (`scrapers/generate_bulk_*.py` → `scrapers/bulk_en*.json`, `scrapers/bulk_tr*.json`, 34 EN + 36 TR batches).

The dataset includes both **Turkish** and **English** conversational examples.

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

As a research and learning project, an equally important goal is to **understand the fine-tuning process itself** — how chat templates, data quality, and training configuration affect the final model — and to document the outcomes honestly, including failure modes.

## Status & Findings

This is an active first-iteration experiment. Key findings so far (full details in [`BENCHMARK_REPORT.md`](BENCHMARK_REPORT.md)):

* The first published adapter was trained with a **mismatched chat template** (Gemma-3 format on a Llama tokenizer), which weakened instruction-following and left persona facts poorly learned.
* On the Turkish MMLU benchmark the model currently scores around the random baseline, and it tends to **hallucinate** identity answers not present in the dataset.
* The training notebook has since been corrected to use the proper `llama-3.1` template; retraining and re-evaluation are the next steps.

These results are expected for a first fine-tuning attempt and are kept in the repo as part of the research record.
