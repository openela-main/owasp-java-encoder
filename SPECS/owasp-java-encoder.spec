Name:		owasp-java-encoder
Version:	1.2.2
Release:	6%{?dist}
Summary:	Collection of high-performance low-overhead contextual encoders

License:	BSD
URL:		https://github.com/OWASP/owasp-java-encoder/

Source0:	https://github.com/OWASP/owasp-java-encoder/archive/v%{version}.tar.gz

# package as a bundle instead of a jar
Patch0:		0_bundle-packaging.patch
# source/target option of 1.5 not compatible with maven-compiler-plugin 3.8.1 >= in f33
Patch1:		1_update-compiler-plugin-version.patch

BuildArch:	noarch

BuildRequires:	maven-local
BuildRequires:	mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:	mvn(org.apache.felix:maven-bundle-plugin)

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
%patch1 -p1

%pom_disable_module jsp
%pom_disable_module esapi

%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin

# analysis tool for testing coverage is not required
%pom_remove_plugin :cobertura-maven-plugin

%pom_remove_parent

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc README.md
%license LICENSE

%changelog
* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1.2.2-6
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Sep 21 2020 Jie Kang <jkang@redhat.com> - 1.2.2-4
- Remove deprecated dependency: sonatype-oss-parent

* Tue Aug 18 2020 Alex Macdonald <almacdon@redhat.com> - 1.2.2-3
- Remove osgi metadata patch0 that previously added a manifest
- Include patch (courtesy of jkang) to package as a bundle instead of a jar
- Update maven-compiler-plugin source/target version for builds in f33

* Tue May 28 2019 Jie Kang <jkang@redhat.com> -1.2.2-2
- Remove unnecessary javadoc plugin for Fedora builds

* Fri Nov 16 2018 Salman Siddiqui <sasiddiq@redhat.com> - 1.2.2-1
- Version update

* Wed Aug 08 2018 Salman Siddiqui <sasiddiq@redhat.com> - 1.2.1-1
- Initial packaging
