<h4>Lab 4/5: Assignment</h4><br>

# Comparing the USA and Australia on Census Data

## Aim

The aim of this assignment is to reveal similarities and differences between the United States and Australia, based on

* data from the _United States Census Bureau_ from 2020 or later, and
* data from _Australian Bureau of Statistics_ (ABS) 2021 Census.

You may compare the countries as a whole, or focus on a specific region or regions that you consider to be comparable in some way.

Your report should be focussed on a question that you plan to answer (or, if you prefer, an hypothesis that you seek to investigate).

It is important to understand at the outset that, while the programming is of course important, this is not a "coding exercise". Searching for appropriate data, and presenting the results in a clear and compelling way, are equally a part of the assignment.

## Learning Outcomes

This assignment demonstrates competencies in:

* sourcing information from (authoritative) public data repositories
* extracting and cleaning information needed to answer a question or hypothesis about the data
* analysing and interpreting the data
* visualising data to aid understanding and communicate results

## Practicalities

The "study buddy" system applies to this assignment. The assignment may be done individually, or in groups of up to three. Unlike the other lab sheets, however, only one "submission" is required \- that is, it needs to be in _one student's CoCalc account_ for collection at the deadline. All group members must be included in the declaration at the top of the submission.

#### Submission and Format

Your report, including all explanations and code, must be provided in the CoCalc notebook `USA_Australia.ipynb` in the directory of the same name. It should contain headings and explanations in markdown cells, and executable code in python cells.

Nothing else in the directory will be marked.

You should download a backup of your final completed submission directory.

#### Code

The code will be executed with a fresh kernel for marking, so (as usual) you should ensure that it runs with a clean kernel.

Any supporting data must be in a text files in the same directory. Data files should not be more than 1MB. (For larger downloads this may require some pre-processing of the data.)

#### Packages

The following packages, _only_, may be imported and used in this project:

Compulsory

* matplotlib/pyplot

Optional \(only for those who wish to use them, there are no marks attached to use of these\)

* csv
* numpy
* seaborn
* re

#### Deadline

The deadline is **11:59pm, Friday 9th September**.

## Rubric

The assignment contributes 15% to the 25% practical component.

The assignment will be marked for clarity and professionalism of both the exposition and the coding.

#### Context and Data \(20%\)

- Adequate context has been provided to understand the question and why it is important.
- The question \(or hypothesis\) you seek to understand is clearly stated.
- It is clear what data is used and its provenance. Instructions allow the reader to easily source the data \(to make the work replicable\). 
- Relevant differences between the data from different sources, and assumptions you have to make for comparison, are clearly described.

#### Data lifecycle, structure, and presentation (20%)

- The route from the data to the results is clearly set out and steps explained.
- It is clear what format the raw data took, what is extracted and why.
- Any data cleaning and conversion is clearly and concisely outlined. 
- The processing or analysis necessary to extract and compile the results is clearly explained.

#### Results, Visualisation and Conclusion \(20%\)

- The results are clearly stated and connected back to the original data and assumptions.
- Appropriate and informative choices are made for visualisation\(s\) \(plots\).
- The visualisations are clearly and professionally presented.
- Conclusions are connected to relevant features of the visualisations.

#### Coding \(20%\)

- Code is _clear_, easy to read and comprehend. Considerations should include:
  - use of meaningful variable names
  - use of comments and/or docstrings for key steps/blocks \(you do not need to comment every line, this tends to obscure the key steps\)
  - use of functions \(see below\)

- Code is appropriately _concise_. \(Code should not be pared down to a bare minimum at the expense of clarity and readability. However you should try to avoid extraneous code that is unnecessary.\)

- Code is reasonably _efficient_. \(It is not necessary to achieve ultimate efficiency at the expense of writing clear logical code. However you should avoid obvious unnecessary inefficiencies.\)

- Code is well _structured_. Functional decomposition is used to separate tasks into meaningful components.

#### Professionalism and Challenge \(20%\)

- Overall the report forms a compelling and illuminating narrative.
- The report is not unnecessarily long or repetitive and provides all the information in a complete but concise way.
- The report reveals aspects of the data that are not trivially obvious.
- The report is of a quality that an employer would be comfortable showing to a client.

