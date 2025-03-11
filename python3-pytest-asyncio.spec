#
# Conditional build:
%bcond_without	tests	# unit tests

Summary:	Pytest support for asyncio
Summary(pl.UTF-8):	Wsparcie do asyncio dla Pytesta
Name:		python3-pytest-asyncio
Version:	0.19.0
Release:	3
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-asyncio/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-asyncio/pytest-asyncio-%{version}.tar.gz
# Source0-md5:	0c74a0ae2b509735594684bf00512252
URL:		https://pypi.org/project/pytest-asyncio/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools >= 1:51.0
#BuildRequires:	python3-setuptools_scm >= 6.2
BuildRequires:	python3-toml
%if %{with tests}
BuildRequires:	python3-flaky >= 3.5.0
BuildRequires:	python3-hypothesis >= 5.7.1
BuildRequires:	python3-pytest >= 6.1.0
BuildRequires:	python3-pytest-trio
%if "%{py3_ver}" == "3.7"
BuildRequires:	python3-typing_extensions >= 3.7.2
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pytest-asyncio is an Apache 2 licensed library, written in Python, for
testing asyncio code with pytest.

asyncio code is usually written in the form of coroutines, which makes
it slightly more difficult to test using normal testing tools.
pytest-asyncio provides useful fixtures and markers to make testing
easier.

%description -l pl.UTF-8
pytest-asyncio to wydana na licencji Apache 2 biblioteka, napisana w
Pythonie, służąca do testowania kodu asynchronicznego we/wy przy
użyciu pytesta.

Kod asyncio jest zwykle pisany w postaci korutyn, co nieco utrudnia
testowanie przy użyciu zwykłych narzędzi testowych. pytest-asyncio
dostarcza przydatne wyposażenie i znaczniki ułatwiające testowanie.

%prep
%setup -q -n pytest-asyncio-%{version}

# stub for setuptools
cat >setup.py <<EOF
from setuptools import setup
setup()
EOF

%build
%py3_build

%if %{with tests}
# test_flaky_integration failure: no expected report found
# test_legacy_mode failures: more warnings than expected
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_asyncio.plugin,pytest_trio.plugin" \
PYTHONPATH=$(pwd) \
%{__python3} -m pytest tests -k 'not test_flaky_integration and not test_legacy_mode'
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.rst README.rst
%{py3_sitescriptdir}/pytest_asyncio
%{py3_sitescriptdir}/pytest_asyncio-%{version}-py*.egg-info
