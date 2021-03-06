from setuptools import setup
import io

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.rst')

setup(
    name='nsxramlclient',
    version='2.0.8',
    packages=['nsxramlclient'],
    url='http://github.com/vmware/nsxramlclient',
    license='MIT',
    author='yfauser',
    author_email='yfauser@yahoo.de',
    maintainer='len',
    maintainer_email='len@len.ro',
    description='A "pseudo dynamic" client for the VMware NSX for vSphere API that uses a RAML file describing the API '
                'as an Input to generate the API calls. Updated to python 3.',
    long_description=long_description,
    classifiers=[
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Libraries',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.8'],
    install_requires=['pyopenssl', 'pyraml-parser>=0.1.3', 'lxml', 'requests>=2.7.0']
)
