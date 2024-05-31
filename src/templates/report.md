# Abstract (English)

Modelling fractures three-dimensionally (3D) is necessary for many applications
such as site characterization in nuclear waste disposal and geothermal energy
investigations. A number of software have been released for this purpose with
many focusing on discrete fracture network (DFN) -modelling as it generates
fractures where we can not empirically detect them. Depending on the use case,
such as for safety cases in nuclear waste disposal, it is important to consider
both the fit-for-purpose of the software used for modelling alongside the
availability of the software in the future. It is uncertain if proprietary,
i.e. paid software, is available far in to the future as the company behind the
software has control on its use.

For this purpose, this report provides a state of the field on free and
open-source three-dimensional fracture modelling software, with focus on
DFN-modelling. It gathers info on their documentation, installation and
practical usage. In total, this report reviews TODO software. The software vary
in terms of their focus as some are built only to serve a very specific
modelling purpose, such as `Pychan3d` for channel network modelling. Some are
more general-purpose, such as `dfnWorks` which has been applied in a variety of
contexts, including nuclear waste disposal investigations. In addition to
containing tools to generate fractures, many software also include subsequent
flow modelling capabilities and often the fracture generation is coupled with
the following modelling. 

A review such as this is useful for end-users, such as nuclear waste companies,
safety regulators or anyone interested in 3D fracture characterization as the
contents can be used to e.g. find new software for modelling and use the
software to create models for comparison to previous ones.

# Abstract (Finnish)

# Introduction

## Statement of need

Data on fractures, discontinuities of the bedrock, can be collected from scan
lines, drillcores and bedrock outcrops. This results in one-dimensional,
two-dimensional (2D) and three-dimensional (3D) data. Basic analysis of these
sorts of data is well defined. However, when the properties of the bedrock
volume where the fractures exist are of interest, it is required to create
models of the fractures. Stochastic, i.e. statistical, generation of
three-dimensional fracture networks is usually required as three-dimensional fracture
planes can not be directly observed as they are contained by the solid bedrock
volume. Furthermore, to actually model the properties of the fractured bedrock
volume that are of interest, such as fluid flow potential and contaminant
transport, three-dimensional fracture network meshes, i.e. products of
modelling, are usually required as the basis [@hyman_dfnworks_2015]. This is
especially the case for crystalline rocks, where the permeability of the matrix
is negligible in comparison to the discontinuities i.e. fractures. In
a crystalline rock scenario the importance of discrete fracture network (DFN)
models are highlighted in numerous publications and reports
[@retrock_project_treatment_2004;@geier_assessment_2012;
@hartley_discrete_2018; @fox_geological_2012; @laine_rakoverkkomallinnus_2017].

Analysis of fracture data has many existing solutions. Solutions for 2D
fracture data are mature and numerous [@ovaskainen_fractopo_2023;
@nyberg_networkgt_2018; @healy_fracpaq_2017]. However, for 3D data, and
especially 3D-modelling, the solutions exist but due to the addition of another
dimension the problem space is larger and consequently, the software are more
complex to develop and use. Furthermore, commonly used 3D analysis and
modelling solutions are proprietary, e.g. `FracMan` [@wsp_uk_ltd_fracman_2024].
Though the proprietary solutions might be fit-for-purpose, the proprietary
nature of the software, and possibly the
output file formats, causes problems in reproducing results, especially for
third-parties. When the results are used as part of e.g. safety cases for
nuclear waste disposal, this causes a possible risk in terms of future review
of the results as the software might
no longer be available, licensing issues or due to the lack of knowledge on the
specific methods the software uses for modelling [@geier_assessment_2012].
Better reproducibility and comparability between models is guaranteed by having
the software source open. However, even with open-source, the software
still must be properly documented including how to install it, how to run it
and any other details needed for reproducing results. Furthermore, the
licenses of open-source software vary with some conflicting with long-term
reproducibility of the software [@di_penta_exploratory_2010]. Furthermore,
support on the use of free software might be limited if the developers are not
available and if development of the software has stopped. Consequently, it is
critical to review the available software in terms of these criteria.
The issues related to open-source software are often related to the limited
time and resources available to the developers and lack of long-term
funding. However, this more agile nature might also result in faster
adoption of newest research knowledge whereas development in more mature
solutions might be slower.

## Agenda

This report is a review on the state of available open-source three-dimensional
fracture network modelling tools with a focus on software capable
of DFN-modelling. It is useful

a)  when considering testing or using mentioned software in site
    characterization,
b)  when considering alternatives to already used proprietary
    software,
c)  for creating comparisons between existing models,
d)  when considering the reasonableness of requirements for nuclear
    waste disposal safety cases,
