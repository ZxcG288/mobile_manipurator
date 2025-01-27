from setuptools import find_packages, setup

package_name = 'mobile_manipurator'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ZxcG288',
    maintainer_email='kangval.work@gmail.com',
    description='A package for mobile manipulator project',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talker = mobile_manipurator.talker1:main",
            "listener = mobile_manipurator.listener1:main",
            "project1 = mobile_manipurator.project1:main" 
        ],
    },
)
