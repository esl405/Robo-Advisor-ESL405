# Robo-Advisor-ESL405
Robo Advisor Project

This is based on the README.md from Professor Rossetti (https://github.com/prof-rossetti/nyu-info-2335-201905/tree/master/projects/robo-advisor)

Issues requests to the [AlphaVantage Stock Market API](https://www.alphavantage.co/) in order to provide automated stock or cryptocurrency trading recommendations.

## Prerequisites

  + Anaconda 3.7
  + Python 3.7
  + Pip

## Installation

> NOTE: subsequent usage and testing commands assume you are running them from the repository's root directory.

Use Anaconda to create and activate a new virtual environment, perhaps called "stocks-env":

```sh
conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```
or 
```sh
pip install requests
pip install panadas
pip install datetime
```
## Setup

Before using or developing this application, take a moment to [obtain an AlphaVantage API Key](https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API Key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API Key:

    ALPHAVANTAGE_API_KEY="abc123"

Recplace "abc123" with your API advantage key

## Usage

Run the recommendation script:

```py
python app/robo_advisor-ESL405.py
```

## [License](/LICENSE.md)
