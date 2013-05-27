from distutils.core import setup

__author__ = 'stkiller'
setup(name='EvePlanner',
      version='1.0',
      description='Gui application for monitoring and planning the development of Eve Online character',
      author='Podoprigora Andrei',
      packages=['config', 'eveapi', 'eveapi_objects', 'eveapi_objects.account', 'eveapi_objects.character', 'eveapi_objects.corporation',
                'eveapi_objects.eve', 'eveapi_objects.map', 'eveapi_objects.misc', 'eveapi_objects.server', 'eveapi_wrapper', 'eveplanner',
                'tools', 'ui'], requires=['Pillow'])
