**"Despite the Challenges She Faces": On Disability Bias in Generative AI**

Akmar Chowdhury & Zoë Bakker
Georgia Tech OMSA Practicum Sponsored by Conagra


This repo holds the code used to create the [paper]([https://github.gatech.edu/achowdhury99/conagra_debias/blob/main/final_paper.pdf](https://github.com/zbakker/gatech-practicum/blob/main/final_paper.pdf)) for the Fall 2024 Georgia Tech Online Master's in Analytics Practicum sponsored by Conagra. 

**Data**

The data for this project is hosted in the _wikibio_ folder. It is an extract from the [WikiBio dataset](https://github.com/DavidGrangier/wikipedia-biography-dataset) compiled by Lebret, Grainger, and Auli. Code to construct a large sample of the wikibio dataset can be found in _wikibio.ipynb_ and the files needed can be found in wikibio/valid. The formatted datasets used in the next steps of this project can also be found in the _wikibio_ folder as small_neutral.csv.

**Visualizations**

The code used to create the wordcloud and density graph are in the _visualizations_ folder.

**Methodology**

A sample notebook called _demo.ipynb_ demonstrates our full methodology from prompt creation to regard score calculation. This notebook walks through the process of:
1. Taking an input prompt
2. Getting the AI response
3. Calculating the regard score as detailed in our [paper](final_paper.pdf)

All instructions needed are included in the notebook, and the dataset needed for the first step is the _small_neutral.csv_ in the _wikibio_ directory.  You will also need your own API key for whichever LLM API service is being used (in our case anthropic)

For those interested in our statistical analysis, _analysis.ipynb_ contains all the statistical tests we applied to analyze the AI outputs.

We also provide _main.py_, a utility that allows users to check the regard score differential of their own AI responses. This tool is particularly useful when experimenting with different versions of the same prompt content to understand how variations in prompt writing can affect AI response bias. Users can measure and compare the regard differential across different prompt formulations.





