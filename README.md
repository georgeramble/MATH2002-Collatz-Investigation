# Collatz Investigation

## Overview

This is the project output component for the 25/26 MATH2002 coursework. The project explores the behaviour of the Collatz sequence through four separate “mini” investigations.

Some content overlaps with the written report, but the mathematics has been explored further here through computational experiments.

This file provides the marker with essential information on how the project is structured and how to navigate it.


## How to Run

The project has been structured so that, provided all files in the repository are accessible, there is no strict need to run the code.

The PDF submission contains the outputs from the investigations presented in the Jupyter notebook, which can be read and followed independently.

Additionally, plots for each section are already saved in the `figures/` folder, so results can be viewed without running the code.

However, if required, each section can be run independently to reproduce the results and view the full outputs. For example: `python section1.py`


## Report Structure

### Jupyter Notebook:

- `collatz_notebook.ipynb`

This is the final submission for this component (submitted as a PDF). The notebook contains the explanations of the code, the results obtained, and further discussion.

### Python Files:

The Python files contain all the code used to generate results for each section of the investigation.

#### `section1.py` - Standard Behaviour

This section looks at the basic structure of the standard Collatz sequence and investigates:

- stopping times  
- maximum excursions  
- relationships between these values  

These are then plotted to show how behaviour changes as the starting value increases.

#### `section2.py` - Related Sequences

This section focuses on additional structural properties of the Collatz sequence and the sequences they produce.

For example, we will look at quantaties such as parity, record breakers, stopping time, and maximum excursion.

#### `section3.py` - Variants of the Collatz Rule

Explores how the behaviour of the sequence changes when we modify the Collatz rule.

We examine two different variants and compare the results with the standard rule. We do this by comparing:

- if the sequences eventually reach 1
- how long the sequences are
- maximum excursion comparisons

#### `section4.py` - Collatz Tree

Creates the Collatz Tree by reverse engineering the standard Collatz sequence from 1.

This section investigates:

- how the tree grows by level
- how nodes branch  
- how values spread across levels  


## Contributions

Below lists the group contributions for this part of the project.

- Jupyter Notebook: Luke & George
- Section 1 (Standard Behaviour): Luke & George
- Section 2 (Related Sequences): Luke
- Section 3 (Variants of the Collatz Rule): Yu & George
- Section 4 (Collatz Tree): George

Other group members had greater contribution to the separate project report.


## References and Useful Sources

The following sources were used to understand the Collatz sequence, related sequences, variants, parity interpretations, Collatz trees, and to support the Python implementation and project setup.

- OEIS Foundation Inc. A006370: Collatz sequence. Online Encyclopedia of Integer Sequences. https://oeis.org/A006370

- OEIS Foundation Inc. A006577: Number of steps for \(n\) to reach 1 in the \(3x+1\) problem. Online Encyclopedia of Integer Sequences. https://oeis.org/A006577

- OEIS Foundation Inc. A025586: Largest value in \(3x+1\) trajectory of \(n\). Online Encyclopedia of Integer Sequences. https://oeis.org/A025586

- Lagarias, J. C. (1985). The \(3x+1\) Problem and Its Generalizations. *The American Mathematical Monthly*, 92(1), 3–23. https://www.jstor.org/stable/2322189

- Veritasium. The Simplest Math Problem No One Can Solve. YouTube. https://www.youtube.com/watch?v=094y1Z2wpJg

- Barina, D. (2022). \(7x\pm1\): Close relative of the Collatz problem. *Computational Methods in Science and Technology*. https://cmst.eu/wp-content/uploads/files/10.12921_cmst.2022.0000025_BARINA.pdf

- Rozier, O. (2018). Parity sequences of the \(3x+1\) map on the 2-adic integers and Euclidean embedding. arXiv. https://arxiv.org/pdf/1805.00133

- RisingEntropy. The Collatz Tree. https://risingentropy.com/collatz-tree/

- Wikipedia. Collatz conjecture. https://en.wikipedia.org/wiki/Collatz_conjecture

- GitHub Docs. Getting started with Git. https://docs.github.com/en/get-started/learning-to-code/getting-started-with-git

- GitHub Docs. Adding locally hosted code to GitHub. https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github

- Python Software Foundation. `os` module documentation. https://docs.python.org/3/library/os.html

- Matplotlib documentation. `savefig` documentation. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html

- Matplotlib documentation. https://matplotlib.org/stable/


## Use of Generative AI

ChatGPT-5 (OpenAI, https://chatgpt.com/) was used to help select and organise content, support debugging, check code formatting, and help format the Jupyter notebook. All final code, figures, explanations, and written material were produced by the group.


## Final Recap

This repository contains the markdown of the final PDF alongside all the finalized code that was used to obtain the results in the project. The notebook is a write up of the main investigation, which is supported by the Python code and plots.

Thank you for taking the time to read through this project.

---