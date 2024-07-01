# WS_cosmo

Contains routines as well as computed terms for the wide-separation and relativistic corrections to the bispectrum - see ... for full details.

Wide angle, Radial redhsift and relativistic terms up to second order in each.

## quickstart

To get started see example.ipynb for a quick guide on using the computed expressions...

## mathematica_routines

The_bispectrum.nb allows for the computation of wide separation terms for some given Fourier kernels (defined in kernels.nb). 2nd order wide-separation effects can be slow to compute due to huge number of terms involved.

- kernels.nb: Defines 1st and 2nd order kernels

- expansions.nb: Defines series expansions for the wide angle and radial redshift parts

- bkfuncsandrules.nb: Contains functions used in The_bispectrum.nb (is messy and long - sorry i don't like mathematica)

- The_bispectrum.nb: Main file used in computation exports terms into .json files


Outputs are stored from mathematica in .json files in mathematica_expr - also read_mathematica.ipynb can be used for converting from mathematica to python formatting.

Terms for other kernels can also be provided or computed from the The_bispectrum.nb - format can also be flexible.

## python functions

Outputs are converted to python format and stored in bk_terms

For an example notebook for using these expressions see example.ipynb

bk_SNR.ipynb includes code to compute and plot the SNR and fisher stuff for multipoles

bk_plots.ipynb contains a bunch of functions that maybe be useful but is not clean


## Errors

Some syntax has been updated so there will be several errors lying around - particular in the bigger notebooks

## Contact

See paper - 
If youre having any problems or have any ideas to make it better-  Feel free to get in contact :) - c.l.j.addis@qmul.ac.uk