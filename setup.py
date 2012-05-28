from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='cs.discussionextender',
      version=version,
      description="This product extends plone.app.discussion's from with 2 extra fields: email and url",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='discussion extender',
      author='Mikel Larreategi',
      author_email='mlarreategi@codesyntax.com',
      url='http://github.com/codesyntax/cs.discussionextender',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['cs'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.app.discussion',
          'z3c.jbot'
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
