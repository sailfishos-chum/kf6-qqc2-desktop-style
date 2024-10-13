Name:    kf6-qqc2-desktop-style
Version: 6.6.0
Release: 0%{?dist}
Summary: QtQuickControls2 desktop style

License: CC0-1.0 and GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-3.0-only AND (GPL-2.0-only OR GPL-3.0-only) AND (LGPL-2.1-only OR LGPL-3.0-only)
URL:     https://invent.kde.org/plasma/%{name}

Source0:    %{name}-%{version}.tar.bz2

## upstream patches

BuildRequires: cmake
BuildRequires: clang
BuildRequires: kf6-extra-cmake-modules
BuildRequires: kf6-rpm-macros

BuildRequires: kf6-kcolorscheme-devel
BuildRequires: kf6-kconfig-devel
BuildRequires: kf6-kcoreaddons-devel
BuildRequires: kf6-kguiaddons-devel
BuildRequires: kf6-kiconthemes-devel
BuildRequires: kf6-kirigami-devel

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel

Requires:       kf6-sonnet

%description
This is a pure Qt Quick/Kirigami Qt Quick Controls style.

%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install

%files
%doc README.md
%license LICENSES/*.txt
%{_kf6_libdir}/cmake/KF6QQC2DesktopStyle/
%{_qt6_qmldir}/org/kde/desktop/
%{_qt6_qmldir}/org/kde/qqc2desktopstyle/
%{_kf6_plugindir}/kirigami/platform/org.kde.desktop.so
%{_kf6_datadir}/locale/


