# Seqly
Seqly is a CLI tool for DNA, RNA, and Protein sequence analysis and pairwise alignment.

## Installation
It is recommended to install Seqly in an **isolated environment**.

### Option 1: Using Python `venv`

1. Create a virtual environment:

```bash
python -m venv env_name #you can customize the environment name
````

2. Activate the environment:

* **Windows:**

```bash
.\env_name\Scripts\activate
```

* **Linux / macOS:**

```bash
source env_name/bin/activate
```

3. Install Seqly:

```bash
pip install /path/to/seqly.whl 
```
> Replace `/path/to/seqly.whl` with the actual path to your `.whl` file.

### Option 2: Using Conda

1. Create a new conda environment (with Python 3.8+):

```bash
conda create -n env_name #you can customize the environment name
```

2. Activate the environment:

```bash
conda activate env_name
```

3. Install Seqly via pip (inside the conda environment):

```bash
pip install /path/to/seqly.whl
```

> Even in a conda environment, `pip` is used to install the wheel.

---

## Usage

After installation, run the CLI:

```bash
seqly
```

This will start the interactive CLI where you can select input options and commands.

---