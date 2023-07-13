import os.path

def pre_mutation(context):
    if context.filename == 'integration_test.py':
        context.skip = True