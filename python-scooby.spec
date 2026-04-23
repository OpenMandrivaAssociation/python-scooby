%define module scooby
%bcond tests 1

Name:		python-scooby
Summary:	A Python lightweight environment detective
Version:	0.11.2
Release:	1
Group:		Development/Python
License:	MIT
URL:		https://github.com/banesullivan/scooby
Source0:	https://github.com/banesullivan/scooby/archive/v%{version}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildArch:		noarch
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(psutil)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	tomcli
%if %{with tests}
BuildRequires:	python-numpy-f2py
BuildRequires:	python%{pyver}dist(beautifulsoup4)
BuildRequires:	python%{pyver}dist(numpy)
BuildRequires:	python%{pyver}dist(pytest)
BuildRequires:	python%{pyver}dist(pytest-console-scripts)
BuildRequires:	python%{pyver}dist(scipy)
BuildRequires:	time
%endif
# extra
Recommends:		python%{pyver}dist(psutil)

%description
This is a lightweight tool for easily reporting your Python environment's
package versions and hardware resources.

%prep -a
# omit linters from tests
tomcli set pyproject.toml lists delitem 'dependency-groups.test' \
    '(mkl|pyvips|no-version|pytest-cov)\b.*'

%build -p
export SETUPTOOLS_SCM_PRETEND_VERSION="%{version}"

%if %{with tests}
%check
# deselect linting tests as we dont package python-script-runner which that test requires.
skiptests+="not test_get_version"
skiptests+=" and not test_tracking"
skiptests+=" and not test_import_os_error"
skiptests+=" and not test_import_time"
export CI=true
export PYTHONPATH="%{buildroot}%{python_sitelib}:${PWD}"
pytest -k "$skiptests"
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{module}
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info
