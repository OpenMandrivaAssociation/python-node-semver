%global oname node_semver

%bcond_without tests

# NOTE Upstream put this package into maintenance mode
# NOTE for more info see: https://github.com/podhmo/python-node-semver/issues/49

Name:           python-node-semver
Version:        0.9.0
Release:        1
Summary:        Python version of node-semver
License:        MIT
Group:          Development/Python
URL:            https://github.com/podhmo/python-node-semver
Source0:        https://github.com/podhmo/python-node-semver/archive/refs/tags/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
%if %{with tests}
BuildRequires:	python%{pyver}dist(pytest)
%endif

%description
This package provide Python version of node-semver.

%prep
%autosetup -n %{name}-%{version}

# Remove bundled egg-info
rm -rf %{oname}.egg-info

# Remove git badge remote images from README
sed -i '4,5d;' README.rst

%build
%py_build

%install
%py_install

%if %{with tests}
%check
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitearch}:${PWD}"
%{__python} -m pytest
%endif

%files
%{python_sitelib}/%{oname}-%{version}*-info
%{python_sitelib}/nodesemver/
%doc README.rst
%doc examples/readme.py
%license LICENSE

