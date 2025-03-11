#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	ipython_genutils
Summary:	IPython vestigial utilities
Summary(pl.UTF-8):	Pozostałe narzędzia IPythona
Name:		python-%{module}
Version:	0.2.0
Release:	11
License:	BSD
Group:		Libraries/Python
#Source0Download: https://github.com/ipython/ipython_genutils/releases
# TODO:		https://github.com/ipython/ipython_genutils/archive/%{version}/%{module}-%{version}.tar.gz
Source0:	https://github.com/ipython/ipython_genutils/archive/%{version}.tar.gz
# Source0-md5:	477e596a0e6e2f74ec08ec09687eeb6c
URL:		https://github.com/ipython/ipython_genutils
%if %(locale -a | grep -q '^C\.utf8$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package shouldn't exist. It contains some common utilities shared
by Jupyter and IPython projects during The Big Split(TM). As soon as
possible, those packages will remove their dependency on this.

%description -l pl.UTF-8
Ten pakiet nie powinien istnieć. Zawiera kilka wspólnych narzędzi
współdzielonych przez projekty Jupyter i IPython podczas Wielkiego
Podziału(TM). Projekty te będą miały usuniętą tę zależność w
najbliższym możliwym czasie.

%package -n python3-%{module}
Summary:	IPython vestigial utilities
Summary(pl.UTF-8):	Pozostałe narzędzia IPythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.3

%description -n python3-%{module}
This package shouldn't exist. It contains some common utilities shared
by Jupyter and IPython projects during The Big Split(TM). As soon as
possible, those packages will remove their dependency on this and this
package will go away.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet nie powinien istnieć. Zawiera kilka wspólnych narzędzi
współdzielonych przez projekty Jupyter i IPython podczas Wielkiego
Podziału(TM). Projekty te będą miały usuniętą tę zależność w
najbliższym możliwym czasie, a ten pakiet przestanie istnieć.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
LC_ALL=C.UTF-8 \
nosetests-%{py_ver} ipython_genutils
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} ipython_genutils
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/ipython_genutils/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/ipython_genutils/tests
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc COPYING.md README.md
%{py_sitescriptdir}/ipython_genutils
%{py_sitescriptdir}/ipython_genutils-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc COPYING.md README.md
%{py3_sitescriptdir}/ipython_genutils
%{py3_sitescriptdir}/ipython_genutils-%{version}-py*.egg-info
%endif
