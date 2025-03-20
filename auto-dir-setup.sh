#!/bin/bash

mkdir -p project_root/config
mkdir -p project_root/data_cleaning
mkdir -p project_root/data_loading
mkdir -p project_root/data_transformation
mkdir -p project_root/dataset
mkdir -p project_root/encodings
mkdir -p project_root/models
mkdir -p project_root/training

touch __init__.py evaluate.py inference.py train_pipeline.py transform_pipeline.py
touch project_root/config/__init__.py project_root/data_cleaning/__init__.py project_root/data_loading/__init__.py project_root/data_transformation/__init__.py project_root/models/__init__.py project_root/training/__init__.py

chmod +x evaluate.py
chmod +x inference.py
chmod +x train_pipeline.py
