%if 0%{?rhel} == 7
%define python3_vers python36
%else
%define python3_vers python3
%endif

Name:           python-pysteps
Version:        1.3.1
Release:        1%{?dist}
Summary:        weather radar data processing

License:        BSD 3-Clause
URL:            https://pysteps.github.io/
Source0:        https://files.pythonhosted.org/packages/source/p/pysteps/pysteps-%{version}.tar.gz

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
%autosetup -n pysteps-%{version}

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
* Thu Jun 18 2020 Daniele Branchini <dbranchini@arpae.it> - 1.3.1-1
- Initial package
