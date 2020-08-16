from setuptools import setup, find_packages

setup(
    name='desafio_iafront',
    version='',
    packages=find_packages(),
    url='',
    license='',
    author='Time IA-FRONT',
    author_email='',
    description='',
    install_requires=[
        "scikit-learn==0.23.1",
        "click==7.1.2",
        "bokeh==2.1.1",
        "dataset-loader==1.6",
        'pandas==1.1.0',
        'numpy==1.19.1'
    ],
    entry_points={
        'console_scripts': [
            'prepara-pedidos=desafio_iafront.jobs.pedidos.job_pedidos:main',
            'cria-visitas=desafio_iafront.jobs.create_visits:main',
            'normalize=desafio_iafront.jobs.escala_pedidos.job_normalizacao:main',
            'clustering=desafio_iafront.jobs.clusters.job_kmeans:main',
            'plot=desafio_iafront.jobs.graphics.job_graphics:main',
        ]
    }
)
