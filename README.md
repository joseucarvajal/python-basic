# Technical instructions

## Create and activate Python virtual environment
```bash
    python3 -m venv venv
    source venv/bin/activate
```

## Install dependencies
Create file *requirements.txt*

```bash
    pip3 install -r requirements.txt
```

## Run streamlit project

```bash
    streamlit run app/app.py 
```


# Utilities
## Steps to remove virtual environment
```bash
    deactivate
    rm -rf venv
```