import os
import re
def getpsycopgenv(options,buildout):
    os.environ['LIBS'] = os.environ['LDFLAGS']
def libxml(options, buildout, version):
    """Patch Makefile to point to our site packages."""
    pwd=options['compile-directory']
    MAKEFILE = os.path.join(
        pwd,
        'Makefile'
    )
    file=open(MAKEFILE)
    lines=file.readlines()
    for i,line in enumerate(lines):
        for word in 'PY_LIB_DIR', 'PY_MOD_DIR':
            if line.startswith(word):
                lines[i] = re.sub(
                    '%s.*' % word,
                    '%s = %s' % (
                        word,
                        os.path.join(
                            buildout['buildout']['directory'],
                            'parts',
                            'site-packages-%s' % version)
                    ),
                    line
                )
    file = open(MAKEFILE,'w+')
    file.writelines(lines)
    file.close()
    os.chdir(pwd)

def make_24(options,buildout):
    """Patch Makefile to point to our site packages."""
    libxml(options, buildout, '2.4')

def make_25(options,buildout):
    """Patch Makefile to point to our site packages."""
    libxml(options, buildout, '2.5')
# vim:set ts=4 sts=4 et  :
