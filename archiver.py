#! /usr/bin/env python

import executor

import json


class Archiver(executor.Executor):

    def archive(self):
        self.ds.safe_archive_all(self.config.archive_threshold)


if __name__ == "__main__":
    archiver = Archiver()
    archiver.archive()
