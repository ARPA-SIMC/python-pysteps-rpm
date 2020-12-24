%global srcname  pysteps

%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-pysteps
Version:        1.4.0
Release:        1
Summary:        weather radar data processing

License:        BSD 3-Clause
URL:            https://pysteps.github.io/
Source0:        %pypi_source

BuildRequires:  gcc
BuildRequires:  %{python3_vers}-devel
BuildRequires:  %{python3_vers}-setuptools
BuildRequires:  %{python3_vers}-numpy
BuildRequires:  %{python3_vers}-Cython


%description
Pysteps is an open-source and community-driven Python library for probabilistic
precipitation nowcasting, i.e. short-term ensemble prediction systems.

%package     -n %{python3_vers}-pysteps
Summary:        weather radar data processing
Requires:  %{python3_vers}-numpy
Requires:  %{python3_vers}-scipy
Requires:  %{python3_vers}-matplotlib
Requires:  %{python3_vers}-h5py
Requires:  %{python3_vers}-netcdf4
Requires:  %{python3_vers}-jsonschema
Requires:  %{python3_vers}-opencv
Requires:  %{python3_vers}-pillow
Requires:  %{python3_vers}-pyproj

%description -n %{python3_vers}-pysteps
Pysteps is an open-source and community-driven Python library for probabilistic
precipitation nowcasting, i.e. short-term ensemble prediction systems.

%prep
%autosetup -n %{srcname}-%{version}

%build
%py3_build

%install
%py3_install

%check
#TODO: needs example data
#https://pysteps.readthedocs.io/en/latest/user_guide/example_data.html
#https://github.com/pySTEPS/pysteps-data
#{__python3} setup.py test

%files -n %{python3_vers}-pysteps
%{python3_sitearch}/*


%changelog
* Thu Dec 24 2020 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.4.0-1
- Introducing the thunderstorm detection and tracking (DATing) modules [#178]
- Introducing the RainFARM (Rebora et al. 2006) module for downscaling precipitation fields [#173]
- Introducing the pysteps importers plugins [#174]
- Improving the semi-lagrangian extrapolation method [#176] [#191]
- Improving pysteps netCDF exporter [#175]
- Implementing a more general importer for ODIM-compliant data sources [#171] [#172]
- Improving plotting of basemaps [#177] [#180] [#192]

* Tue Sep 01 2020 Emanuele Di Giacomo <edigiacomo@arpae.it> - 1.3.2-1.simc.20200901.gitb5aa2fe
- Custom version (waiting for https://github.com/pySTEPS/pysteps/issues/171 fix)

* Thu Jun 18 2020 Daniele Branchini <dbranchini@arpae.it> - 1.3.1-1
- Initial package
