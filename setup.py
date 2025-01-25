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
    maintainer='g288-pc',
    maintainer_email='g288-pc@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "talker = mobile_manipurator.talker1:main",
            "listener = mobile_manipurator.listener1:main"
        ],
    },
)
