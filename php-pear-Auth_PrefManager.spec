%define		status		stable
%define		pearname	Auth_PrefManager
Summary:	%{pearname} - preferences management class
Summary(pl.UTF-8):	%{pearname} - klasa do zarządzania preferencjami
Name:		php-pear-%{pearname}
Version:	1.2.2
Release:	1
License:	PHP 3.01
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	77055fdd23539d68f52166c273162799
URL:		http://pear.php.net/package/Auth_PrefManager/
BuildRequires:	php-pear-PEAR >= 1:1.4.0
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-DB >= 1.7.0
Requires:	php-pear-PEAR-core >= 1:1.4.0
Provides:	php-pear-PrefManager = 0.2.0
Obsoletes:	php-pear-Auth_PrefManager-tests
Obsoletes:	php-pear-PrefManager < 0.2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Preference Manager is a class to handle user preferences in a web
application, looking them up in a table using a combination of their
userid, and the preference name to get a value, and (optionally)
returning a default value for the preference if no value could be
found for that user. It is designed to be used alongside the PEAR Auth
class, but can be used with anything that allows you to obtain the
user's id - including your own code.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Preference Manager (Zarządca ustawień) to klasa obsługująca ustawienia
użytkownika w aplikacjach WWW, wyszukiwania ich w tabeli przy użyciu
kombinacji identyfikatora użytkownika i nazwy ustawienia w celu
uzyskania wartości i (opcjonalnie) zwrócenia domyślnej wartości
ustawienia w przypadku nie znalezienia wartości dla danego
użytkownika. Klasa została zaprojektowana w celu używania wraz z klasą
PEAR-a Auth, ale może być używana z czymkolwiek, co pozwala na
uzyskanie identyfikatora użytkownika - włącznie z własnym kodem.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv .%{php_pear_dir}/data/Auth_PrefManager/README .

mv .%{php_pear_dir}/docs .
install -d examples
mv docs/PM_Example.php examples

rm -rf .%{php_pear_dir}/data/Auth_PrefManager/tests

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# For compatibility with old class:
ln -s PrefManager.php $RPM_BUILD_ROOT%{php_pear_dir}/Auth/preferences.php

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc README
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Auth/PrefManager.php
%{php_pear_dir}/Auth/preferences.php
%{_examplesdir}/%{name}-%{version}
