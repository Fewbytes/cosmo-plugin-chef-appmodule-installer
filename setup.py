__author__ = 'dank'

import setuptools

COSMO_CELERY_VERSION = "0.1.1"
COSMO_CELERY_BRANCH = "master"
COSMO_CELERY = "https://github.com/CloudifySource/cosmo-celery-common/tarball/{0}".format(COSMO_CELERY_BRANCH)


CHEF_CLIENT_COMMON_VERSION = "0.1.0"
CHEF_CLIENT_COMMON_BRANCH = "master"
CHEF_CLIENT_COMMON = "https://github.com/CloudifySource/cosmo-plugin-chef-client-common/tarball/{0}".format(CHEF_CLIENT_COMMON_BRANCH)


setuptools.setup(
    zip_safe=False,
    name='cosmo-plugin-chef-appmodule-installer',
    version='0.1.0',
    author='yoni',
    author_email='yoni@fewbytes.com',
    packages=['chef_appmodule_installer'],
    license='LICENSE',
    description='Chef plugin implementing comso appmodule installer interface',
    install_requires=[
        "celery",
        "cosmo-celery-common",
        "cosmo-plugin-chef-client-common"
    ],
    dependency_links=["{0}#egg=cosmo-celery-common-{1}".format(COSMO_CELERY, COSMO_CELERY_VERSION),
                      "{0}#egg=cosmo-plugin-chef-client-common-{1}".format(CHEF_CLIENT_COMMON, CHEF_CLIENT_COMMON_VERSION)]
)
