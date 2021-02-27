#
# Conditional build:
%bcond_with	tests	# unit tests (not included in release package)

Summary:	Pytest support for asyncio
Summary(pl.UTF-8):	Wsparcie do asyncio dla Pytesta
Name:		python3-pytest-asyncio
Version:	0.14.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-asyncio/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-asyncio/pytest-asyncio-%{version}.tar.gz
# Source0-md5:	b63593bc08f445f6e3f14c34128a68ed
URL:		https://pypi.org/project/pytest-asyncio/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
%if %{with tests}
%if "%{py3_ver}" < "3.6"
BuildRequires:	python3-async_generator >= 1.3
%endif
BuildRequires:	python3-hypothesis >= 5.7.1
BuildRequires:	python3-pytest >= 5.4.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.5
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

%build
%py3_build

%if %{with tests}
%{__python3} -m pytest ...
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/pytest_asyncio
%{py3_sitescriptdir}/pytest_asyncio-%{version}-py*.egg-info
