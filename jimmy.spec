Name:		Jimmy
Version:	1.32
Release:	1%{?dist}
Summary:	Once upon a time there was Jimmy

Group:		We no like gruppa
License:	to kill
URL:		http://blah.url
Source0:	%{name}-%{version}.tar.gz

BuildRequires:	javac
Requires:	jar

%description


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%files
%doc



%changelog

