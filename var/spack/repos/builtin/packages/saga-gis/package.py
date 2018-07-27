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
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install saga-gis
#
# You can edit this file again by typing:
#
#     spack edit saga-gis
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class SagaGis(AutotoolsPackage):
    """FIXME: Put a proper description of your package here."""

    homepage = "http://saga-gis.org/"
#FIXME: Url noch nicht ausreichend für automatischen Download
#    url      = "https://sourceforge.net/projects/saga-gis/files/SAGA%20-%205/SAGA%20-%205.0.0/saga-5.0.0.tar.gz"
#    git      = "https://git.code.sf.net/p/saga-gis/code.git"
#
#
#    version('develop', branch='master')
#    version('6.0.0', branch='release-6.0.0')
#    version('5.0.1', branch='release-5-0-1')
#    version('5.0.0', '475adff7b2e05cbdf5ccabfbbca449ac')
#
#    variant('shared',   default=True,   description='Build shared libraries')
#    variant('static',   default=True,   description='Build static libraries')
##FIXME: Debug Variant notwendig?
#    #variant('debug',    default=False,  description='Turn on debugging')
#    variant('gui',      default=True,   description='Build GUI and interactive SAGA tools')
#    variant('odbc',     default=True,   description='Build with ODBC support')
#    variant('triangle', default=True,   description='Build with triangle.c (non free for commercial use); otherwise use qhull')
#    variant('libfire',  default=True,   description='Build with libfire (non free for commercial usage)')
#    variant('openmp',   default=True,   description='Build with OpenMP enabled')
#    variant('python',   default=False,  description='Build Python extension')
#
#    depends_on('autoconf', type='build')
#    depends_on('automake', type='build')
#    depends_on('libtool',  type='build')
#    depends_on('m4',       type='build')
#
#    depends_on('wx')
#    depends_on('gdal')
#    depends_on('unixodbc')
#    depends_on('proj')
#    depends_on('qhull', when='~triangle')

    def autoreconf(self, spec, prefix):
        # FIXME: Modify the autoreconf method as necessary
        autoreconf('--install', '--verbose', '--force')

#    def configure_args(self):
#        # FIXME: Add arguments other than --prefix
#        # FIXME: If not needed delete this function
#        args = []
#        if spec.satisfies('@5:'):
#            if '+shared' in spec:
#                args.append('--enable-shared=yes')
#            else:
#                args.append('--enable-shared=no')
#
#            if '+static' in spec:
#                args.append('--enable-static=yes')
#            else:
#                args.append('--enable-static=no')
#
#            if '~gui' in spec:
#                args.append('--disable-gui')
#
#            if '~odbc' in spec:
#                args.append('--disable-odbc')
#
#            if '~triangle' in spec:
#                args.append('--disable-triangle')
#
#            if '~libfire' in spec:
#                args.append('--disable-libfire')
#
#            if '~openmpi' in spec:
#                args.append('--disable-openmp')
#
#            if '+python' in spec:
#                args.append('--enable-python')
#
#        return args
