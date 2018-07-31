##############################################################################
# Copyright (c) 2013-2018, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
from spack import *


class SagaGis(AutotoolsPackage):
    """
    SAGA is a GIS for Automated Geoscientific Analyses and has been designed for an
    easy and effective implementation of spatial algorithms. It offers a comprehensive,
    growing set of geoscientific methods and provides an easily approachable user
    interface with many visualisation options
    """

    homepage = "http://saga-gis.org/"
    url      = "https://sourceforge.net/projects/saga-gis/files/SAGA%20-%205/SAGA%20-%205.0.0/saga-5.0.0.tar.gz"
#    git      = "https://git.code.sf.net/p/saga-gis/code.git"
#
#
#    version('develop', branch='master')
#    version('6.0.0', branch='release-6.0.0')
#    version('5.0.1', branch='release-5-0-1')
    version('5.0.0', '475adff7b2e05cbdf5ccabfbbca449ac')

    variant('gui',      default=True,   description='Build GUI and interactive SAGA tools')
    variant('odbc',     default=True,   description='Build with ODBC support')
    variant('triangle', default=True,   description='Build with triangle.c non free for commercial use otherwise use qhull')
    variant('libfire',  default=True,   description='Build with libfire (non free for commercial usage)')
    variant('openmp',   default=True,   description='Build with OpenMP enabled')
    variant('python',   default=False,  description='Build Python extension')

    depends_on('autoconf', type='build')
    depends_on('automake', type='build')
    depends_on('libtool',  type='build')
    depends_on('m4',       type='build')

    depends_on('wx')
    depends_on('gdal')
    depends_on('unixodbc')
    depends_on('proj')

    depends_on('qhull', when='~triangle')
    depends_on('swig', type='build', when='+python')

    def autoreconf(self, spec, prefix):
        autoreconf('--install', '--verbose', '--force')

    def configure_args(self):
        args = []
        if self.spec.satisfies('@5:'):
            if '~gui' in self.spec:
                args.append('--disable-gui')

            if '~odbc' in self.spec:
                args.append('--disable-odbc')

            if '~triangle' in self.spec:
                args.append('--disable-triangle')

            if '~libfire' in self.spec:
                args.append('--disable-libfire')

            if '~openmpi' in self.spec:
                args.append('--disable-openmp')

            if '+python' in self.spec:
                args.append('--enable-python')

        return args
