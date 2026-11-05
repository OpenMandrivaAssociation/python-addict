Name:		python-addict
Version:	2.4.0
Release:	1
Summary:	Dictionary with attribute access
License:	MIT
Group:		Development/Python
URL:		https://github.com/mewwts/addict
Source0:	https://files.pythonhosted.org/packages/85/ef/fd7649da8af11d93979831e8f1f8097e85e82d5bfeabc8c68b39175d8e75/addict-%{version}.tar.gz
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)

%description
A dictionary subclass whose keys can be read and written as attributes.
misaki uses it for token metadata.

%files
%doc README.md
%license LICENSE
%{py_sitedir}/addict
%{py_sitedir}/addict-*.egg-info
