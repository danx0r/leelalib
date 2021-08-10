########################################################################
# This is all the configuration data for pyvision.
# Everything is configured by environment variables.
# Additional configuration could also come from s3://leela-videos/PROJECTNAME/pyvision-config.json


import os
import sys
import json


########################################################################


def getenv_warn(var, default=None):
    if var not in os.environ:
        print("WARNING: Environment variable " + var + " not defined. Using default: " + str(default))
    return os.environ.get(var, default)

def env_string(var):
    return getenv_warn(var, '')


def env_int(var):
    return int(getenv_warn(var, '0'))


def env_float(var):
    return float(getenv_warn(var, '0.0'))


def env_bool(var):
    return getenv_warn(var, 'false').lower() in ('true', 't', 'yes', 'y', 'on', '1')


########################################################################


config = {
    "bugsnag_config": {
        "api_key": env_string('BUGSNAG_API_KEY'),
        "project_root": env_string('BUGSNAG_PROJECT_ROOT'),
    },
    "s3_config": {
        "endpoint_url": env_string('S3_ENDPOINT_URL'),
        "access_key_id": env_string('S3_ACCESS_KEY_ID'),
        "secret_access_key": env_string('S3_SECRET_ACCESS_KEY'),
    },
    "rsmq_config": {
        "host": env_string('RSMQ_HOST'),
        "port": env_int('RSMQ_PORT'),
        "tls": env_bool('RSMQ_TLS'),
        "password": env_string('RSMQ_PASSWORD'),
        "ns": env_string('RSMQ_NS'),
        "vt": env_float('RSMQ_VT'),
        "empty_queue_delay": env_float('RSMQ_EMPTY_QUEUE_DELAY'),
        "trace": env_bool('RSMQ_TRACE'),
    },
    "wamp_config": {
        "url": env_string('WAMP_URL'),
        "realm": env_string('WAMP_REALM')
    },
    "pyvision_config": {
        "project_name": env_string('PYVISION_PROJECT_NAME'),
        "queue_name": env_string('PYVISION_QUEUE_NAME'),
        "output_topic": env_string('PYVISION_OUTPUT_TOPIC'),
        "jwt_secret": env_string('PYVISION_JWT_SECRET'),
        "queues": {
            "posedetection": {
                "config_path": "configs/quick_schedules/keypoint_rcnn_R_50_FPN_inference_acc_test.yaml",
                "config_options": None,
                "custom_dataset_path": None,
                "compute_contours": False,
                "confidence_threshold": 0.3,
                "output_suffix": ".pose.jsonl",
            },
            "objectdetection": {
                "config_path": None,
                "config_options": None,
                "custom_dataset_path": None,
                "compute_contours": False,
                "confidence_threshold": 0.3,
                "output_suffix": ".object.jsonl",
            },
        },
    },
}


########################################################################
