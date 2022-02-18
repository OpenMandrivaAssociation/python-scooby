%define module	scooby

Summary:	A Python lightweight environment detective
Name:		python-%{module}
Version:	0.5.11
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/banesullivan/scooby
Source0:	https://pypi.io/packages/source/s/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)

# extra
Suggests:	python3dist(psutil)

BuildArch:	noarch

%files
%license LICENSE
%doc README.md
%{py_sitedir}/%{module}/
%{py_sitedir}/%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%description
This is a lightweight tool for easily reporting your Python environment's
package versions and hardware resources.

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

