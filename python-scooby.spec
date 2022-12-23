Summary:	A Python lightweight environment detective
Name:		python-scooby
Version:	0.7.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/banesullivan/scooby
Source0:	https://pypi.io/packages/source/s/scooby/scooby-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(wheel)

# extra
Suggests:	python3dist(psutil)

BuildArch:	noarch

%files
%license LICENSE
%doc README.md
%{_bindir}/scooby
%{py_sitedir}/scooby/
%{py_sitedir}/scooby*-info/

#----------------------------------------------------------------------------

%description
This is a lightweight tool for easily reporting your Python environment's
package versions and hardware resources.

%prep
%autosetup -n scooby-%{version}

%build
%py_build

%install
%py_install

