%include	/usr/lib/rpm/macros.php
%define		_class		Auth
%define 	_subclass	PrefManager
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - Preferences management class
Summary(pl):	%{_pearname} - klasa do zarz±dzania preferencjami
Name:		php-pear-%{_pearname}
Version:	1.1.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	0a0dda8e705890644c5862a6b494b4ff
URL:		http://pear.php.net/package/Auth_PrefManager/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
Requires:	php-pear-DB >= 1.3
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

This class has in PEAR status: %{_status}.

%description -l pl
Preference Manager (Zarz±dca ustawieñ) to klasa obs³uguj±ca ustawienia
u¿ytkownika w aplikacjach WWW, wyszukiwania ich w tabeli przy u¿yciu
kombinacji identyfikatora u¿ytkownika i nazwy ustawienia w celu
uzyskania warto¶ci i (opcjonalnie) zwrócenia domy¶lnej warto¶ci
ustawienia w przypadku nie znalezienia warto¶ci dla danego
u¿ytkownika. Klasa zosta³a zaprojektowana w celu u¿ywania wraz z klas±
PEAR-a Auth, ale mo¿e byæ u¿ywana z czymkolwiek, co pozwala na
uzyskanie identyfikatora u¿ytkownika - w³±cznie z w³asnym kodem.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/

# For compatibility with old class:
ln -s %{_subclass}.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/preferences.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
