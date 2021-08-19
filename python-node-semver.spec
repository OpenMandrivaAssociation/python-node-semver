%global pypi_name node-semver

Name:           python-%{pypi_name}
Version:        0.8.0
Release:        1
Summary:        Python version of node-semver
License:        MIT
Group:          Development/Python
URL:            https://github.com/podhmo/python-semver
Source0:        https://github.com/podhmo/python-semver/archive/refs/tags/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description
This package provide Python version of node-semver.

%prep
%autosetup -n %{pypi_name}-%{version}

# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

%files
#{python_sitelib}/patch_ng-%{version}-py*.*.egg-info
#{python_sitelib}/patch_ng.py
#{python_sitelib}/__pycache__/
