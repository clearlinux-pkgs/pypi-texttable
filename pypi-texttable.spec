#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-texttable
Version  : 1.6.4
Release  : 25
URL      : https://files.pythonhosted.org/packages/d5/78/dbc2a5eab57a01fedaf975f2c16f04e76f09336dbeadb9994258aa0a2b1a/texttable-1.6.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/d5/78/dbc2a5eab57a01fedaf975f2c16f04e76f09336dbeadb9994258aa0a2b1a/texttable-1.6.4.tar.gz
Summary  : module for creating simple ASCII tables
Group    : Development/Tools
License  : MIT
Requires: pypi-texttable-license = %{version}-%{release}
Requires: pypi-texttable-python = %{version}-%{release}
Requires: pypi-texttable-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
# texttable
Python module for creating simple ASCII tables
## Availability
This module is available on [PyPI](https://pypi.org/project/texttable/), and has been packaged for several Linux/Unix platforms
([Debian](https://packages.debian.org/search?&searchon=names&keywords=python-texttable+),
[FreeBSD](https://www.freebsd.org/cgi/ports.cgi?query=texttable&stype=all), Fedora, Suse...).

%package license
Summary: license components for the pypi-texttable package.
Group: Default

%description license
license components for the pypi-texttable package.


%package python
Summary: python components for the pypi-texttable package.
Group: Default
Requires: pypi-texttable-python3 = %{version}-%{release}

%description python
python components for the pypi-texttable package.


%package python3
Summary: python3 components for the pypi-texttable package.
Group: Default
Requires: python3-core
Provides: pypi(texttable)

%description python3
python3 components for the pypi-texttable package.


%prep
%setup -q -n texttable-1.6.4
cd %{_builddir}/texttable-1.6.4
pushd ..
cp -a texttable-1.6.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656368851
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-texttable
cp %{_builddir}/texttable-1.6.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-texttable/9462bef0996c5adf3697a1cb5fff34a43f40edaa
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-texttable/9462bef0996c5adf3697a1cb5fff34a43f40edaa

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
