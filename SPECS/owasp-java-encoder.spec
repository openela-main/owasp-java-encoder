Name:		owasp-java-encoder
Version:	1.2.2
Release:	3%{?dist}
Summary:	Collection of high-performance low-overhead contextual encoders

License:	BSD
URL:		https://github.com/OWASP/owasp-java-encoder/

Source0:	https://github.com/OWASP/owasp-java-encoder/archive/v%{version}.tar.gz

# add OSGi metadata
Patch0:		0_manifest.patch

BuildArch:	noarch
ExclusiveArch: x86_64

BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.sonatype.oss:oss-parent:pom:)

%description
The OWASP Encoders package is a collection of high-performance low-overhead
contextual encoders, that when utilized correctly, is an effective tool in
preventing Web Application security vulnerabilities such as
Cross-Site Scripting.

%package javadoc
Summary:  Javadoc for %{name}

%description javadoc
%{summary}.

%prep
%setup -q

%patch0 -p1

# add version number in OSGi metadata
sed -i '/^Bundle-SymbolicName: org.owasp.encoder$/a Bundle-Version: %{version}' %{_builddir}/%{name}-%{version}/META-INF/MANIFEST.MF

%pom_disable_module jsp
%pom_disable_module esapi

%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# analysis tool for testing coverage is not required
%pom_remove_plugin :cobertura-maven-plugin

%build
%mvn_build

# inject OSGi manifest
jar ufm %{_builddir}/%{name}-%{version}/core/target/encoder-%{version}.jar %{_builddir}/%{name}-%{version}/META-INF/MANIFEST.MF

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md
%license LICENSE

%changelog
* Thu Mar 04 2021 Alex Macdonald <almacdon@redhat.com> - 1.2.2-3
- Add ExclusiveArch: x86_64

* Tue May 28 2019 Jie Kang <jkang@redhat.com> -1.2.2-2
- Remove unnecessary javadoc plugin for Fedora builds

* Fri Nov 16 2018 Salman Siddiqui <sasiddiq@redhat.com> - 1.2.2-1
- Version update

* Wed Aug 08 2018 Salman Siddiqui <sasiddiq@redhat.com> - 1.2.1-1
- Initial packaging
