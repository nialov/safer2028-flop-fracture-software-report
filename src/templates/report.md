# Abstract (English)

Modelling fractures three-dimensionally (3D) is necessary for many applications,
such as site characterization in nuclear waste disposal and geothermal energy
investigations. A number of software tools have been released for this purpose, with
many focusing on discrete fracture network (DFN) modelling, as it generates
fractures where they can not be empirically detected. Depending on the use case,
such as for safety cases in nuclear waste disposal, it is important to consider
both the suitability of the software used for modelling and the future
availability of the software. It is uncertain whether proprietary,
i.e., paid software, will be available far into the future, as the company behind the
software has control over its use.

For this purpose, this report provides a state of the field for free and
open-source three-dimensional fracture modelling software, with a focus on
DFN-modelling. In total, this report reviews TODO software, and gathers information on the documentation, installation and practical usage of the software. The software tools vary
in terms of their focus, as some have only been built to serve a very specific
modelling purpose, such as `Pychan3d` for channel network modelling. Some are
more general purpose, such as `dfnWorks` which has been applied in a variety of
contexts, including nuclear waste disposal investigations. In addition to
containing tools to generate fractures, many software tools also include subsequent
flow modelling capabilities and fracture generation is often coupled with
the following modelling. 

A review such as this is useful for end-users such as nuclear waste companies,
safety regulators or anyone interested in 3D fracture characterization as the
contents can be used to, for instance, to find new software for modelling and
use the software to create models for comparison with previous ones.

# Abstract (Finnish)

# Introduction

## Statement of need

Data on fractures, i.e. bedrock discontinuities, can be collected from scan
lines, drill cores and bedrock outcrops. This results in one-dimensional,
two-dimensional (2D) and three-dimensional (3D) data. The basic analysis of these
types of data is well defined. However, when the properties of the bedrock
volume in which the fractures exist are of interest, it is necessary to create
models of the fractures. The stochastic, i.e. statistical, generation of
3D fracture networks is usually required as 3D fracture
planes cannot be directly observed, because they are contained by the solid bedrock
volume. Furthermore, 3D fracture network meshes, i.e., products of modelling, are usually required as the basis to consequently model the actual properties of the fractured bedrock
volume that are of interest, such as fluid flow potential and contaminant
transport [@hyman_dfnworks_2015]. This is
especially the case for crystalline rocks, where the permeability of the matrix
is negligible in comparison to the discontinuities, i.e., fractures. In
crystalline rock environments, the importance of discrete fracture network (DFN)
models are highlighted in numerous publications and reports
[@retrock_project_treatment_2004;@geier_assessment_2012;
@hartley_discrete_2018; @fox_geological_2012; @laine_rakoverkkomallinnus_2017].

The analysis of fracture data has many existing solutions. Solutions for 2D
fracture data are mature and numerous [@ovaskainen_fractopo_2023;
@nyberg_networkgt_2018; @healy_fracpaq_2017]. Solutions also exist for 3D data,
especially 3D-modelling, but due to the addition of another
dimension the problem space is larger and the software tools are consequently more
complex to develop and use. Furthermore, commonly used 3D analysis and
modelling solutions are proprietary, e.g. `FracMan` [@wsp_uk_ltd_fracman_2024].
Although such proprietary solutions might be fit for purpose, the proprietary
nature of the software, and possibly the
output file formats, causes problems in reproducing results, especially for
third parties. When the results are used, for example, as part of safety cases for
nuclear waste disposal, this causes a possible risk in terms of the future review
of the results as due to the software potentially no longer being available, licensing issues or a lack of knowledge of the
specific methods the software uses for modelling [@geier_assessment_2012].
Better reproducibility and comparability between models is guaranteed by having an
open software source. However, open-source software
must still be properly documented including how to install it, how to run it
and any other details needed to reproduce results. The
licenses of open-source software tools vary with some conflicting with the long-term
reproducibility of the software [@di_penta_exploratory_2010]. Furthermore,
support in the use of free software might be limited if the developers are not
available or if development of the software has stopped. Consequently, it is
critical to review the available software in terms of these criteria.
Issues concerning open-source software are often related to the limited time
and resources available to the developers and the lack of long-term funding.
However, the more agile nature of such software development might also result
in faster adoption of the latest research knowledge whereas development in more
mature solutions might be slower.

## Agenda

This report presents a review of the state of available open-source three-dimensional
fracture network modelling tools with a focus on software capable
of DFN modelling. It is useful

a)  when considering the testing or use of the mentioned software in site
    characterization,
b)  when considering alternatives to already used proprietary
    software,
c)  for making comparisons between existing models,
d)  when considering the reasonableness of requirements for nuclear
    waste disposal safety cases,
e)  when researching novel implementations of the latest knowledge on fracture
    networks, and
f)  as a basis for future development efforts.

The anticipated end users of this report include nuclear waste and energy companies, safety
regulators, and researchers in other fields where fracture modelling is required, such as in
geothermal energy or bedrock groundwater resource management.

