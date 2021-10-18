from setuptools import setup

setup(
    name='GSE153056_anndata',
    author='',
    version='0.0.1',
    include_package_data=True,
    description='',
    packages=[
        'GSE153056_anndata',
    ],
    package_data={
        '': ['*.hdf5']
    },
    install_requires=[
        'GitPython'
    ]
)

def pull_first():
    import os
    import git
    cwd = os.getcwd()
    gitdir = os.path.dirname(os.path.realpath(__file__))
    os.chdir(gitdir)
    g = git.cmd.Git(gitdir)
    try:
        g.execute(['git', 'lfs', 'pull'])
    except git.exc.GitCommandError:
        raise RuntimeError("Make sure git-lfs is installed!")
    os.chdir(cwd)
pull_first()