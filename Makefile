# Makefile for DSCI 522 Project: Understanding Stress Through Sleep Patterns
# This Makefile automates the data analysis pipeline

# Variables
# Use conda run to execute in the dsci522 environment
# If you prefer to activate the environment manually, you can override by setting:
# make all CONDA_ENV=""
CONDA_ENV ?= dsci522
PYTHON = $(if $(CONDA_ENV),conda run -n $(CONDA_ENV) python3,python3)
QUARTO = $(if $(CONDA_ENV),conda run -n $(CONDA_ENV) quarto,quarto)
DATA_RAW := data/raw/sleep_data_raw.csv
DATA_PROCESSED := data/processed/sleep_data_clean.csv
RESULTS_DIR := results
ANALYSIS_DIR := analysis
QUARTO_SOURCE := $(ANALYSIS_DIR)/sleep-disorder-analysis.qmd
QUARTO_HTML := $(ANALYSIS_DIR)/sleep-disorder-analysis.html
QUARTO_PDF := $(ANALYSIS_DIR)/sleep-disorder-analysis.pdf
QUARTO_FILES_DIR := $(ANALYSIS_DIR)/sleep-disorder-analysis_files

# Results files
EDA_RESULT := $(RESULTS_DIR)/eda_summary.png
MODEL_CV_RESULT := $(RESULTS_DIR)/model_analysis_cv_results.png
MODEL_TEST_RESULT := $(RESULTS_DIR)/model_analysis_test_metrics.png
MODEL_PLOTS_RESULT := $(RESULTS_DIR)/model_analysis_prediction_plots.png

# Scripts
SCRIPT_DOWNLOAD := scripts/download_data.py
SCRIPT_CLEAN := scripts/clean_data.py
SCRIPT_EDA := scripts/eda.py
SCRIPT_MODEL := scripts/model.py

.PHONY: all clean download_data clean_data eda model quarto_html quarto_pdf

# Default target: run all scripts and generate Quarto outputs
all: $(QUARTO_HTML) $(QUARTO_PDF)
	@echo "All targets completed successfully!"

# Download raw data
download_data: $(DATA_RAW)

$(DATA_RAW): $(SCRIPT_DOWNLOAD)
	@echo "Downloading raw data..."
	$(PYTHON) $(SCRIPT_DOWNLOAD)
	@echo "Raw data downloaded to $(DATA_RAW)"

# Clean and preprocess data
clean_data: $(DATA_PROCESSED)

$(DATA_PROCESSED): $(DATA_RAW) $(SCRIPT_CLEAN)
	@echo "Cleaning and preprocessing data..."
	$(PYTHON) $(SCRIPT_CLEAN)
	@echo "Cleaned data saved to $(DATA_PROCESSED)"

# Exploratory Data Analysis
eda: $(EDA_RESULT)

$(EDA_RESULT): $(DATA_PROCESSED) $(SCRIPT_EDA)
	@echo "Running Exploratory Data Analysis..."
	$(PYTHON) $(SCRIPT_EDA) --output-dir $(RESULTS_DIR)
	@echo "EDA results saved to $(EDA_RESULT)"

# Model analysis
model: $(MODEL_CV_RESULT) $(MODEL_TEST_RESULT) $(MODEL_PLOTS_RESULT)

$(MODEL_CV_RESULT) $(MODEL_TEST_RESULT) $(MODEL_PLOTS_RESULT): $(DATA_PROCESSED) $(SCRIPT_MODEL)
	@echo "Running model analysis..."
	$(PYTHON) $(SCRIPT_MODEL)
	@echo "Model analysis results saved to $(RESULTS_DIR)/"

# Render Quarto to HTML
quarto_html: $(QUARTO_HTML)

$(QUARTO_HTML): $(QUARTO_SOURCE) $(EDA_RESULT) $(MODEL_CV_RESULT) $(MODEL_TEST_RESULT) $(MODEL_PLOTS_RESULT)
	@echo "Rendering Quarto document to HTML..."
	@rm -rf .quarto 2>/dev/null || true
	@if [ -f _quarto.yml ]; then mv _quarto.yml _quarto.yml.bak; fi
	@cd $(ANALYSIS_DIR) && $(QUARTO) render sleep-disorder-analysis.qmd --to html --output-dir .; \
	RENDER_EXIT=$$?; \
	cd ..; \
	if [ -f _quarto.yml.bak ]; then mv _quarto.yml.bak _quarto.yml; fi; \
	exit $$RENDER_EXIT
	@echo "HTML report generated at $(QUARTO_HTML)"

# Render Quarto to PDF
quarto_pdf: $(QUARTO_PDF)

$(QUARTO_PDF): $(QUARTO_SOURCE) $(EDA_RESULT) $(MODEL_CV_RESULT) $(MODEL_TEST_RESULT) $(MODEL_PLOTS_RESULT)
	@echo "Rendering Quarto document to PDF..."
	@rm -rf .quarto 2>/dev/null || true
	@if [ -f _quarto.yml ]; then mv _quarto.yml _quarto.yml.bak; fi
	@cd $(ANALYSIS_DIR) && $(QUARTO) render sleep-disorder-analysis.qmd --to pdf --output-dir .; \
	RENDER_EXIT=$$?; \
	cd ..; \
	if [ -f _quarto.yml.bak ]; then mv _quarto.yml.bak _quarto.yml; fi; \
	exit $$RENDER_EXIT
	@echo "PDF report generated at $(QUARTO_PDF)"

# Clean all generated files
clean:
	@echo "Cleaning generated files..."
	@rm -f $(DATA_RAW)
	@rm -f $(DATA_PROCESSED)
	@rm -f $(RESULTS_DIR)/*.png
	@rm -f $(QUARTO_HTML)
	@rm -f $(QUARTO_PDF)
	@rm -rf $(QUARTO_FILES_DIR)
	@rm -rf .quarto
	@echo "Clean completed!"

