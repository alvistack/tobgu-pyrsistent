# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-pyrsistent
Epoch: 100
Version: 0.18.1
Release: 1%{?dist}
Summary: Persistent or Functional or Immutable data structures
License: MIT
URL: https://github.com/tobgu/pyrsistent/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: gcc
BuildRequires: python-rpm-macros
BuildRequires: python3-cython
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-pyrsistent
Summary: Persistent or Functional or Immutable data structures
Requires: python3
Provides: python3-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python3dist(pyrsistent) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyrsistent) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyrsistent) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-pyrsistent
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

%files -n python%{python3_version_nodots}-pyrsistent
%license LICENSE.mit
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-pyrsistent
Summary: Persistent or Functional or Immutable data structures
Requires: python3
Provides: python3-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python3dist(pyrsistent) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyrsistent) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyrsistent) = %{epoch}:%{version}-%{release}

%description -n python3-pyrsistent
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

%files -n python3-pyrsistent
%license LICENSE.mit
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-pyrsistent
Summary: Persistent or Functional or Immutable data structures
Requires: python3
Provides: python3-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python3dist(pyrsistent) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(pyrsistent) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-pyrsistent = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(pyrsistent) = %{epoch}:%{version}-%{release}

%description -n python3-pyrsistent
Pyrsistent is a number of persistent collections (by some referred to as
functional data structures). Persistent in the sense that they are
immutable.

%files -n python3-pyrsistent
%license LICENSE.mit
%{python3_sitearch}/*
%endif

%changelog
