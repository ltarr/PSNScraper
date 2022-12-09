import os

class Config:
    PSN_SHA_256 = os.environ.get('PSN_SHA_256') or '4ce7d410a4db2c8b635a48c1dcec375906ff63b19dadd87e073f8fd0c0481d35'
