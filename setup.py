from setuptools import setup, Extension
import numpy as np

try:
    from Cython.Build import cythonize
    ext_modules = cythonize(['shorttext/metrics/dynprog/dldist.pyx',
                             'shorttext/metrics/dynprog/lcp.pyx',
                             'shorttext/spell/edits1_comb.pyx'])
except ImportError:
    ext_modules = [Extension('shorttext.metrics.dynprog.dldist', ['shorttext/metrics/dynprog/dldist.c']),
                   Extension('shorttext.metrics.dynprog.lcp', ['shorttext/metrics/dynprog/lcp.c']),
                   Extension('shorttext.spell.edits1_comb', ['shorttext/spell/edits1_comb.c'])]

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='shorttext',
      version="1.0.3",
      description="Short Text Mining",
      long_description="Short text mining algorithms, involving word-embedding models, topic models, edit distances, Word Mover's distance, deep learning etc.",
      classifiers=[
          "Topic :: Scientific/Engineering :: Artificial Intelligence",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Text Processing :: Linguistic",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Cython",
          "Programming Language :: C",
          "Natural Language :: English",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Intended Audience :: Education",
          "Intended Audience :: Information Technology",
          "Intended Audience :: Science/Research"
      ],
      keywords="shorttext natural language processing text mining",
      url="https://github.com/stephenhky/PyShortTextCategorization",
      author="Kwan-Yuet Ho",
      author_email="stephenhky@yahoo.com.hk",
      license='MIT',
      ext_modules=ext_modules,
      packages=['shorttext',
                'shorttext.utils',
                'shorttext.classifiers',
                'shorttext.classifiers.embed',
                'shorttext.classifiers.embed.nnlib',
                'shorttext.classifiers.embed.sumvec',
                'shorttext.classifiers.bow',
                'shorttext.classifiers.bow.topic',
                'shorttext.classifiers.bow.maxent',
                'shorttext.data',
                'shorttext.stack',
                'shorttext.generators',
                'shorttext.generators.bow',
                'shorttext.generators.charbase',
                'shorttext.generators.seq2seq',
                'shorttext.metrics',
                'shorttext.metrics.dynprog',
                'shorttext.metrics.wasserstein',
                'shorttext.metrics.embedfuzzy',
                'shorttext.spell'],
      package_dir={'shorttext': 'shorttext'},
      package_data={'shorttext': ['data/*.csv', 'utils/*.txt',
                                  'metrics/dynprog/*.pyx', 'metrics/dynprog/*.c',
                                  'spell/*.pyx', 'spell/*.c']},
      include_dirs=[np.get_include()],
      setup_requires=['numpy>=1.11.3', 'scipy==1.1.0'],
      install_requires=[
          'Cython', 'numpy>=1.11.3', 'scipy==1.1.0', 'scikit-learn==0.19.1', 'keras>=2.0.0', 'gensim>=3.2.0',
          'pandas', 'spacy>=1.7.0', 'pulp', 'PyStemmer',
      ],
      tests_require=[
          'unittest2', 'keras>=2.0.0', 'gensim>=3.2.0', 'tensorflow',
      ],
      scripts=['bin/ShortTextCategorizerConsole',
               'bin/ShortTextWordEmbedSimilarity',
               'bin/switch_kerasbackend'],
      # include_package_data=False,
      test_suite="test",
      zip_safe=False)
