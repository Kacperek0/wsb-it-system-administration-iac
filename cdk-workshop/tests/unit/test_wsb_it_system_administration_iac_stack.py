import aws_cdk as core
import aws_cdk.assertions as assertions

from wsb_it_system_administration_iac.wsb_it_system_administration_iac_stack import WsbItSystemAdministrationIacStack

# example tests. To run these tests, uncomment this file along with the example
# resource in wsb_it_system_administration_iac/wsb_it_system_administration_iac_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = WsbItSystemAdministrationIacStack(app, "wsb-it-system-administration-iac")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
