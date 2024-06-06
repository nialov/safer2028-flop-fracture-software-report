## {{ name }}

### Info

-   Repository: <{{ url.repository }}>
-   Reference for citations: <{{ url.reference }}>
-   Discussions: <{{ url.forum }}>
-   Documentation: <{{ url.documentation }}>
-   License: {{ license }}
-   Interface: {{ interface }}

Authors:

{% for author in authors %}
-   {{ author }}
{% endfor %}

### Capabilities

{{ capabilities.based_on_documentation }}

### Data 

#### Input data

{{ input_data }}

#### Outputs

{{ outputs }}

### Documentation

#### Installation

{{ state_of_documentation.installation }}

#### Usage

{{ state_of_documentation.usage }}

#### Examples

{{ state_of_documentation.examples }}

### Remarks

{{ remarks }}
