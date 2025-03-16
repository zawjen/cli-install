import time
from sdk.logger import Logger

def test_logger(monkeypatch):
    logger = Logger()
    messages = []
    def fake_print(msg):
        messages.append(msg)
    monkeypatch.setattr('builtins.print', fake_print)
    start_time = time.time()
    logger.log('Test message', start_time)
    assert any('Test message' in m for m in messages)
