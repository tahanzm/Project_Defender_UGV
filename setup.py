import os
from glob import glob
from setuptools import find_packages, setup

package_name = 'defender_ugv_sim'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # --- BURADAN AŞAĞISINI EKLE ---
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*.urdf')),
        # -----------------------------
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='taha',
    maintainer_email='taha@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'display = defender_ugv_sim.display:main',  # Bu zaten vardır (örnek)
            'camera_reader = defender_ugv_sim.camera_reader:main', # <-- BU SATIRI EKLE
        ],
    },
)
