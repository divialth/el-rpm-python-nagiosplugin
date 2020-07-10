# Created by pyp2rpm-3.3.4
%global pypi_name nagiosplugin

Name:           python-%{pypi_name}
Version:        1.3.2
Release:        1%{?dist}
Summary:        Class library for writing Nagios (Icinga) plugins

License:        ZPL-2.1
URL:            https://nagiosplugin.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-sphinx

%description
The nagiosplugin library About **nagiosplugin** is a Python class library which
helps writing Nagios (or Icinga) compatible plugins easily in Python. It cares
for much of the boilerplate code and default logic commonly found in Nagios
checks, including:- Nagios 3 Plugin API compliant parameters and output
formatting - Full Nagios range syntax support - Automatic threshold checking -
Multiple...

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        Class library for writing Nagios (Icinga) plugins

%description -n python%{python3_pkgversion}-%{pypi_name}
The nagiosplugin library About **nagiosplugin** is a Python class library which
helps writing Nagios (or Icinga) compatible plugins easily in Python. It cares
for much of the boilerplate code and default logic commonly found in Nagios
checks, including:- Nagios 3 Plugin API compliant parameters and output
formatting - Full Nagios range syntax support - Automatic threshold checking -
Multiple...

%package -n python-%{pypi_name}-doc
Summary:        nagiosplugin documentation
%description -n python-%{pypi_name}-doc
Documentation for nagiosplugin

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%{__python3} setup.py build
# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 doc html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%{__python3} setup.py install --skip-build --root %{buildroot}

%check
%{__python3} setup.py test

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.txt doc/readme.rst
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE.txt

%changelog
* Fri Jul 10 2020 divialth <65872926+divialth@users.noreply.github.com> 1.3.2-1
- Initial package.
