import logging
import os
import sys

from nose.plugins import Plugin

log = logging.getLogger('nose.plugins.nosegunit')


class NoseGunit(Plugin):
    name = 'nosegunit'

    def options(self, parser, env=os.environ):
        super(NoseGunit, self).options(parser, env=env)

        parser.add_option(
            '--gae-lib-path', default='/usr/local/google_appengine',
            dest='gae_lib_path',
            help='Set the path to the directory of the GAE SDK installation')

    def configure(self, options, conf):
        super(NoseGunit, self).configure(options, conf)

        if not self.enabled:
            return

        if sys.version_info[0:2] < (2,5):
            raise EnvironmentError(
                "Python version must be greater than 2.5. Current running: %s" %
                sys.version)

        if options.gae_lib_path:
            self.gae_path = options.gae_lib_path
            sys.path.append(self.gae_path)

        current_path = sys.path[:]

        from dev_appserver import fix_sys_path
        fix_sys_path()

        sys.path.extend(current_path)
