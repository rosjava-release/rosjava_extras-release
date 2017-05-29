Name:           ros-kinetic-rosjava-extras
Version:        0.3.2
Release:        0%{?dist}
Summary:        ROS rosjava_extras package

Group:          Development/Libraries
License:        Apache 2.0
URL:            http://ros.org/wiki/rosjava_extras
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-rosjava-bootstrap
Requires:       ros-kinetic-rosjava-build-tools
Requires:       ros-kinetic-rosjava-core
Requires:       ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-rosjava-bootstrap
BuildRequires:  ros-kinetic-rosjava-build-tools
BuildRequires:  ros-kinetic-rosjava-core
BuildRequires:  ros-kinetic-sensor-msgs

%description
Extra packages for rosjava_core

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Mon May 29 2017 Daniel Stonier <d.stonier@gmail.com> - 0.3.2-0
- Autogenerated by Bloom

* Wed Feb 22 2017 Daniel Stonier <d.stonier@gmail.com> - 0.3.1-0
- Autogenerated by Bloom

* Sun Dec 25 2016 Daniel Stonier <d.stonier@gmail.com> - 0.3.0-0
- Autogenerated by Bloom

