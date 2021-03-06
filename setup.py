from setuptools import setup, find_packages
 
setup(
    name='django-oauth-plus',
    version='2.0',
    description='Support of OAuth 1.0a in Django using python-oauth2.',
    author='David Larlet',
    author_email='david@larlet.fr',
    url='http://code.welldev.org/django-oauth-plus/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    # Make setuptools include all data files under version control,
    # svn and CVS by default
    include_package_data=True,
    zip_safe=False,
    # Tells setuptools to download setuptools_git before running setup.py so
    # it can find the data files under Hg version control.
    setup_requires=['setuptools_hg'],
)
