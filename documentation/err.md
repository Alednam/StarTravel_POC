
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/usr/lib/python3.13/threading.py", line 1043, in _bootstrap_inner
    self.run()
    ~~~~~~~~^^
  File "/usr/lib/python3.13/threading.py", line 994, in run
    self._target(*self._args, **self._kwargs)
    ~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
    ~~^^^^^^^^^^^^^^^^^
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/core/management/commands/runserver.py", line 134, in inner_run
    self.check(**check_kwargs)
    ~~~~~~~~~~^^^^^^^^^^^^^^^^
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/core/management/base.py", line 496, in check
    all_issues = checks.run_checks(
        app_configs=app_configs,
    ...<2 lines>...
        databases=databases,
    )
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/core/checks/registry.py", line 89, in run_checks
    new_errors = check(app_configs=app_configs, databases=databases)
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/core/checks/urls.py", line 136, in check_custom_error_handlers
    handler = resolver.resolve_error_handler(status_code)
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/urls/resolvers.py", line 743, in resolve_error_handler
    callback = getattr(self.urlconf_module, "handler%s" % view_type, None)
                       ^^^^^^^^^^^^^^^^^^^
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/utils/functional.py", line 47, in __get__
    res = instance.__dict__[self.name] = self.func(instance)
                                         ~~~~~~~~~^^^^^^^^^^
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/urls/resolvers.py", line 722, in urlconf_module
    return import_module(self.urlconf_name)
  File "/usr/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1027, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/mfalme/Theories/science_calculator/scicalc/urls.py", line 22, in <module>
    path('', include('science_engine.urls')),
             ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/mfalme/Theories/science_calculator/venv/lib/python3.13/site-packages/django/urls/conf.py", line 39, in include
    urlconf_module = import_module(urlconf_module)
  File "/usr/lib/python3.13/importlib/__init__.py", line 88, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
           ~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1387, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1360, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1331, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 935, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 1027, in exec_module
  File "<frozen importlib._bootstrap>", line 488, in _call_with_frames_removed
  File "/home/mfalme/Theories/science_calculator/science_engine/urls.py", line 2, in <module>
    from . import views
  File "/home/mfalme/Theories/science_calculator/science_engine/views.py", line 3, in <module>
    from .logic import Scientist
  File "/home/mfalme/Theories/science_calculator/science_engine/logic.py", line 201
    """
    ^^^
IndentationError: expected an indented block after function definition on line 200
^C
