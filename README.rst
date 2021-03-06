What is Varapp ?
----------------

Varapp is an application to filter genetic variants, with a reactive graphical user interface.

The application has been developed in a collaboration between the
Swiss Institute of Bioinformatics (SIB) and the Lausanne University hospital (CHUV).

The complete documentation is available at
`https://varapp-demo.vital-it.ch/docs/ <https://varapp-demo.vital-it.ch/docs/>`_ .

.. figure:: /resources/img/main-border.png
   :width:  100%
   :alt: [Main window]

Motivation
..........

Common filtering pipelines can be very tedious, including an annotation step,
complicated forms, multiple exports to spreadsheets, merging and manual curation
of theses spreadsheets.
Although there already exist several tools to facilitate the annotation of lists of variants
and apply basic filters such as frequency in a population, quality or location,
Varapp has at least one of the following advantages over existing software:

*   **Security**: It does not require to upload data to a cloud or external client;
    one can deploy the app on any local computer and keep the data private.

*   **Fast, non-trivial filtering** based on family pedigree, including complex cases
    such as compound heterozygous, in less than a second for 500K variants.

*   **Reproducibility**: It uses a relational database, adding the potential to cross information
    between experiments, reuse the results of previously studied data,
    and keep track of the annotation/versions used to produce the results.

*   **Reactive user interface**: apply a filter and see the result immediately.

Use cases
.........

Varapp is typically well-suited to cover the following two use cases,
the result of which is obtained within a few seconds:

*   **Mendelian diseases**

    We consider all variants in the exomes of one or several families
    affected by the same hereditary disease. We are searching for the variants
    that are susceptible to cause the disease.

    Varapp provides one-click filters for dominant, recessive, de novo, X-linked,
    and compound heterozygous cases.

*   **Gene panels**

    We consider the same few genes (typically a few hundred) 
    in a large series of independent individuals. We seek rare variants with
    strong impact, then inspect the individual(s) that carry them.

What Varapp is not
..................

*   ... a variants caller:

    It starts after the variant calling has already been done, 
    and works based on the VCF file that the latter produces.

*   ... adapted to full genome sequencing or million genomes projects:

    For the moment, the app is responsive with datasets up to 500'000 variants
    and a few hundred individuals,
    but performance issues are expected when dealing with millions of variants,
    as in the case of full genome sequencing, or with thousands of samples.


How can I try it?
-----------------

One demo version of the program is available at `https://varapp-demo.vital-it.ch <https://varapp-demo.vital-it.ch>`_ .
Log in as user "test" with password "test".
You will be granted access to a variants database "demo".

Try the following standard filters:

- Recessive scenario
- 1% frequencies in 1000 Genomes, ESP and EXAC
- Quality filter: PASS (VQSR)
- HIGH/MED impact

You should retrieve a single variant on gene TBC1D7 that has been published
in `Hum Mutat. 2014 Apr;35(4):447-51 <http://www.ncbi.nlm.nih.gov/pubmed/24515783>`_.

.. note::

    Prior to making it public, this dataset has been anonymized and obfuscated.
    Parents variant data was generated by random shuffling variants from several
    independent exome datasets. Children variant data was derived from the
    shuffled parents data. The TBC1D7 pathogenic variant was then added
    following recessive pattern of inheritance.

.. note::

    This version runs on minimal hardware, thus its performance is not comparable
    to a real production setup.
