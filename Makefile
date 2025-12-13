# Configuration Variables
PYTHON      = python
SCRIPT_DIR  = scripts
ANALYSIS_DIR= analysis
DOCS_DIR    = docs
RESULTS_DIR = results
REPORT      = $(ANALYSIS_DIR)/sleep-disorder-analysis.qmd

# Targets

.PHONY: all help clean download-data clean-data eda model to-html to-pdf

help:
	@echo "----------------------------------------------------------------"
	@echo "                    PROJECT AUTOMATION MANAGER                  "
	@echo "----------------------------------------------------------------"
	@echo "Usage: make <target>"
	@echo ""
	@echo "  make all            Run the full pipeline (Data -> Models -> Report)"
	@echo "  make clean          Remove all generated files (keeps docs/index.html)"
	@echo ""
	@echo "Individual Steps:"
	@echo "  make download-data  Step 1: Download raw data"
	@echo "  make clean-data     Step 2: Process and clean data"
	@echo "  make eda            Step 3: Generate EDA figures"
	@echo "  make model          Step 4: Train models and save results"
	@echo "  make to-html        Render report to HTML"
	@echo "  make to-pdf         Render report to PDF"
	@echo "----------------------------------------------------------------"

all: download-data clean-data eda model to-html to-pdf

# Data Analysis Pipeline
download-data:
	$(PYTHON) $(SCRIPT_DIR)/download_data.py

clean-data: download-data
	$(PYTHON) $(SCRIPT_DIR)/clean_data.py

eda: clean-data
	$(PYTHON) $(SCRIPT_DIR)/eda.py

model: clean-data
	$(PYTHON) $(SCRIPT_DIR)/model.py

# Rendering
# Note: We use '../$(DOCS_DIR)' because Quarto resolves output relative 
# to the input file location (analysis/), not the project root.
to-html: eda model
	quarto render $(REPORT) --to html --output-dir ../$(DOCS_DIR)

to-pdf: eda model
	quarto render $(REPORT) --to pdf --output-dir ../$(DOCS_DIR)

# Cleanup
clean:
	find $(DOCS_DIR)/ -type f ! -name 'index.html' -delete
	rm -rf $(RESULTS_DIR)/*