e)  when researching novel implementations of the newest knowledge on fracture
    networks,
f)  and as a basis for future development efforts.

End users are e.g. nuclear waste and energy companies, safety regulators, and
other fields where fracture modelling is required such as in geothermal energy
or in bedrock groundwater resource management.

# Software

An overview of the collected metadata and information on each software is
presented in Table @tbl:software_schema_table. In the reviewed software,
varying input data options are available. Often a set of input variables, such
as length distribution variables, fracture orientation set information and
intensities can be inputted rather than directly inputting geometric fracture
data. 

{{ software_schema_table }}
: Schema of the collected information for each software. {\#tbl:software_schema_table}

Most built solutions, e.g. `dfnWorks` [@hyman_dfnworks_2015], make an
end-to-end solution where e.g. fracture generation is only one part of the
solution. This kind of approach makes further development of one part of the
software, e.g. fracture generation, more difficult as it is usually tightly
coupled to the rest of the software. Some are focused only on the singular task
of generating three-dimensional fracture geometries, such as `frackit`
[@glaser_frackit_2020].

Very few of the software solutions have graphical user interfaces (GUI) and
interaction usually demands using the command-line or writing code to run the
solution. Typical non-GUI solutions consist of configuring the model using
plain text files or actual code and then running the software using
the command-line. Plain text files can be simpler to create, as they do not
require specific programming knowledge, but configuring with actual code can
enable a higher degree of choice in running the software. The choice of
programming language for a code interface can affect the accessibility, as some
languages, such as Python, are more widely used and more easily accessible.
The software itself might be coded in one language but the interface
to run it might be implemented in another language, which is the case
for e.g. `dfnWorks` [@hyman_dfnworks_2015].

{% for section in rendered_sections %}
{{ section }}
{% endfor %}

# Discussion and disclaimer

## Applicability of the report

DFN-modelling is a critical component of site description/characterization of
nuclear waste repositories [@fox_geological_2012]. Of the reviewed software
most provide some form of DFN-modelling capability but only `dfnWorks` seems to
have demonstrated use directly in such a context at Forsmark, Sweden
[@hyman_influence_2015]. All the reviewed software provide opportunity to
compare results to established models, made by e.g. `FracMan`, and some, such as
`DFM Generator`, even provide output files that are directly readable by
`FracMan`. However, some of the software are very specialized, such as
`Pychan3d`, which is only purpose-built for the purpose of modelling channeled
flow and probably lacks functionality to model more general cases. However,
this specialization represents novel research and experimentation that might be
considered in e.g. future nuclear waste safety cases and demonstrates the
capability of new software to implement the newest knowledge on flow in
a fractured medium. The most general purpose of the reviewed software, based on
example applications, seems to be `dfnWorks` which is demonstrated by e.g.
collaboration with developers of `FracMan` in experimenting with a combined
DFN-modelling and subsequent flow modelling workflow [@gable_fracman_2022].
Altogether this review provides important context for any end-users, whether it
be a nuclear waste company, their regulator or a geothermal energy expert, with
a view into the current field of free and open-source 3D fracture modelling
landscape and especially on DFN-modelling capable software.

## Report availability

This review merely represents an outside view into the software, their state
and their associated documentation. The developers and users of these software
can provide further information on e.g. capabilities and for further info they
should be contacted. Software also always develops and consequently, the
information of this review only represents the current state of the software
and associated data at the time of release of this report.

Criteria for inclusion in this report included the software being free to use
and having source code available. Furthermore, the software had to be found,
which becomes an issue for one-off software that have been developed for e.g.
a single article and released in only e.g. appendix format. As a recommendation
for further software releases, a release of the source into a version control
website, such as *GitHub* or *Gitlab*, guarantees better discoverability by
future researchers. Due to these criteria, this review only included TODO
software. A larger sample of software would have been useful for applicability
of this report but it nonetheless fulfils the goal of demonstrating the current
quantity and state of free and open-source 3D fracture characterization software,
and in this case the state is the low number of findable software.

In an attempt to address the issues of the report contents being only a view of
the author and only reflecting the state at the time of release, the report
source text is available for inspection, corrections by e.g. software authors
and edit contributions on *GitHub*:

-  <https://github.com/nialov/safer2028-flop-fracture-software-report>.

Edits can be included in the way of issue creation or by directly modifying the
source and creating a pull requests. All contributions are welcome! Future
edits to the contents are reflected in web (HTML) format which can be accessed
following the aforementioned link.

# Acknowledgements

This report is released as part of the SAFER FLOP -project, funded by the
National Nuclear Waste Management Fund (Finland; Ydinjätehuoltorahasto) and
Geological Survey of Finland.

# References
