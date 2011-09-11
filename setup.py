from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess, os

class pre_install(install):
    def run(self):
        install.run(self)

        script = os.path.join(self.install_lib, 'apache2', 'a2reload')
        
        subprocess.call(['gcc', script + '.c', '-o', script])
        os.remove(script + '.c')
        subprocess.call(['chown', 'root:root', script])
        subprocess.call(['chmod', '4755', script])
        

setup(
    name='apache2',
    version='1.0',
    description='Apache2 reload module',
    long_description=open('README.rst').read(),
    author='Maccesch',
    author_email='maccesch@gmail.com',
    url='http://github.com/maccesch/apache2',
    packages=find_packages(),
    keywords='contact form django cms django-cms spam protection email',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: Unix',
        'Programming Language :: Python',
    ],
    license='BSD License',
    include_package_data=True,
    zip_safe=False,
    install_requires=[],
    cmdclass={'install': pre_install },
)
