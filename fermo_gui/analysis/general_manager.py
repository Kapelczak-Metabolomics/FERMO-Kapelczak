"""Manages general functionality

Copyright (c) 2022-present Mitja Maximilian Zdouc, PhD

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import json
from pathlib import Path
from typing import Any

from celery import uuid
from flask_mail import Message

from fermo_gui.config.extensions import mail


class GeneralManager:
    """Organize general functionality such as data management"""

    @staticmethod
    def create_uuid(location: str) -> str:
        """Create task id and check if not already used

        Arguments:
            location: the location of the upload dirs with task id names

        Returns:
            A unique UUID task identifier
        """
        while True:
            task_id = uuid()
            if not Path(location).joinpath(task_id).exists():
                return task_id

    @staticmethod
    def create_upload_dir(location: str, task_id: str) -> str:
        """Create a task-specific directory for data upload

        Arguments:
            location: the location of the upload dir
            task_id: the task identifier

        Returns:
            A string indicating the specific upload dir path
        """
        path = Path(location).joinpath(task_id)
        path.mkdir()
        return str(path.resolve())

    @staticmethod
    def store_data_as_json(location: str, filename: str, data: dict):
        """Stores data as a json file under the filename in the specified location.

        Arguments:
            location: the location of the upload dir
            filename: the filename identifier
            data: the specified user-provided parameters
        """
        location = Path(location)
        with open(location.joinpath(filename), "w") as outfile:
            outfile.write(json.dumps(data, indent=4, ensure_ascii=False))

    @staticmethod
    def read_data_from_json(location: str, filename: str) -> dict:
        """Read file filename from the specified location.

        Arguments:
            location: the location of the upload dir
            filename: the filename identifier
        """
        location = Path(location)
        with open(location.joinpath(filename)) as infile:
            params = json.load(infile)
        return params

    @staticmethod
    def email_notify_success(root_url: str, address: str, job_id: str):
        """Notify user if job completed successfully

        Arguments:
            root_url: URL to construct link
            address: the user-provided email address
            job_id: the job identifier
        """
        msg = Message()
        msg.recipients = [address]
        msg.subject = "Fermo Job Successful (NOREPLY)"
        msg.body = (
            "Dear user, \n"
            "\n"
            "your job with the ID \n"
            f"{job_id}\n"
            "has completed successfully. \n"
            "Please follow this link to see the results: \n"
            f"{root_url}/results/{job_id}/.\n"
            "\n"
            "Kind regards, \n"
            "the FERMO team. \n"
        )
        mail.send(msg)

    @staticmethod
    def email_notify_fail(root_url: str, address: str, job_id: str):
        """Notify user that job failed

        Arguments:
            root_url: URL to construct link
            address: the user-provided email address
            job_id: the job identifier
        """
        msg = Message()
        msg.recipients = [address]
        msg.subject = "Fermo Job Failed (NOREPLY)"
        msg.body = (
            "Dear user, \n"
            "\n"
            "your job with the ID \n"
            f"{job_id}\n"
            "has failed. \n"
            "Please follow this link to see the fail log: \n"
            f"{root_url}/results/job_failed/{job_id}/.\n"
            "\n"
            "Kind regards, \n"
            "the FERMO team. \n"
        )
        mail.send(msg)
