import os
import subprocess

from aws_cdk import (
    Duration,
    Stack,
    aws_lambda as lambda_,
    aws_events as events,
    aws_events_targets as events_targets
    # aws_sqs as sqs,
)
from constructs import Construct

class WsbItSystemAdministrationIacStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        wsb_lambda = lambda_.Function(
            self,
            'WsbLambda',
            code=lambda_.Code.from_asset('code'),
            runtime=lambda_.Runtime.PYTHON_3_9,
            handler='handler.lambda_handler',
            timeout=Duration.seconds(30),
            memory_size=128,
            layers=[
                self.create_dependencies_layer('WsbLambda')
            ]
        )

        event_rule = events.Rule(
            self,
            'WsbEventRule',
            rule_name='WsbEventRule',
            schedule=events.Schedule.cron(
                minute='0',
                hour='0',
                day='*',
                month='*'
            )
        )

        event_rule.add_target(
            events_targets.LambdaFunction(wsb_lambda)
        )

    def create_dependencies_layer(self, function_name: str) -> lambda_.LayerVersion:
        requirements_file = 'code/requirements.txt'
        output_dir = '.lambda_dependencies' + function_name

        if not os.environ.get('SKIP_PIP'):
            subprocess.check_call(f'pip install -r {requirements_file} -t {output_dir}/python'.split())

        return lambda_.LayerVersion(
            self,
            function_name + '-dependencies',
            code=lambda_.Code.from_asset(output_dir)
        )


