import time

import pytest


@pytest.fixture(scope='session',autouse=True)
def manage_logs(request):
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    log_name = 'output/log/' + now + '.logs'
    request.config.pluginmanager.get_plugin("logging-plugin").set_log_path(log_name)
