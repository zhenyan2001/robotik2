import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'my_first_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.*')),
        (os.path.join('share', package_name, 'config'), glob('config/*.yaml')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robolab',
    maintainer_email='robolab@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [ 'emptynode = my_first_package.robotik2:main',
                            'my_pub = my_first_package.publish:main',
                            'my_sub = my_first_package.subscribe:main',
        ],
    },
)
