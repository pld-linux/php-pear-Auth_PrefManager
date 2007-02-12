%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define 	_subclass	PrefManager
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - preferences management class
Summary(pl.UTF-8):   %{_pearname} - klasa do zarządzania preferencjami
Name:		php-pear-%{_pearname}
Version:	1.1.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	b29c2f95475fbc4970e2fa2d93715ae7
URL:		http://pear.php.net/package/Auth_PrefManager/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Requires:	php-pear-DB >= 1.6.0
Provides:	php-pear-PrefManager
Obsoletes:	php-pear-PrefManager
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

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Preference Manager (Zarządca ustawień) to klasa obsługująca ustawienia
użytkownika w aplikacjach WWW, wyszukiwania ich w tabeli przy użyciu
kombinacji identyfikatora użytkownika i nazwy ustawienia w celu
uzyskania wartości i (opcjonalnie) zwrócenia domyślnej wartości
ustawienia w przypadku nie znalezienia wartości dla danego
użytkownika. Klasa została zaprojektowana w celu używania wraz z klasą
PEAR-a Auth, ale może być używana z czymkolwiek, co pozwala na
uzyskanie identyfikatora użytkownika - włącznie z własnym kodem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

# For compatibility with old class:
ln -s %{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/preferences.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php
