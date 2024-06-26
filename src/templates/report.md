# Cover image

![Illustration of the workflow from fracture characterization to
modelling. Focus of the report is on three-dimensional fracture, flow
and transport modelling. Two-dimensional fracture characterization
images from `fractopo` [@ovaskainen_fractopo_2023] documentation.
Three-dimensional fracture modelling images, top to bottom: `frackit`
documentation [@glaser_frackit_2020] and `ADFNE` documentation
[@fadakar_alghalandis_adfne_2017], respectively. Flow and transport
modelling images, top to bottom: `dfnWorks` documentation
[@hyman_dfnworks_2015] and `CTtoDFM` article
[@ferreira_computed-tomography-based_2023],
respectively.](src/images/report_cover.drawio.png)

# Abstract (English)

{{ abstract_english }}

# Abstract (Finnish)

{{ abstract_finnish }}

# Introduction

## Statement of need

Data on fractures, i.e. bedrock discontinuities, can be collected from
scan lines, drill cores and bedrock outcrops. This results in
one-dimensional, two-dimensional (2D) and three-dimensional (3D) data.
The basic analysis of these types of data is well defined. However, when
the properties of the fractured bedrock volume are of
interest, it is necessary to create models of the fractures. The
stochastic, i.e. statistical, generation of 3D fracture networks is
usually required as 3D fracture planes cannot be directly observed,
because they are contained by the solid bedrock volume. Furthermore, 3D
fracture network meshes, i.e., products of modelling, are usually
required as the basis to consequently model the actual properties of the
fractured bedrock volume of interest, such as fluid flow
potential and contaminant transport [@hyman_dfnworks_2015]. This is
especially the case for crystalline rocks, where the permeability of the
matrix is negligible in comparison to the discontinuities, i.e.,
fractures. In crystalline rock environments, the importance of discrete
fracture network (DFN) models is highlighted in numerous publications
and reports
[@retrock_project_treatment_2004; @geier_assessment_2012; @hartley_discrete_2018; @fox_geological_2012; @laine_rakoverkkomallinnus_2017].

The analysis of fracture data has many existing solutions. Solutions for
2D fracture data are mature and numerous
[@ovaskainen_fractopo_2023; @nyberg_networkgt_2018; @healy_fracpaq_2017].
Solutions also exist for 3D data, especially 3D-modelling, but due to
the addition of the third dimension the problem space is more extensive, and the
software programs are consequently more complex to develop and use.
Furthermore, commonly used 3D analysis and modelling solutions are
proprietary, e.g., `FracMan` [@wsp_uk_ltd_fracman_2024]. Although such
proprietary solutions might be fit for purpose, the proprietary nature
of the software, and possibly the output file formats, causes problems
in reproducing results, especially for third parties. When the results
are used, for example, as part of safety cases for nuclear waste
disposal, this causes a possible risk in terms of the future review of
the results as due to the software potentially no longer being
available, licensing issues or a lack of knowledge of the specific
methods the software uses for modelling [@geier_assessment_2012]. Better
reproducibility and comparability between models are guaranteed by having
an open software source. However, open source software must still be
properly documented including how to install it, how to run it and any
other details needed to reproduce results. The licenses of open source
software programs vary with some conflicting with the long-term
reproducibility of the software [@di_penta_exploratory_2010].
Furthermore, support in the use of free software might be limited if the
developers are not available or if development of the software has
stopped. Consequently, it is critical to review the available software
in terms of these criteria. Issues concerning open source software are
often related to the limited time and resources available to the
developers and the lack of long-term funding. However, the more agile
nature of such software development might also result in faster adoption
of the latest scientific results whereas development in more mature
solutions might be slower.

## Agenda

This report presents a review of the state of available open source
three-dimensional fracture network characterization programs with a focus on
software capable of DFN modelling. It is useful

a)  when considering the testing or use of the mentioned software in site
    characterization,
b)  when considering alternatives to already used proprietary
    software,
c)  for making comparisons between existing models,
d)  when considering the feasibility of requirements for nuclear
    waste disposal safety cases,
e)  when researching novel implementations of the latest knowledge on fracture
    networks, and
f)  as a basis for future development efforts.

The anticipated end users of this report include nuclear waste and energy
companies, safety regulators, and researchers in other fields where fracture
modelling is required, such as in geothermal energy or bedrock groundwater
resource management.

# Review criteria

An overview of the collected metadata and information on each software
program is presented in Table @tbl:software_schema_table. In the
reviewed software, various options for input data are available. Often,
a set of input variables, such as length distribution variables, and
information on the orientation of fracture sets and fracture intensities
can be inserted rather than geometric fracture data directly.

{{ software_schema_table }}
: Schema of the information collected for each software. {\#tbl:software_schema_table}

Most built solutions, e.g., `dfnWorks` [@hyman_dfnworks_2015], provide an
end-to-end solution where fracture generation, for example, is only one part of the
solution. This type of approach makes further development of one part of the
software, e.g., fracture generation, more difficult, as it can be tightly coupled
to the rest of the software such as with `Pychan3d`  where the channel
generation is tightly coupled with subsequent modelling [@dessirier_new_2018].
Some programs are only focused on the task of generating three-dimensional
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

# Software reviews

{% for section in rendered_sections %}
{{ section }}
{% endfor %}

# Discussion

## Applicability of the report

DFN modelling is a critical component of site description/characterization of
nuclear waste repositories [@fox_geological_2012]. Of the reviewed software solutions
most provide some form of DFN modelling capability, but only `dfnWorks` appears to
have demonstrated use directly in such a context, at Forsmark, Sweden
[@hyman_influence_2015]. Most of the reviewed software programs provide an opportunity to
compare the results with established models, made by e.g., `FracMan`, and some of them, such as
`DFM Generator`, even provide output files that are directly readable by
`FracMan`. However, some of the software programs are very specialized, such as
`Pychan3d`, which is designed for modelling channelled
flow and probably lacks the functionality to model more general cases. However,
this specialization reflects novel research and experimentation that might be
considered, for example, in future nuclear waste safety cases, and it demonstrates the
capability of new software to implement the latest knowledge on flow in
a fractured medium. The most versatile, and possibly mature, of the reviewed
software, based on the example applications, appears to be `dfnWorks` which is
demonstrated, for example, by collaboration with the developers of `FracMan` in
experimenting with a combined DFN modelling and subsequent flow modelling
workflow [@gable_fracman_2022]. Altogether this review provides an important
context for any end user, whether it be a nuclear waste company, their
regulator or a geothermal energy expert, with a view into the current field of
free and open source 3D fracture modelling and especially DFN modelling
-capable software.

## Report availability

This review presents a general view of the software programs, their state
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
includes seven software. A larger sample of software would have been useful to
further increase the applicability of this report, but it nonetheless fulfils
the goal of demonstrating the current quantity and state of free and
open source 3D fracture characterization software. The criteria for being free
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
source and creating a pull request. All contributions are welcome. Future
edits to the contents will be reflected in web (HTML) format, which can be
accessed following the aforementioned link.

# Acknowledgements

This report has been released as part of the SAFER FLOP -project, funded by the
National Nuclear Waste Management Fund (Finland; Ydinjätehuoltorahasto) and the
Geological Survey of Finland. Thanks to Jon Engström and Nicklas Nordbäck for
reviews, Roy Siddall and Marja Muittari for English and Finnish language
checks, respectively and thanks to Päivi Kuikka-Niemi for editorial handling of
this publication at the GTK.

# References
