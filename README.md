# CI/CD Pipeline with GitHub Actions & Docker

A small Flask API with an automated CI/CD pipeline: every push to `main` runs tests, builds a Docker image, and pushes it to Docker Hub.

## Stack
- Python 3.11 / Flask
- Docker (multi-stage build)
- GitHub Actions
- Pytest

## Run locally
```bash
pip install -r requirements.txt
python app.py
# visit http://localhost:5000/health
```

## Run tests
```bash
pytest
```

## Run with Docker
```bash
docker build -t ci-cd-demo .
docker run -p 5000:5000 ci-cd-demo
```

## CI/CD Pipeline
On every push to `main`, GitHub Actions:
1. Checks out the code
2. Installs dependencies
3. Runs the test suite
4. Builds a Docker image
5. Pushes the image to Docker Hub

Requires two repo secrets: `DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`.

## Author
Manojeet Mahato
