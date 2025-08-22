# End to end Text-Summarizer-Project

## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update entity
4. Update the configuration manager in src config
5. update the conponents
6. update the pipeline
7. update the main.py
8. update the app.py


# Text Summarization Project with Pegasus

A comprehensive text summarization system that uses Google's Pegasus model from Hugging Face Transformers to generate abstractive summaries from dialogue text.

## 📋 Project Overview

This project implements an end-to-end text summarization pipeline that:
- Ingests and preprocesses dialogue data
- Fine-tunes the Pegasus transformer model
- Generates high-quality abstractive summaries
- Provides a scalable training and evaluation framework

## 🚀 Features

- **Data Ingestion**: Automated download and extraction of summarization datasets
- **Data Validation**: Quality checks and validation of processed data
- **Data Transformation**: Tokenization and preprocessing for transformer models
- **Model Training**: Fine-tuning of Pegasus model on custom datasets
- **Model Evaluation**: Comprehensive metrics for summary quality assessment
- **Modular Architecture**: Clean, maintainable code structure with configuration management

## 🛠️ Technical Stack

- **Framework**: Python 3.8+
- **ML Library**: Hugging Face Transformers
- **Model**: Google Pegasus (pegasus-cnn_dailymail)
- **Data Processing**: Datasets library, PyArrow
- **Configuration**: YAML-based configuration management
- **Logging**: Custom logging with timestamps and stage tracking