# Software

An overview of the collected metadata and information on each software tool is
presented in Table @tbl:software_schema_table. In the reviewed software,
various options for input data are available. Often, a set of input variables, such
as length distribution variables, and information on the orientation of fracture sets and fracture
intensities can be inputted rather than directly inputting geometric fracture
data. 

{{ software_schema_table }}
: Schema of the information collected for each software tool. {\#tbl:software_schema_table}

Most built solutions, e.g. `dfnWorks` [@hyman_dfnworks_2015], provide an
end-to-end solution where fracture generation, for example, is only one part of the
solution. This type of approach makes further development of one part of the
software, e.g., fracture generation, more difficult, as it can be tightly coupled
to the rest of the software such as with `Pychan3d`  where the channel
generation is tightly coupled with subsequent modelling [@dessirier_new_2018].
Some tools are focused on the singular task of generating three-dimensional
fracture geometries, such as `frackit` [@glaser_frackit_2020].

Very few of the software solutions have graphical user interfaces (GUI)
and interaction usually demands using the command line or writing code
to run the solution. Typical non-GUI solutions consist of configuring
the model using plain text files or actual code and then running the
software using the command line. Plain text files can be simpler to
create, as they do not require specific programming knowledge, but
configuring with actual code can enable a higher degree of choice in
running the software. The choice of programming language for a code
interface can affect the accessibility, as some languages, such as
Python, are more widely used and more easily accessible. The software
itself might be coded in one language, but for the interface to run, it might
be implemented in another language, which is the case for example with
`dfnWorks` [@hyman_dfnworks_2015].

{% for section in rendered_sections %}
{{ section }}
{% endfor %}

# Discussion and disclaimer

## Applicability of the report

DFN modelling is a critical component of site description/characterization of
nuclear waste repositories [@fox_geological_2012]. Of the reviewed software solutions
most provide some form of DFN modelling capability, but only `dfnWorks` appears to
have demonstrated use directly in such a context, at Forsmark, Sweden
[@hyman_influence_2015]. Most of the reviewed software tools provide an opportunity to
compare the results with established models, made by e.g. `FracMan`, and some of them, such as
`DFM Generator`, even provide output files that are directly readable by
`FracMan`. However, some of the software tools are very specialized, such as
`Pychan3d`, which is purpose built for modelling channelled
flow and probably lacks the functionality to model more general cases. However,
this specialization reflects novel research and experimentation that might be
considered, for example, in future nuclear waste safety cases, and it demonstrates the
capability of new software to implement the latest knowledge on flow in
a fractured medium. The most general purpose of the reviewed software, based on
the example applications, appears to be `dfnWorks` which is demonstrated, for example, by
collaboration with the developers of `FracMan` in experimenting with a combined
DFN modelling and subsequent flow modelling workflow [@gable_fracman_2022].
Altogether this review provides an important context for any end user, whether it
be a nuclear waste company, their regulator or a geothermal energy expert, with
a view into the current field of free and open-source 3D fracture modelling
and especially DFN modelling -capable software.

## Report availability

This review merely presents a general view of the software tools, their state
and their associated documentation. The developers and users of the software
can provide further details, for example, on capabilities, and they should be
contacted for further information. Moreover, software always develops, and, the
information provided in this review thus only represents the current state of
the software and associated data at the time of release of this report.

Criteria for inclusion in this report included the software being free to use
and having available source code. Furthermore, the software had to be found,
which becomes an issue for one-off software that has been developed, for
example, for a single article and only released in an appendix format. As
a recommendation for further software releases, the release of the source on
a version control platform, such as *GitHub* or *Gitlab*, guarantees better
discoverability by future researchers. Due to these criteria, this review only
includes TODO software. A larger sample of software would have been useful to
further increase the applicability of this report, but it nonetheless fulfils
the goal of demonstrating the current quantity and state of free and
open-source 3D fracture characterization software. The criteria for being free
is not strict as some software have components that require proprietary
software for full use of the software. E.g. `ADFNE` requires a `Matlab` license
and `CTtoDFM` requires multiple proprietary software to fully complete the
described workflow. However, with the source freely available it is at least
theoretically possible to replicate these workflows with free software in the
future.

In an attempt to address the issues associated with the contents of this report
only being a view of the author and only reflecting the state at the time of
release, the source text of the report is available for inspection and, for
example, corrections and updates by software authors and edit
contributions on *GitHub*:

-  <https://github.com/nialov/safer2028-flop-fracture-software-report>.

Edits can be included by creating issue posts or by directly modifying the
source and creating a pull requests. All contributions are welcome! Future
edits to the contents will be reflected in web (HTML) format, which can be accessed
following the aforementioned link.

# Acknowledgements

This report has been released as part of the SAFER FLOP -project, funded by the
National Nuclear Waste Management Fund (Finland; Ydinjätehuoltorahasto) and
the Geological Survey of Finland.

# References
