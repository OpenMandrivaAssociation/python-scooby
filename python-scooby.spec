%define module scooby
%bcond tests 1

Name:		python-scooby
Summary:	A Python lightweight environment detective
Version:	0.11.0
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/banesullivan/scooby
Source0:	https://github.com/banesullivan/scooby/archive/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:		noarch
BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with tests}
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(beautifulsoup4)
%endif
# extra
Recommends:		python%{pyver}dist(psutil)

%description
This is a lightweight tool for easily reporting your Python environment's
package versions and hardware resources.

%prep
%autosetup -n %{module}-%{version} -p1
# Remove bundled egg-info
rm -rf %{module}.egg-info
# omit linters from tests
sed -r -i 's/^(mkl|pyvips|no_version|pytest-cov)\b/# &/' requirements_test.txt

%build
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"
%py_build

%if %{with tests}
# deselect linting tests and test_cli as we dont package python-script-runner which that test requires.
k="${k-}${k+ and }not test_get_version"
k="${k-}${k+ and }not test_tracking"
k="${k-}${k+ and }not test_import_os_error"
k="${k-}${k+ and }not test_import_time"
k="${k-}${k+ and }not test_cli"
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -k "${k-}" -v tests/
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
