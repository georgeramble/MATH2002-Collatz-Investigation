# Collatz Investigation

## Overview

This is the project output component for the 25/26 MATH2002 coursework. The project explores the behaviour of the Collatz sequence through four separate “mini” investigations.

Some content overlaps with the written report, but the mathematics has been explored further here through computational experiments.

This file provides the marker with essential information on how the project is structured and how to navigate it.

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

#### `section2.py` - Further analysis of Structure

#### `section3.py` - Variants of the Collatz Rule

Explores how the sequence changes behaviour when we modify the rule of the Collatz sequence.

We examine two different variant and compare the results with the standard rule. We do this by comparing:

- if the sequences eventually reach 1
- how long the sequences are
- maximum excursion comparisons

#### `section4.py` - Collatz Tree

Creates the Collatz Tree by reverse engineering the standard Collatz sequence from 1.

This section investigates:

- how the tree grows by level
- how nodes branch  
- how values spread across levels  

---

## How to Run

The project has been structured so that, provided all files in the repository are accessible, there is no strict need to run the code.

The PDF submission contains the outputs from the investigations presented in the Jupyter notebook, which can be read and followed independently.

Additionally, plots for each section are already saved in the `figures/` folder, so results can be viewed without running the code.

However, if required, each section can be run independently to reproduce the results and view the full outputs. For example:

```bash
python section1.py
```

---

## Contributions

Below lists the group contributions for this part of the project.

- Jupyter Notebook: Luke & George
- Section 1 (Standard Behaviour): Luke & George
- Section 2 (Further Sequence Analysis): Luke
- Section 3 (Variants of the Collatz Rule): Yu & George
- Section 4 (Collatz Tree): George

Other group members had greater contribution to the seperate project report.