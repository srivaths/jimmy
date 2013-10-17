Name:		Jimmy
Version:	1.34
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
* Thu Oct 17 2013 Sri Sankaran <sri@redhat.com> 1.34-1
- Added README to rid github nag (sri@redhat.com)

* Thu Oct 17 2013 Sri Sankaran <sri@redhat.com> 1.33-1
- new package built with tito
Here we go!


