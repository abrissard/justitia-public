# JustitIA

![img](resources/WelcomePage.png)

## Project Layout

- `src/` stuff around processing our dataset and constructing embeddings
- `api/` a flask app serving as our backend
- `web/` a NextJS app for the frontend

## Usage

### Environment Setup

In the `api/` directory, rename `.env.example` to `.env`. Edit this file and
fill in the placeholder values with valid credentials for OpenAI and Pinecone.

Install `npm`, `python 3.11`, and [`pipenv`](https://pipenv.pypa.io/en/latest/).

### Running a local version

Open two terminal windows. In the first, run:

```bash
cd api
pipenv install --dev # (skip this line after the first time)
pipenv run python3 main.py
```

In the second, run:

```bash
cd web
npm install # (skip this line after the first time)
npm run dev
```

In the second window, a URL will be printed. Probably `http://localhost:3000`.
Paste this into your browser to see the app.

--------------------------------------------------------------------------------

This repository was forked from https://github.com/FraserLee/AlignmentSearch/.

We thank the EA McGill team for their original implementation and the technical help they provided. 
