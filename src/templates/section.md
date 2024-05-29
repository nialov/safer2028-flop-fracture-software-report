## {{ name }}

### Info

-   Repository: <{{ url.repository }}>
-   Reference for e.g. citations: <{{ url.reference }}>
-   Discussions: <{{ url.forum }}>
-   Documentation: <{{ url.documentation }}>
-   License: {{ license }}
-   Interface: {{ interface }}

Authors:

{% for author in authors %}
-   {{ author }}
{% endfor %}

### Data 

{{ input_data }}

{{ outputs }}

### Documentation

{{ state_of_documentation.installation }}

{{ state_of_documentation.usage }}

{{ state_of_documentation.examples }}

### Capabilities

{{ capabilities.based_on_documentation }}

### Remarks

{{ remarks }}
