# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Repeatmasker(Package):
    """RepeatMasker is a program that screens DNA sequences for interspersed
       repeats and low complexity DNA sequences."""

    homepage = "http://www.repeatmasker.org"
    url      = "http://www.repeatmasker.org/RepeatMasker-open-4-0-7.tar.gz"

    version('4.0.9', sha256='8d67415d89ed301670b7632ea411f794c6e30d8ed0f007a726c4b0a39c8638e5')
    version('4.0.7', '4dcbd7c88c5343e02d819f4b3e6527c6')

    variant('crossmatch', description='Enable CrossMatch search engine',
            default=False)

    depends_on('perl', type=('build', 'run'))
    depends_on('perl-text-soundex', type=('build', 'run'))
    depends_on('hmmer')
    depends_on('ncbi-rmblastn')
    depends_on('trf')

    depends_on('phrap-crossmatch-swat', type=('build', 'run'),
               when='+crossmatch')

    def url_for_version(self, version):
        url = 'http://www.repeatmasker.org/RepeatMasker-open-{0}.tar.gz'
        return url.format(version.dashed)

    def install(self, spec, prefix):
        # Config questions consist of:
        #
        # <PRESS ENTER TO CONTINUE>
        # Enter perl path
        # Enter where repeatmasker is being configured from
        # Enter trf path
        # Add a Search Engine:
        #    1. CrossMatch
        #    2. RMBlast - NCBI Blast with RepeatMasker extensions
        #    3. WUBlast/ABBlast (required by DupMasker)
        #    4. HMMER3.1 & DFAM
        #    5. Done
        # Enter RMBlast path
        # Do you want RMBlast to be your default search engine for
        #    Repeatmasker? (Y/N)
        # Add a Search Engine: Done

        config_answers = []

        if spec.satisfies('@4.0.9:'):
            # 4.0.9 removes a bunch of the interactive options
            config_answers.append('')
        else:
            config_answers.extend(['',
                                   self.spec['perl'].command.path,
                                   self.stage.source_path,
                                   self.spec['trf'].prefix.bin.trf])

        # add crossmatch search
        if '+crossmatch' in spec:
            crossmatch = self.spec['phrap-crossmatch-swat'].prefix.bin
            config_answers.extend(['1', crossmatch, 'N'])

        # set default BLAST search
        config_answers.extend(['2',
                               self.spec['ncbi-rmblastn'].prefix.bin,
                               'Y'])

        # end configuration
        config_answers.append('5')

        config_answers_filename = 'spack-config.in'

        with open(config_answers_filename, 'w') as f:
            f.write('\n'.join(config_answers))

        with open(config_answers_filename, 'r') as f:
            perl = which('perl')
            perl('configure', input=f)

        install_tree('.', prefix.bin)
