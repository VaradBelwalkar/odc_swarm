something = [
    {
        "ID": "fokys7y9yfg7z0idhszn4x115",
        "Version": {
            "Index": 25
        },
        "CreatedAt": "2022-11-13T13:39:36.988341337Z",
        "UpdatedAt": "2022-11-13T13:40:03.861447377Z",
        "Spec": {
            "Name": "interesting_vaughan",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "base_ubuntu:latest",
                    "StopGracePeriod": 10000000000,
                    "DNSConfig": {},
                    "Isolation": "default"
                },
                "Resources": {},
                "RestartPolicy": {
                    "Condition": "any",
                    "Delay": 5000000000,
                    "MaxAttempts": 0
                },
                "Placement": {},
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            },
            "UpdateConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "RollbackConfig": {
                "Parallelism": 1,
                "FailureAction": "pause",
                "Monitor": 5000000000,
                "MaxFailureRatio": 0,
                "Order": "stop-first"
            },
            "EndpointSpec": {
                "Mode": "vip",
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "TargetPort": 22,
                        "PublishedPort": 49148,
                        "PublishMode": "ingress"
                    }
                ]
            }
        },
        "PreviousSpec": {
            "Name": "interesting_vaughan",
            "Labels": {},
            "TaskTemplate": {
                "ContainerSpec": {
                    "Image": "base_ubuntu",
                    "Isolation": "default"
                },
                "ForceUpdate": 0,
                "Runtime": "container"
            },
            "Mode": {
                "Replicated": {
                    "Replicas": 1
                }
            }
        },
        "Endpoint": {
            "Spec": {
                "Mode": "vip",
                "Ports": [
                    {
                        "Protocol": "tcp",
                        "TargetPort": 22,
                        "PublishedPort": 49148,
                        "PublishMode": "ingress"
                    }
                ]
            },
            "Ports": [
                {
                    "Protocol": "tcp",
                    "TargetPort": 22,
                    "PublishedPort": 49148,
                    "PublishMode": "ingress"
                }
            ],
            "VirtualIPs": [
                {
                    "NetworkID": "lr6dlkuquzn4esnicmzi62hvx",
                    "Addr": "10.0.0.3/24"
                }
            ]
        },
        "UpdateStatus": {
            "State": "completed",
            "StartedAt": "2022-11-13T13:39:37.041556905Z",
            "CompletedAt": "2022-11-13T13:40:03.861350926Z",
            "Message": "update completed"
        }
    }
]


port = something[0]["Endpoint"]['Ports'][0]['PublishedPort']

print(port)