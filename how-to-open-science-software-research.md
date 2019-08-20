If you're doing some kind of computational or data-intensive research, this post describes how to make a good open-science repository about your digital experimental results. It summarizes my experience in doing such replication packages over years for my software engineering experiments.

The core idea is that, in those computational research areas, the paper itself is not enough: one needs to access to the associated data and code in order to fully understand the contribution, to verify the claims or to build upon the results. Such additional material has different names: "replication package", "laboratory package", "supplementary material", "online appendix", etc. In this post, I call them "open-science repository".

**Definition**: An open-science repository contains the data, code (or both) that is required to reproduce all the results of a published paper.

Note that, beyond reproducibility, open-science has other noble goals:

* foster comparative experiments
* enable unanticipated and serendipitous usages 
* outreach to the general public


Requirements for an open-science repository
---------------

An open-science repository must be:

* Downloadable: the data and code lies behind a single URL.
* Findable: the open-science repository must be well indexed by search engines, it must be findable when googling for it (eg, based on the paper title).
* Documented: an inventory of artifacts (files and folders) is included, the used file formats and the naming conventions are documented.
* Complete: all numbers and figures can be re-computed from the artifacts in the open-science repository
* Exercisable: the code must be executable, and does not depend on non publicly-available modules and libraries.
* Durable: the repository URL must be stable in the long term (10 years, 100 years and more).

(Points inspired from the [ACM policy](https://www.acm.org/publications/policies/artifact-review-badging) and from the [Sciclomatic project](https://www.monperrus.net/martin/sciclomatic-sharing-scientific-datasets)).

Where to host an open-science repository?
------------------------------

Recommended options:

Open-science data and code must be pushed to platforms that are dedicated to provide long-term archival:

* [Zenodo](http://zenodo.org/) by Cern
* [HAL](http://hal.archives-ouvertes.fr/) by CNRS
* [archive.org](https://archive.org/) by the Internet Archive foundation

Github is also a good option because one gets versioning, replication, and communication (issue tracker) for free. But Github does not commit to providing stable URLs and long-term archival for decades. However, there is a direct bridge between Github and Zenodo: any Github repo can be transfered to Zenodo in one click, together with being given a DOI, see [documentation](https://guides.github.com/activities/citable-code/). 

*Hence, I recommend to use Github as working repository and to upload a backup archive to Zenodo or equivalent once the project is over.*

Discouraged options:

* Create a specific web site with all files. Reason: it is very tedious to download all files one by one or to scrape a whole website. 
* Add a file on your web page: what if your web page moves (eg for your next job): will the URL disappear? worst, will the data disappear? 
* Put the data on Google Drive or Dropbox. Reason: in such cases, the open-science repository is almost never indexed, and it can easily disappear in a cleaning operation when your account gets full.

FAQ about open-science repositories
----------------------

**How big can an open-science repository be?** Completeness is more important than size. (Note that Github supports arbitrary [large repositories](https://help.github.com/articles/what-is-my-disk-quota/) -- in my group, we have one open-science repository of [8GB for example](https://github.com/Spirals-Team/defects4j-repair/))

**Should I push the raw, intermediate or final data?** Many computational results are based on a sequence of steps.

    Raw data -> Intermediate data 1 -> Intermediate data 2 -> Final data -> Table, graphics and numbers in the paper 

In this case, the best solution is to push all the data, incl. the raw data and the intermediate data. This much eases the use by future researchers: 1) they can only use the part they are interested in 2) if they find surprising or buggy data or behavior, having the data from all intermediate steps helps a lot in understanding and fixing the problem.

**What license should be put on the open-science repository?** For research code, liberal licenses (MIT, BSD) maximizes impact, GPL-like maximizes back-contributions and control. For research data, MIT/BSD work well, and [Creative Commons licenses](https://creativecommons.org/) are also appropriate (eg CC-BY-SA). 

**Should I refactor my code before publishing it?** No. Research software packages are in essence prototypes, they don't have the same quality constraints as industrial code (see the [six golden rules for writing, using and sharing research prototypes](https://www.monperrus.net/martin/rules-research-prototype)). While the code shouldn’t be industry quality, refactorings that make the code a bit more legible or less sloppy do help. 

**I have data as Excel CLS files or as Google Doc Spreadsheets? How to share them?**

One good option is to push them on an archival repo such as Zenodo.

Checklist for creating a good open-science repository
-----------------------------

Main questions:

- Downloadable: does the data and/or code lies behind a single URL?
- Complete: can all numbers and figures from the paper be re-computed from the package?
- Durable: will the repository URL last in the long term?
- Documented: is there an inventory of artifacts (files and folders) included?

Other questions:

- Does the repository contains a main file that is easily identifiable, typically a README? ([example README for a data repository](https://github.com/monperrus/misc/blob/master/README-data-repository-template.md))
- Are all file formats documented? For tabular files (CSV, TSV, Excel is the meaning of rows and columns explained?). For database dumps, is the restoration procedure documented?
- For those used artifacts that are versioned (data or code), is the used version documented? 
- For executable artifacts, is compilation and execution documented?
- For studies involving humans, are all training materials present? Documented? 
- When proprietary data/code is used, is the procedure to get the proprietary data documented?
- Is the contact point documented? Who to contact in case of questions? How to be contacted (email, issue, etc)?
- Does the README tell which paper(s) to cite if one uses the data?

Software technology for reproducible results
-----------------------------

* Container images, such as Docker images are a good option for freezing dependencies
* Virtualization images, such as VirtualBox images, are helpful to get a running environment quickly.
* The mainstream dependency management systems (Maven, PIP) are very valuable to specify the dependencies.  [Conda](https://conda.io/) is a valuable technology in that space. 
* [Jupyter Notebooks](https://jupyter.org/). Note that Jupyter is not a dependency management system, it requires to specify dependencies elsewhere (eg with pip).

Related work
---------

* [Good enough practices in scientific computing](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510)
* [Six golden rules for writing, using and sharing research prototypes](https://www.monperrus.net/martin/rules-research-prototype)
* [The Open-Science Initiative at the Empirical Software Engineering Journal](https://github.com/emsejournal/openscience/)

Discussion
--------
