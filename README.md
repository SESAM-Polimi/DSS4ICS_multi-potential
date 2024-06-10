# DSS4ICS_multi-potential

The Decision Support System for Improved Cooking Stoves (DSS4ICS) multi-potential evaluation is a tool developed in SESAM to assess the attractiveness of ICS distribution projects in sub-Saharan Africa. The assessment is performed across four potentials:
- the environmental potential, related to the fraction of non-renewable biomass available in a certain country;
- the techno-economic potential, related to the CO2 emission reduction with respect to the average baseline cookstove efficiency in the country;
- the social potential, intended as the share of population lacking access to clean cooking in the country;
- the regulatory potential, related to ESMAP's RISE indicators and reflecting the ease of doing business in the ICS sector in the country.

Moreover, the DSS4ICS allows the user to assign specific weights to the different factors, via a built-in Analytic Hierarchy Process, and to compare different countries accordingly through radar diagrams.

# Quick installation
To use DSS4ICS make sure to have installed anaconda and to follow these steps:
- install the environment using $$ conda env create -f env-dss4ics.yaml  ;
- activate the installed environment using $$ conda env activate env-dss4ics  ;
- open DSS4ICS.py and run it in spyder;
- follow the indications that appear on the console;
- to inspect the default inputs, including the updated fNRB database, you can access the default-data.xlsx file;
- to visualize the results, you can navigate them in the results-comparison folder.

The tool remains free to access and improve under the associated license.
