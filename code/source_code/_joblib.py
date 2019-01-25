from __future__ import absolute_import
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 19:03:33 2018

@author: Shyam
"""

# We need the absolute_import to avoid the local joblib to override the
# site one

import os as _os
import warnings as _warnings

# An environment variable to use the site joblib
if _os.environ.get('SKLEARN_SITE_JOBLIB', False):
    with _warnings.catch_warnings():
        _warnings.simplefilter("ignore")
        # joblib imports may raise DeprecationWarning on certain Python
        # versions
        import joblib
        from joblib import logger
        from joblib import dump, load
        from joblib import __version__
        from joblib import effective_n_jobs
        from joblib import hash
        from joblib import cpu_count, Parallel, Memory, delayed
        from joblib import parallel_backend, register_parallel_backend
else:
    from sklearn.externals import joblib
    from sklearn.externals.joblib import logger
    from sklearn.externals.joblib import dump, load
    from sklearn.externals.joblib import __version__
    from sklearn.externals.joblib import effective_n_jobs
    from sklearn.externals.joblib import hash
    from sklearn.externals.joblib import cpu_count, Parallel, Memory, delayed
    from sklearn.externals.joblib import parallel_backend, register_parallel_backend


__all__ = ["parallel_backend", "register_parallel_backend", "cpu_count",
           "Parallel", "Memory", "delayed", "effective_n_jobs", "hash",
           "logger", "dump", "load", "joblib", "__version__"]